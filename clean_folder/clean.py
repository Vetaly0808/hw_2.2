import os
import glob
import shutil

extensions = {
    "jpg": "images",
    "png": "images",
    "docx": "word",
    "zip": "archive",
    "py": "python",
    "mp3": "audio",
    "mkw": "video"
}

def normalize(name):
    valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(c for c in name if c in valid_chars)

path = ""

for ext, folder_name in extensions.items():
    files = glob.glob(os.path.join(path, f"*.{ext}"))
    print(f"[*]найдено {len(files)} файлов с расширением {ext}.")
    if files:
        folder_name = normalize(folder_name)
        folder_path = os.path.join(path, folder_name)
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)
            print(f"[+] Создана папка {folder_name}.")

        for file in files:
            basename = os.path.basename(file)
            name, ext = os.path.splitext(basename)
            new_name = normalize(name)
            new_basename = f"{new_name}{ext}"
            dst = os.path.join(folder_path, new_basename)
            print(f"[*] Перенесення файл'{file}' в {dst}")
            shutil.move(file, dst)
    else:
        print(f"[!] Файлы с расширением {ext} не найдены.")


