import os
import re

def generate_gallery_html(img_folder):
    # 匹配 molord_数字.webp 或 molord_数字.gif
    pattern = re.compile(r'molord_(\d+)\.(webp|gif)$', re.IGNORECASE)

    files = os.listdir(img_folder)
    # 按数字顺序排序
    files = sorted(
        [f for f in files if pattern.match(f)],
        key=lambda x: int(pattern.match(x).group(1))
    )

    html_lines = ['<div class="image-gallery">']
    for f in files:
        html_lines.append(f'  <img src="/img/molord/{f}">')
    html_lines.append('</div>')

    return "\n".join(html_lines)

if __name__ == "__main__":
    folder_path = os.path.join('source', 'img', 'molord')
    html_output = generate_gallery_html(folder_path)
    print(html_output)
