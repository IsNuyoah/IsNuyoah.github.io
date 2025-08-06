import os
import re

def generate_gallery_html(img_folder):
    folder_name = os.path.basename(img_folder)  # 当前目录名
    # 匹配 当前目录名_数字.webp 或 当前目录名_数字.gif
    pattern = re.compile(rf'{re.escape(folder_name)}_(\d+)\.(webp|gif)$', re.IGNORECASE)

    files = os.listdir(img_folder)
    # 按数字排序
    files = sorted(
        [f for f in files if pattern.match(f)],
        key=lambda x: int(pattern.match(x).group(1))
    )

    # 直接输出 <img> 标签
    for f in files:
        print(f'<img src="/img/{folder_name}/{f}">')

if __name__ == "__main__":
    folder_path = os.getcwd()  # 直接获取当前目录
    generate_gallery_html(folder_path)
