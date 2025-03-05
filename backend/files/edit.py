import os

# Fayllar turgan joy (papka yo'li)
folder = '.'  # BU YERGA O'Z PAPKANGIZ YO'LINI YOZING

# MP3 fayllarni yig'ib olish
files = [f for f in os.listdir(folder) if f.startswith('UNIT-') and f.endswith('.mp3')]

# Fayllarni 1.1, 1.2, 2.1 tartibiga qarab saralash
def extract_key(filename):
    parts = filename.replace('UNIT-', '').replace('.mp3', '').split('.')
    return int(parts[0]), int(parts[1])

files.sort(key=extract_key)
print("hello world")
# Har bir faylga tartib raqami berib qayta nomlash
for index, file in enumerate(files, start=1):
    new_name = f'{index:03d}-{file}'  # 001-UNIT-1.1.mp3
    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)

print("✅ Barcha fayllar tartiblandi va nomlari yangilandi!")
