import timeit
try:
    from pyranoid_ver import pyranoid_version
except ImportError:
    pyranoid_version = "N/A"
from os import devnull, system, sync
from sys import hexversion
from sys import stdout as sys_stdout
from sys import exit as sys_exit
try:
    from crc32c import crc32c as crc32  # crc32c for intel
except ImportError:
    from zlib import crc32  # standard crc32
    pass
import re  # regex
import shutil  # High-level file copy
import json  # saving/loading JSON files
import itertools
from time import sleep, mktime  # For timeouts and time output
from datetime import datetime
from argparse import ArgumentParser  # Set variables via parameters
from pathlib import Path
try:
    from colorama import Fore, Style, init, deinit
    init(autoreset=True)
except ImportError:
    print("For better readability, please install colorama: pip install colorama")
    sleep(2)

    # DEF: create empty strings and functions for everything necessary:
    class Fore():
        BLACK = ""
        RED = ""
        GREEN = ""
        YELLOW = ""
        BLUE = ""
        MAGENTA = ""
        CYAN = ""
        WHITE = ""
        RESET = ""
        LIGHTBLACK_EX = ""
        LIGHTRED_EX = ""
        LIGHTGREEN_EX = ""
        LIGHTYELLOW_EX = ""
        LIGHTBLUE_EX = ""
        LIGHTMAGENTA_EX = ""
        LIGHTCYAN_EX = ""
        LIGHTWHITE_EX = ""

    class Style():
        DIM = ""
        NORMAL = ""
        BRIGHT = ""
        RESET_ALL = ""

    def deinit():
        pass

    pass
try:
    from tqdm import tqdm
except ImportError:
    print(Style.BRIGHT + Fore.RED + "Please install tqdm: " + Fore.WHITE + "pip install tqdm")
    sleep(3)
    sys_exit("Please install tqdm:\tpip install tqdm")


def search_files(where="/home/floadmin/Pictures/_CANON/Privat/"):
    found_files = []
    """ DEF:
        [0] full source path
        [1] file name
        [2] basename
        [3] extension
        [4] size
        [5] mod-date
        [6] hash
        [7] full target path(s) (list)
    """
    recurse = '**/*.*'

    try:
        for i in tqdm(where, desc="Paths", unit="Paths",
                    bar_format="    {desc}: {n_fmt}/{total_fmt} |{bar}| {elapsed}<{remaining}"):
            for j in Path(i).glob(recurse):
                j = Path(j).resolve()
                    j_stat = j.stat()
                    found_files += [[str(j),
                                    j.name,
                                    j.stem,
                                    j.suffix,
                                    j_stat.st_size,
                                    j_stat.st_mtime,
                                    "XYZ",
                                    []]]

        found_files = sorted(found_files, key=lambda attris: attris[0])  # For %c in param['naming_file'].
    except Exception:
        print(Style.BRIGHT + Fore.RED + "    " + "Error while searching files!")
    return found_files

