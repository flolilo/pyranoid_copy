#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from pmc_ui import Ui_MainWindow
from pmc_ver import pmc_version
#  import pmc_preset

import os
import sys
import hashlib  # hash algorithms
import re  # regex
import shutil  # High-level file copy
import json  # saving/loading JSON files
#  from time import localtime, sleep  # For timeouts and time output
import argparse  # Set variables via parameters
parser = argparse.ArgumentParser()
parser.add_argument("--source", dest="source", default="/home/flo/Download",
                    help="Source path(s). Multiple ones like 'path1$path2'")
parser.add_argument("--target", dest="target", default="/tmp/pmc_test",
                    help="Target path(s). Multiple ones like 'path1$path2'")
parser.add_argument("--ext-pref", type=int, default=0, dest="extension_preference",
                    help="0 = all; -1 = exclude; 1 = include")
parser.add_argument("--ext-list", dest="extension_list", default="",
                    help="Extensions to in-/exclude. Use like 'ext1$ext2'")
parser.add_argument("--source-r", dest="source_recurse", type=int, default=1,
                    help="Search recursively (i.e. including subfolders) in source(s)")
parser.add_argument("--source-d", dest="source_dedup", type=int, default=1,
                    help="Search for duplicates in source(s)")
parser.add_argument("--source-d-t", dest="source_dedup_tolerance", type=int, default=1,
                    help="Allow 3sec difference for --source-d")
parser.add_argument("--history-d", dest="history_dedup", type=int, default=1,
                    help="Search for duplicates in history-file.")
parser.add_argument("--history-p", dest="history_path", default="./pmc_history.json",
                    help="Path of history-file.")
parser.add_argument("--history-h", dest="history_hash", type=int, default=0,
                    help="Use hashes for history-check.")
parser.add_argument("--history-w", dest="history_write", type=int, default=1,
                    help="0 = don't write, 1 = append, -1 = overwrite.")
parser.add_argument("--target-d", dest="target_dedup", type=int, default=0,
                    help="Check for duplicates in target-folder.")
parser.add_argument("--target-owp", dest="target_protect", type=int, default=1,
                    help="Overwrite-protection.")
parser.add_argument("--naming-sd", dest="naming_subdir", default="%y4%-%M%-%d%_%h%-%m%-%s%",
                    help="Naming scheme for subdirs")
parser.add_argument("--naming-f", dest="naming_file", default="%n",
                    help="Naming scheme for files")
parser.add_argument("--verify", dest="verify", type=int, default=1,
                    help="Verify files via checksum")
parser.add_argument("--verify-h", dest="verify_hash", default="MD5",
                    help="Hash for verification")
parser.add_argument("--target-c", dest="target_compress", type=int, default=0,
                    help="Compress files for target # >1")
parser.add_argument("--unsleep", dest="unsleep", type=int, default=1,
                    help="Prevent system from sleep")
parser.add_argument("--preset", dest="preset", default="default",
                    help="Preset name")
parser.add_argument("--preset-w-source", dest="save_source", type=int, default=0,
                    help="Save source path(s) to preset")
parser.add_argument("--preset-w-target", dest="save_target", type=int, default=0,
                    help="Save target path(s) to preset")
parser.add_argument("--preset-w-settings", dest="save_settings", type=int, default=0,
                    help="Save settings to preset")
parser.add_argument("--verbose", dest="verbose", type=int, default=1,
                    help="Verbose. 2 = file, 1 = console, 0 = none")

param = parser.parse_args()
print(type(param))

# DEFINITION: Set print location (none/terminal/file)
if (param.verbose == 2):
    f = open("./pmc.log", mode='a')
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

print(pmc_version, file=f)

# ==================================================================================================
# ==============================================================================
#    Actual code block:
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
    found_files = []
    #  also possible: glob
    for root, dirs, files in os.walk(os.path.normpath(where)):
        for file in files:
            if file.endswith(".txt"):
                inter_path = os.path.join(root, file)
                inter_regex = re.search(r"(\w*)(\.\w*)$", file)
                inter_stats = os.stat(inter_path)
                found_files += [{
                    'name_full': inter_path,
                    'name': file,
                    'name_base': inter_regex.group(1),
                    'name_extension': inter_regex.group(2),
                    'size': inter_stats.st_size,
                    'time': inter_stats.st_mtime,
                }]

    return found_files


# DEFINITION: Get hashes for files:
def get_hashes(what):
    md5 = hashlib.md5()
    blocksize = 128*256
    for i in what:
        with open(i["name_full"], "rb") as file:
            while True:
                buf = file.read(blocksize)
                if not buf:
                    break
                md5.update(buf)
            i["checksum"] = md5.hexdigest()

    return what


def save_json(what, where):
    with open(where, 'w') as outfile:
        json.dump(what, outfile, ensure_ascii=False)


def load_json(where):
    with open(where, 'r', encoding='utf-8') as file:
        inter = json.load(file)
    return list(inter)


def copy_files(source_files):
    if not os.path.exists("/tmp/pmc"):
        os.makedirs("/tmp/pmc")

    for i in source_files:
        shutil.copy2(i["name_full"], "/tmp/pmc")


def print_files(source_files):
    for i in source_files:
        print("\n" + str(i), end="", file=f)

    print("\n", file=f)


source_files = search_files(param.source)
source_files = get_hashes(source_files)
print_files(source_files)
history_files = load_json(param.history_path)
print_files(history_files)


for i in source_files:
    for k in history_files:
        if i["time"] == k["time"] and i["size"] == k["size"] and i["name"] == k["name"]:
            i["time"] = -9999
source_files = list(filter(lambda i: i["time"] != -9999, source_files))

print_files(source_files)

to_save = source_files
for i in to_save:
    del i["name_full"]
    del i["name_base"]
    del i["name_extension"]

# save_json(param, "./pmc_preset.json")

# save_json(to_save, "./pmc_history.json")
