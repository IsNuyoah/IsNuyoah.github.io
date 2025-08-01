import os
from PIL import Image
import time

# 你的图片目录路径
img_dir = './htb/archetype'

# 遍历所有 PNG 文件，按修改时间排序
png_files = [f for f in os.listdir(img_dir) if f.lower().endswith('.png')]
png_files = sorted(png_files, key=lambda x: os.path.getmtime(os.path.join(img_dir, x)))

for png_file in png_files:
    full_path = os.path.join(img_dir, png_file)

    # 取文件修改时间，生成时间戳字符串
    mtime = os.path.getmtime(full_path)
    timestamp = str(int(mtime))

    # webp 文件名
    webp_file = f"{timestamp}.webp"
    webp_path = os.path.join(img_dir, webp_file)

    # 打开png，转webp保存
    with Image.open(full_path) as img:
        img.save(webp_path, "WEBP", quality=80)

    print(f"Converted {png_file} -> {webp_file}")
