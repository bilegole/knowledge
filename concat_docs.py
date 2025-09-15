#!/usr/bin/env python3
"""
将 docs 目录下的所有“文本文件”的内容原样拼接后，输出到当前工作目录的 output.txt。

特性与说明：
- 递归遍历 docs/ 目录；
- 采用二进制方式读写，保留源文件的字节序与换行符，不做任何额外分隔或改写；
- 使用简单启发式判断“文本文件”：
  * 若样本中包含 NUL 字节，或不可打印控制字符比例过高，则视为二进制文件并跳过；
  * 这样可以避免误将图片等二进制资源写入输出；
- 为保证可重复性，按相对路径字典序排序后依次拼接；

使用方法：
- 在项目根目录执行：
    python concat_docs.py
- 可选参数：
    python concat_docs.py --docs docs --out output.txt

注意：
- 输出文件 output.txt 写在“当前工作目录”中（即你运行脚本的目录）。
- 若 output.txt 已存在，将被覆盖。
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Iterable, List

# 允许的控制字符（常见文本中的空白/换行控制）
_ALLOWED_CTRL = {9, 10, 12, 13}  # TAB, LF, FF, CR


def is_probably_text(filepath: Path, sample_size: int = 4096, max_ctrl_ratio: float = 0.3) -> bool:
    """基于启发式判断文件是否是“文本”。

    规则：
    - 若样本中出现 NUL 字节(0x00) → 视为二进制，返回 False；
    - 统计样本中属于不可打印控制字节(0x00-0x1F 但不在允许集内)的比例，若比例大于阈值 → 返回 False；
    - 否则返回 True。
    """
    try:
        with open(filepath, 'rb') as f:
            blob = f.read(sample_size)
    except OSError:
        return False

    if not blob:
        # 空文件当作文本处理
        return True

    if b"\x00" in blob:
        return False

    ctrl_total = 0
    for b in blob:
        if b < 32 and b not in _ALLOWED_CTRL:
            ctrl_total += 1
    ratio = ctrl_total / len(blob)
    if ratio > max_ctrl_ratio:
        return False

    return True


def iter_doc_files(docs_dir: Path) -> Iterable[Path]:
    """遍历 docs 目录下的所有文件，过滤出“文本文件”。"""
    for root, _dirs, files in os.walk(docs_dir):
        for name in files:
            p = Path(root) / name
            # 快速跳过常见二进制扩展名（加速与保险）
            if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.ico', '.svg', '.pdf', '.zip', '.gz'}:
                continue
            if is_probably_text(p):
                yield p


def concat_files_to_output(files: List[Path], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'wb') as out:
        for fp in files:
            with open(fp, 'rb') as f:
                # 直接原样写入
                while True:
                    chunk = f.read(1024 * 1024)
                    if not chunk:
                        break
                    out.write(chunk)


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='拼接 docs 目录下的文本文件为一个 output.txt（原样字节拼接）。')
    parser.add_argument('--docs', default='docs', help='待遍历的目录（默认：docs）')
    parser.add_argument('--out', default='output.txt', help='输出文件路径（相对当前工作目录，默认：output.txt）')
    args = parser.parse_args(argv)

    docs_dir = Path(args.docs)
    if not docs_dir.exists() or not docs_dir.is_dir():
        print(f"[错误] 找不到目录：{docs_dir}", file=sys.stderr)
        return 2

    files = sorted(iter_doc_files(docs_dir), key=lambda p: str(p.relative_to(docs_dir)).lower())

    if not files:
        print('[提示] 未在 docs 目录下找到可识别的文本文件。', file=sys.stderr)

    out_path = Path(args.out)
    try:
        concat_files_to_output(files, out_path)
    except Exception as e:
        print(f"[错误] 写入输出失败：{e}", file=sys.stderr)
        return 1

    print(f"已生成：{out_path.resolve()}  （共 {len(files)} 个文件拼接）")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
