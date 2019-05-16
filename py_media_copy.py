#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  from PyQt5 import QtWidgets
#  from pmc_ui import Ui_MainWindow
from pmc_ver import pmc_version
#  import pmc_preset

import os
import sys
import hashlib  # hash algorithms
import re  # regex
import shutil  # High-level file copy
import json  # saving/loading JSON files
import itertools
#  from collections import defaultdict
# from time import sleep  # For timeouts and time output
from datetime import datetime
from tqdm import tqdm
import argparse  # Set variables via parameters
parser = argparse.ArgumentParser()
parser.add_argument("--source", dest="source",
                    default="./.testing/in",
                    help="Source path(s). Multiple ones like 'path1$path2'")
parser.add_argument("--target", dest="target",
                    default="./.testing/out",
                    help="Target path(s). Multiple ones like 'path1$path2'")
parser.add_argument("--ext-pref", dest="extension_preference",
                    type=int, default=0,
                    help="0 = all; -1 = exclude; 1 = include")
parser.add_argument("--ext-list", dest="extension_list",
                    default="",
                    help="Extensions to in-/exclude. Use like 'ext1$ext2'")
parser.add_argument("--source-r", dest="source_recurse",
                    type=int, default=1,
                    help="Search recursively (i.e. including subfolders) in source(s)")
parser.add_argument("--source-d", dest="source_dedup",
                    type=int, default=1,
                    help="Search for duplicates in source(s)")
parser.add_argument("--source-d-t", dest="source_dedup_tolerance",
                    type=int, default=1,
                    help="Allow 3sec difference for --source-d")
parser.add_argument("--history-d", dest="history_dedup",
                    type=int, default=1,
                    help="Search for duplicates in history-file.")
parser.add_argument("--history-p", dest="history_path",
                    default="./pmc_history.json",
                    help="Path of history-file.")
parser.add_argument("--history-w", dest="history_write",
                    type=int, default=2,
                    help="0 = don't write, 1 = append, -1 = overwrite.")
parser.add_argument("--target-d", dest="target_dedup",
                    type=int, default=0,
                    help="Check for duplicates in target-folder.")
parser.add_argument("--dupli-h", dest="dedup_hash",
                    type=int, default=0,
                    help="Use hashes for dedup-check.")
parser.add_argument("--target-owp", dest="target_protect",
                    type=int, default=1,
                    help="Overwrite-protection.")
parser.add_argument("--naming-sd", dest="naming_subdir",
                    default="%y4%-%M%-%d%_%h%-%m%-%s%",
                    help="Naming scheme for subdirs")
parser.add_argument("--naming-f", dest="naming_file",
                    default="%n",
                    help="Naming scheme for files")
parser.add_argument("--verify", dest="verify",
                    type=int, default=1,
                    help="Verify files via checksum")
parser.add_argument("--verify-h", dest="verify_hash",
                    default="MD5",
                    help="Hash for verification")
parser.add_argument("--target-c", dest="target_compress",
                    type=int, default=0,
                    help="Compress files for target # >1")
parser.add_argument("--unsleep", dest="unsleep",
                    type=int, default=1,
                    help="Prevent system from sleep")
parser.add_argument("--preset", dest="preset",
                    default="default",
                    help="Preset name")
parser.add_argument("--preset-w-source", dest="save_source",
                    type=int, default=0,
                    help="Save source path(s) to preset")
parser.add_argument("--preset-w-target", dest="save_target",
                    type=int, default=0,
                    help="Save target path(s) to preset")
parser.add_argument("--preset-w-settings", dest="save_settings",
                    type=int, default=0,
                    help="Save settings to preset")
parser.add_argument("--verbose", dest="verbose",
                    type=int, default=1,
                    help="Verbose. 2 = file, 1 = console, 0 = none")
param = parser.parse_args()

# DEFINITION: Set print location (none/terminal/file)
if (param.verbose == 2):
    f = open("./pmc.log", mode='a+')
elif (param.verbose == 0):
    f = open(os.devnull, 'w')
    sys.stdout = f
else:
    f = sys.stdout

#  for glob:
if sys.hexversion < 0x030500F0:
    print("Cannot run py_media-copy on versions older than 3.5 - sorry!", file=sys.stderr)
    f.close()
    sys.exit(0)

print('\x1b[1;33;40m' + pmc_version + '\x1b[0m', file=f)

# ==================================================================================================
# ==============================================================================
#    Setting functions:
# ==============================================================================
# ==================================================================================================

""" GUI:
    testvar = "meine testvariable /home/bla"
    class getvariable:
        def __init__(self):
            md5 = hashlib.md5()
            blocksize = 2**20
            with open(os.path.normpath('./README.md'), "rb") as f:
                while True:
                    buf = f.read(blocksize)
                    if not buf:
                        break
                    md5.update(buf)
            # return md5.hexdigest()


    class mainwindow(QtWidgets.QMainWindow):
        def __init__(self):
            global pmc_version
            super(mainwindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.textedit_outputconsole.append(pmc_version)
            self.ui.textedit_source.setText("Template test\nhallo")
            self.ui.pushbutton_start.clicked.connect(self.startBtnClicked)
            self.ui.pushbutton_exit.clicked.connect(self.close)

        def startBtnClicked(self):
            global testvar
            self.ui.textedit_outputconsole.append("button")
            testvar = self.ui.textedit_source.toPlainText()
            check = getvariable().md5.hexdigest
            print(check, file=f)


    app = QtWidgets.QApplication([])
    application = mainwindow()

    application.ui.textedit_target.setText(testvar)
    application.show()

    sys.exit(app.exec())
"""


