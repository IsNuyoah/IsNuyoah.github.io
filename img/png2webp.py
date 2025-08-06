# import os
# from PIL import Image

# # 图片目录路径（修改为你的绝对路径）
# img_dir = r'F:\website\myblog\myblog\source\img\htb\vaccine'

# # 只扫描当前目录，不进入子目录
# files = os.listdir(img_dir)

# # 过滤出 jpg 和 png 文件（不区分大小写）
# img_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# # 按文件修改时间排序
# img_files = sorted(img_files, key=lambda x: os.path.getmtime(os.path.join(img_dir, x)))

# # 遍历图片文件，按时间戳递增编号生成文件名
# for idx, img_file in enumerate(img_files, start=1):
#     full_path = os.path.join(img_dir, img_file)

#     # 获取文件修改时间，转成整数时间戳字符串
#     mtime = os.path.getmtime(full_path)
#     timestamp = str(int(mtime))

#     # 自动递增编号，格式为两位数字
#     file_number = f"{idx:02d}"

#     # 新的webp文件名，格式为 timestamp-01, timestamp-02 等
#     webp_file = f"{timestamp}-{file_number}.webp"
#     webp_path = os.path.join(img_dir, webp_file)

#     # 打开图片，转成webp保存，quality=80
#     with Image.open(full_path) as img:
#         img.save(webp_path, "WEBP", quality=80)

#     print(f"Converted {img_file} -> {webp_file}")
import os
from pathlib import Path
from PIL import Image
import re

# 图片目录路径
img_dir = Path(r"F:\website\myblog\myblog\source\img\htb\vaccine")

# 获取当前目录所有 PNG/JPG 文件
img_files = [f for f in img_dir.iterdir() if f.suffix.lower() in {".png", ".jpg", ".jpeg"}]

# 按修改时间排序
img_files.sort(key=lambda x: x.stat().st_mtime)

# 转换
for idx, img_path in enumerate(img_files, start=1):
    file_number = f"{idx:02d}"  # 两位编号

    # 匹配日期部分（例：2025-08-04）
    match = re.search(r"\d{4}-\d{2}-\d{2}", img_path.stem)
    if match:
        date_part = match.group()
    else:
        date_part = "unknown-date"  # 如果匹配不到日期

    # 新文件名：日期-编号.webp
    webp_name = f"{date_part}-{file_number}.webp"
    webp_path = img_dir / webp_name

    # 打开图片并保存为 webp
    with Image.open(img_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        img.save(webp_path, "WEBP", quality=80)

    # 删除原文件
    img_path.unlink()

    print(f"Converted {img_path.name} -> {webp_name} (原文件已删除)")
