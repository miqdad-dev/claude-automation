import os
import shutil
import sys

def get_files_from_dir(dir_path):
    """
    Get all files from directory
    """
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return files

def categorize_files(files, dir_path):
    """
    Categorize files by their extensions
    """
    categorized_files = {}
    for file in files:
        file_ext = file.split('.')[-1]
        if file_ext not in categorized_files:
            categorized_files[file_ext] = []
        categorized_files[file_ext].append(os.path.join(dir_path, file))
    return categorized_files

def move_files(categorized_files, target_dir):
    """
    Move files to their respective extension-named directories
    """
    for ext in categorized_files:
        target_sub_dir = os.path.join(target_dir, ext)
        if not os.path.exists(target_sub_dir):
            os.makedirs(target_sub_dir)
        for file_path in categorized_files[ext]:
            shutil.move(file_path, target_sub_dir)

def main():
    source_dir = sys.argv[1]
    target_dir = sys.argv[2]
    files = get_files_from_dir(source_dir)
    categorized_files = categorize_files(files, source_dir)
    move_files(categorized_files, target_dir)

if __name__ == '__main__':
    main()