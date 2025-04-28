import os
import re
import shutil


source_folder = '.'

pattern = re.compile(r'^(\d+)_(\d+)\.py$')


for filename in os.listdir(source_folder):

    match = pattern.match(filename)

    if match:
        
        dest_number, hell_number = match.groups()

        dest_folder = os.path.join(source_folder, f'Dəst {dest_number}')

        new_filename = f'Həll{hell_number}.py'

        os.makedirs(dest_folder, exist_ok=True)

        src_path = os.path.join(source_folder, filename)

        dest_path = os.path.join(dest_folder, new_filename)

        shutil.move(src_path, dest_path)

        print(f"Moved '{filename}' to '{dest_path}'")
