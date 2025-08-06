import os
from PIL import Image

def rename_and_convert_images(base_folder):
    for root, dirs, files in os.walk(base_folder):
        folder_name = os.path.basename(root)  # 当前文件夹名
        counter = 1  # 编号从 1 开始

        for filename in sorted(files):
            name, ext = os.path.splitext(filename)
            ext_lower = ext.lower()

            # 去括号和空格
            clean_name = name.replace('(', '').replace(')', '').replace(' ', '')
            old_path = os.path.join(root, filename)

            if clean_name != name:
                filename = clean_name + ext_lower
                new_path = os.path.join(root, filename)
                if not os.path.exists(new_path):
                    os.rename(old_path, new_path)
                    old_path = new_path
                    print(f"去括号重命名：{name+ext} → {filename}")
                else:
                    print(f"重命名目标已存在，跳过: {filename}")
                    old_path = new_path

            # 新文件名
            new_name = f"{folder_name}_{counter}.webp"
            new_path = os.path.join(root, new_name)

            try:
                if ext_lower in ['.png', '.jpg', '.jpeg']:
                    img = Image.open(old_path).convert("RGBA")
                    img.save(new_path, "WEBP", quality=80)
                    img.close()
                    os.remove(old_path)
                    print(f"JPG/PNG 转 WebP：{filename} → {new_name}")

                elif ext_lower == '.gif':
                    # GIF 不压缩，只改名为同名 GIF（保持原格式）
                    gif_new_name = f"{folder_name}_{counter}.gif"
                    gif_new_path = os.path.join(root, gif_new_name)
                    if filename != gif_new_name:
                        if not os.path.exists(gif_new_path):
                            os.rename(old_path, gif_new_path)
                            print(f"重命名 GIF 文件：{filename} → {gif_new_name}")
                        else:
                            print(f"重命名目标已存在，跳过: {gif_new_name}")
                    counter += 1
                    continue  # 跳过下面的 WebP 转换逻辑

                elif ext_lower == '.webp':
                    if filename != new_name:
                        if not os.path.exists(new_path):
                            os.rename(old_path, new_path)
                            print(f"重命名 WebP 文件：{filename} → {new_name}")
                        else:
                            print(f"重命名目标已存在，跳过: {new_name}")

                counter += 1

            except Exception as e:
                print(f"处理文件 {filename} 出错: {e}")


if __name__ == "__main__":
    folder = os.getcwd()
    rename_and_convert_images(folder)
