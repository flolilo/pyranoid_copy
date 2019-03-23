#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from pmc_ui import Ui_MainWindow
from pmc_ver import pmc_version
import hashlib
import re
#  import pmc_preset

import os
import sys
"""
    from time import localtime, sleep  # For timeouts and time output
    import argparse  # Set variables via parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", dest="source", help="Source path(s). Multiple ones like 'path1$path2'", default="")
    parser.add_argument("--target", dest="target", help="Target path(s). Multiple ones like 'path1$path2'", default="")
    parser.add_argument("--ext-pref", dest="extension_preference", help="0 = all; -1 = exclude; 1 = include", type=int, default=0)
    parser.add_argument("--ext-list", dest="extension_list", help="Extensions to in-/exclude. Use like 'ext1$ext2'", default="")
    parser.add_argument("--source-r", dest="source_recurse", help="Search recursively (i.e. including subfolders) in source(s)", type=int, default=1)
    parser.add_argument("--source-d", dest="source_dedup", help="Search for duplicates in source(s)", type=int, default=0)
    parser.add_argument("--source-d-t", dest="source_dedup_tolerance", help="Allow 3sec difference for --source-d", type=int, default=1)
    parser.add_argument("--history-d", dest="history_dedup", help="Polling interval (in seconds).", type=int, default=10)
    parser.add_argument("--history-p", dest="history_path", help="Polling interval (in seconds).", type=int, default=10)
    parser.add_argument("--history-h", dest="history_hash", help="Polling interval (in seconds).", type=int, default=10)
    parser.add_argument("--history-w", dest="history_write", help="Polling interval (in seconds).", type=int, default=10)
    parser.add_argument("--target-d", dest="target_dedup", help="Polling interval (in seconds).", type=int, default=10)
    parser.add_argument("--target-owp", dest="target_protect", help="Polling interval (in seconds).", type=int, default=10)
    parser.add_argument("--naming-sd", dest="naming_subfolder", help="Naming scheme for subfolders", type=int, default=10)
    parser.add_argument("--naming-f", dest="naming_file", help="Naming scheme for files", type=int, default=10)
    parser.add_argument("--verify", dest="verify", help="Verify files via checksum", type=int, default=1)
    parser.add_argument("--verify-h", dest="verify_hash", help="Hash for verification", default="MD5")
    parser.add_argument("--target-c", dest="target_compress", help="Compress files for target # >1", type=int, default=0)
    parser.add_argument("--unsleep", dest="unsleep", help="Prevent system from sleep", type=int, default=1)
    parser.add_argument("--preset", dest="preset", help="Preset name", default="default")
    parser.add_argument("--preset-w-source", dest="save_source", help="Save source path(s) to preset", type=int, default=0)
    parser.add_argument("--preset-w-target", dest="save_target", help="Save target path(s) to preset", type=int, default=0)
    parser.add_argument("--preset-w-settings", dest="save_settings", help="Save settings to preset", type=int, default=0)
    parser.add_argument("--verbose", dest="verbose", help="Verbose. 2 = file, 1 = console, 0 = none", type=int, default=1)

    args = parser.parse_args()


    # DEFINITION: Set print location (none/terminal/file)
    if (args.verbose == 2):
        f = open("./pmc.log", mode='a')
    elif (args.Log == 1):
        f = sys.stdout
    else:
        f = open(os.devnull, 'w')
        sys.stdout = f
"""

f = sys.stdout

#  for glob:
if sys.hexversion < 0x030500F0:
    print("Cannot run py_media-copy on versions older than 3.5 - sorry!", file=sys.stderr)
    f.close()
    sys.exit(0)

# ==================================================================================================
# ==============================================================================
#    Actual code block:
# ==============================================================================
# ==================================================================================================

print(pmc_version, file=f)
testvar = "meine testvariable /home/bla"

""" GUI:
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

source_files = []
#  also possible: glob
for root, dirs, files in os.walk(os.path.normpath("/home/flo/Downloads")):
    for file in files:
        if file.endswith(".txt"):
            inter_path = os.path.join(root, file)
            inter_regex = re.search(r"(\w*)(\.\w*)$", inter_path)
            inter_basename = inter_regex.group(1)
            inter_extension = inter_regex.group(2)
            inter_stats = os.stat(inter_path)
            inter_checksum = ""
            source_files += [{'name_full': inter_path, 'name_base': inter_basename, 'name_extension': inter_extension,
                              'size': inter_stats.st_size, 'time': inter_stats.st_mtime, 'checksum': inter_checksum}]


md5 = hashlib.md5()
blocksize = 128*256
for i in source_files:
    with open(i["name_full"], "rb") as file:
        while True:
            buf = file.read(blocksize)
            if not buf:
                break
            md5.update(buf)

        i["checksum"] = md5.hexdigest()

for i in source_files:
    print("\n" + i["name_full"], end="\t|  ", file=f)
    print(i["name_base"], end="\t|  ", file=f)
    print(i["name_extension"], end="\t|  ", file=f)
    print(str(i["size"]), end="\t|  ", file=f)
    print(str(i["time"]), end="\t|  ", file=f)
    print(i["checksum"], end="", file=f)

print("", file=f)
