#!/usr/bin/env python
"""
指定したサイズ以上の画像のパスを並べる

指定したディレクトリを再帰的に調べ、指定px以上のものをリストアップする
"""
from PIL import Image
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="検索を始めるディレクトリ")
parser.add_argument("width", type=int, help="image width px")
parser.add_argument("height", type=int, help="image height px")
args = parser.parse_args()

if not args.dir: # デフォルトの引数の設定
    path = './'
else:
    path = args.dir

path = Path(path)
if not path.is_dir():
    exit()

width = args.width
height = args.height
if height < 1 and width < 1:
    exit()
else:
    set_size = (width, height)

files = list(path.glob('**/*'))   # 指定ディレクトリ以下のファイルを再帰的に列挙
# 画像のみ抽出
img_suffix = ['.png', '.jpg', '.gif']
images = []
for f in files:
    if f.suffix in img_suffix:
        images.append(str(f))

# 指定サイズ以上のみ出力
for img in images:
    if Image.open(img).size > set_size:
        print(img)