# DEFINITION: Search for files, get basic directories:
def search_files(where):
    global f
    global param
    print('\x1b[1;34;40m' + datetime.now().strftime('%H:%M:%S') + ' -- Searching files in ' + where + "..." + '\x1b[0m', file=f)
    found_files = []
    #  also possible: glob
    for root, dirs, files in os.walk(os.path.normpath(where)):
        for file in files:
            # if file.endswith(".CR2"):
            inter_path = os.path.join(root, file)
            inter_regex = re.search(r"(\w*)(\.\w*)$", file)
            inter_stats = os.stat(inter_path)
            """ DEFINITION:
            [0] full path
            [1] file name
            [2] basename
            [3] extension
            [4] size
            [5] mod-date
            [6] hash
            [7] target path
            """
            found_files += [[inter_path, file, inter_regex.group(1), inter_regex.group(2), inter_stats.st_size, inter_stats.st_mtime, "XYZ", "XYZ"]]
    # print(found_files, file=f)

    return found_files


# DEFINITION: Get hashes for files:
def get_hashes(what):
    if sys.hexversion < 0x030600F0:
        algorithm = hashlib.sha1()
        # print("Using SHA1", file=f)
    else:
        algorithm = hashlib.blake2b()
        # print("Using BLAKE2", file=f)
    blocksize = 128*256
    print('\x1b[1;34;40m' + datetime.now().strftime('%H:%M:%S') + ' -- Getting hashes...' + '\x1b[0m', file=f)
    for i in tqdm(what):
        if i[6] == "XYZ":
            with open(i[0], "rb") as file:
                while True:
                    buf = file.read(blocksize)
                    if not buf:
                        break
                    algorithm.update(buf)
                i[6] = algorithm.hexdigest()

    return what


def save_json(what, where):
    print('\x1b[1;34;40m' + datetime.now().strftime('%H:%M:%S') + ' -- Saving JSON ' + where + '...' + '\x1b[0m', file=f)
    try:
        with open(where, 'w+') as outfile:
            json.dump(what, outfile, ensure_ascii=False)
    except:
        print("Error!", file=f)


def load_json(where):
    global param
    print('\x1b[1;34;40m' + datetime.now().strftime('%H:%M:%S') + ' -- Loading JSON ' + where + '...' + '\x1b[0m', file=f)
    try:
        with open(where, 'r+', encoding='utf-8') as file:
            inter = json.load(file)
        return list(inter)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError!", file=f)
        return set()
    except FileNotFoundError:
        print("JSON file not found.", file=f)
        return set()


def create_subfolders(for_what):
    for i in for_what:
        if not os.path.exists(i[7]):
            os.makedirs(i[7])


def copy_files(what):
    print('\x1b[1;34;40m' + datetime.now().strftime('%H:%M:%S') + ' -- Copy files...' + '\x1b[0m', file=f)
    for i in what:
        # shutil.copy2(i[0], i[7])
        print(str(i[0]) + " -> " + str(i[7]))


def print_files(source_files):
    for i in source_files:
        print("\n" + str(i), end="", file=f)

    print("\n", file=f)


def dedup_files(source, compare):
    print('\x1b[1;34;40m' + datetime.now().strftime('%H:%M:%S') + ' -- Dedup files...' + '\x1b[0m', file=f)
    seen_set = compare
    deduped_list = []
    if len(seen_set) >= 1:
        for i in source:
            if tuple([i[1], i[4], i[5]]) not in seen_set:
                deduped_list.append(i)
    else:
        for i in source:
            if tuple([i[1], i[4], i[5]]) not in seen_set:
                deduped_list.append(i)
                seen_set.add(tuple([i[1], i[4], i[5]]))

    return deduped_list


# ==================================================================================================
# ==============================================================================
#    Chronology / Workflow:
# ==============================================================================
# ==================================================================================================

# DEFINITION: search files:
source_files = search_files(param.source)
if len(source_files) <= 1:
    print("No files found!", file=sys.stderr)
    f.close()
    sys.exit(0)
else:
    print(str(len(source_files)) + " files found", file=f)

# DEFINITION: Dedups:
# dedup source:
if param.source_dedup == 1:
    # get hashes:
    if param.verify_hash == 1:
        source_files = get_hashes(source_files)
    source_files = dedup_files(source_files, set())

# dedup history:
if param.history_dedup == 1:
    history_files = load_json(param.history_path)
    # get hashes:
    if param.verify_hash == 1:
        source_files = get_hashes(source_files)
    source_files = dedup_files(source_files, history_files)
    history_files = None

# dedup target:
if param.target_dedup == 1:
    target_files = search_files(param.target)
    target_files = [1], [4], [5]
    # get hashes:
    if param.verify_hash == 1:
        source_files = get_hashes(source_files)
        target_files = get_hashes(target_files)
    source_files = dedup_files(source_files, target_files)
    target_files = None

# DEFINITION: get rest of the hashes:
if param.verify == 1:
    source_files = get_hashes(source_files)

# DEFINITION: prepare paths:

# DEFINITION: Copy:
copy_files(source_files)

# DEFINITION: Verify:

# DEFINITION: write history:
if param.history_write != 0:
    history_files = load_json(param.history_path)
    to_save = source_files
    for i in to_save:
        del i[7]
        del i[3]
        del i[2]
        del i[0]
    if param.history_write == 1 and history_files is not None:
        to_save += history_files

    to_save.sort()
    to_save = list(to_save for to_save, _ in itertools.groupby(to_save))

    save_json(to_save, param.history_path)
    to_save = None
