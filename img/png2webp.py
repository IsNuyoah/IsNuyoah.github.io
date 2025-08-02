import os
from PIL import Image

# 图片目录路径（修改为你的绝对路径）
img_dir = r'F:\website\myblog\myblog\source\img'

# 只扫描当前目录，不进入子目录
files = os.listdir(img_dir)

# 过滤出 jpg 和 png 文件（不区分大小写）
img_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# 按文件修改时间排序
img_files = sorted(img_files, key=lambda x: os.path.getmtime(os.path.join(img_dir, x)))

for img_file in img_files:
    full_path = os.path.join(img_dir, img_file)

    # 获取文件修改时间，转成整数时间戳字符串
    mtime = os.path.getmtime(full_path)
    timestamp = str(int(mtime))

    # webp 文件名，避免重名，加上文件名防止覆盖（可选）
    name_without_ext = os.path.splitext(img_file)[0]
    webp_file = f"{timestamp}_{name_without_ext}.webp"
    webp_path = os.path.join(img_dir, webp_file)

    # 打开图片，转成webp保存，quality=80
    with Image.open(full_path) as img:
        img.save(webp_path, "WEBP", quality=80)

    print(f"Converted {img_file} -> {webp_file}")
