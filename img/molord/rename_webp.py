import os
import re
from PIL import Image

def rename_and_convert_images():
    folder = os.getcwd()
    files = os.listdir(folder)

    pattern = re.compile(r'\D*(\d+)\D*')  # 用于提取文件名中的数字

    for filename in files:
        name, ext = os.path.splitext(filename)
        ext_lower = ext.lower()

        # 先去除括号和空格
        clean_name = name.replace('(', '').replace(')', '').replace(' ', '')

        # 如果有改名需求（文件名或扩展名没变也算没改名）
        if clean_name != name:
            new_filename = clean_name + ext_lower
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_filename)
            if filename != new_filename:
                if os.path.exists(new_path):
                    print(f"重命名目标已存在，跳过: {new_filename}")
                else:
                    os.rename(old_path, new_path)
                    print(f"去括号重命名：{filename} → {new_filename}")
            filename = new_filename
            name = clean_name
        else:
            filename = filename  # 无变化，保持原名

        old_path = os.path.join(folder, filename)

        # 处理图片文件格式和重命名
        if ext_lower in ['.png', '.jpg', '.jpeg']:
            # 转成 webp，重命名格式 molord_<数字>.webp
            match = pattern.match(name)
            if not match:
                print(f"跳过无数字图片文件：{filename}")
                continue
            number = match.group(1)
            new_name = f"molord_{number}.webp"
            new_path = os.path.join(folder, new_name)

            try:
                img = Image.open(old_path).convert("RGBA")
                img.save(new_path, "WEBP")
                print(f"转换并保存：{filename} → {new_name}")
                os.remove(old_path)
            except Exception as e:
                print(f"处理文件 {filename} 出错: {e}")

        elif ext_lower == '.webp':
            # webp文件只改名格式，不改格式
            match = pattern.match(name)
            if not match:
                print(f"跳过无数字webp文件：{filename}")
                continue
            number = match.group(1)
            new_name = f"molord_{number}.webp"
            new_path = os.path.join(folder, new_name)
            if filename != new_name:
                if os.path.exists(new_path):
                    print(f"重命名目标已存在，跳过: {new_name}")
                else:
                    os.rename(old_path, new_path)
                    print(f"重命名webp文件：{filename} → {new_name}")

        elif ext_lower == '.gif':
            # gif文件只去括号，不改格式和内容，名字格式 molord_<数字>.gif
            match = pattern.match(name)
            if not match:
                print(f"跳过无数字gif文件：{filename}")
                continue
            number = match.group(1)
            new_name = f"molord_{number}.gif"
            new_path = os.path.join(folder, new_name)
            if filename != new_name:
                if os.path.exists(new_path):
                    print(f"重命名目标已存在，跳过: {new_name}")
                else:
                    os.rename(old_path, new_path)
                    print(f"重命名gif文件：{filename} → {new_name}")

        else:
            # 其他非图片文件，只去括号重命名，不动格式
            pass

if __name__ == "__main__":
    rename_and_convert_images()
