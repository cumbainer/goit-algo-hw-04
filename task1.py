import os
from os import listdir
from os.path import isfile
from pathlib import Path
from shutil import copyfile


def do_recursive_copy(src: str, dest: str = "dist"):
    if not src:
        print("Please provide valid source directory")
        return

    try:
        if isfile(src):
            extension = Path(src).suffix[1:]
            target_dir = os.path.join(dest, extension)
            os.makedirs(target_dir, exist_ok=True)
            file_to_copy = os.path.basename(src)
            try:
                copyfile(src, os.path.join(target_dir, file_to_copy))
            except (OSError, PermissionError) as e:
                print(f"Failed to copy {src}: {e}")
        else:
            try:
                entries = listdir(src)
            except (OSError, PermissionError) as e:
                print(f"Failed to list {src}: {e}")
                return
            for entry in entries:
                full_path = os.path.join(src, entry)
                do_recursive_copy(full_path, dest)
    except OSError as e:
        print(f"Error processing {src}: {e}")


do_recursive_copy("source_dir", "123123")