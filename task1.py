import os
from os import listdir
from os.path import isfile
from pathlib import Path
from shutil import copyfile


def do_recursive_copy(src: str, dest: str = "dist"):
    if not src:
        print("Please provide valid source directory")
        return
    if isfile(src):
        extension = Path(src).suffix[1:]
        if not os.path.exists(extension):
            os.makedirs(f"{dest}/{extension}", exist_ok=True)
        file_to_copy = src.split("/")[-1]
        copyfile(src, f"{dest}/{extension}/{file_to_copy}")
    else:
        [do_recursive_copy(f"{src}/{dir}", dest) for dir in listdir(src) if not isfile(dir)]


do_recursive_copy("source_dir", "123123")
