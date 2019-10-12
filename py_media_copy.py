#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-3-Clause-Clear
#  from PyQt5 import QtWidget
#  from pmc_ui import Ui_MainWindow
from pmc_ver import pmc_version
#  import pmc_preset

import os
import sys
import hashlib  # hash algorithms
try:
    from crc32c import crc32  # TRYOUT: crc32c for intel
except ImportError:
    from zlib import crc32
    pass
import re  # regex
import shutil  # High-level file copy
import json  # saving/loading JSON files
import itertools
#  from collections import defaultdict
from time import sleep  # For timeouts and time output
from datetime import datetime
try:
    import colorama
except ImportError:
    print("For better readability, please install colorama: pip install colorama")
    pass
try:
    from tqdm import tqdm
except ImportError:
    print('\x1b[1;31;40m' + "Please install tqdm: " + '\x1b[1;37;40m' + "pip install tqdm" + '\x1b[0m')
import argparse  # Set variables via parameters
from pathlib import Path  # TODO: make all possible things with pathlib instead of os.path

parser = argparse.ArgumentParser()
parser.add_argument("--source", "-in",
                    dest="source",
                    default="./.testing/in",
                    help="Source path(s). Can be absolute/relative. Multiple ones like 'path1|path2'")
parser.add_argument("--target", "-out",
                    dest="target",
                    default="./.testing/out",
                    help="Target path(s). Can be absolute/relative. Multiple ones like 'path1|path2'")
parser.add_argument("--filter_preference", "-filterpref",
                    dest="filter_preference",
                    type=int,
                    default=0,
                    help="Filter preference. Works with --filter-list. \
                          0 = all (no filter); -1 = exclude listed formats; 1 = include listed formats")
parser.add_argument("--filter_list", "-filterlist",
                    dest="filter_list",
                    default='.*cr2$|.*/bla.*',
                    help="Name(s) to include/exclude. Paths are converted to forward slashes (C:\\ becomes C:/) and \
                          case-insensitive regex is used: see regular-expressions.info/refquick.html and regex101.com")
parser.add_argument("--recursive_search", "-r",
                    dest="source_recurse",
                    type=int,
                    default=0,
                    help="Search recursively (i.e. including subfolders) in source(s)")
parser.add_argument("--deduplicate_source", "-dedupin",
                    dest="dedup_source",
                    type=int,
                    default=1,
                    help="Search for duplicates in source(s)")
parser.add_argument("--deduplicate_source_tolerance", "-dedupintol",
                    dest="dedup_source_tolerance",
                    type=int,
                    default=1,
                    help="Allow 3sec difference for --deduplicate_source")
parser.add_argument("--deduplicate_history", "-deduphist",
                    dest="dedup_history",
                    type=int,
                    default=1,
                    help="Search for duplicates in history-file.")
parser.add_argument("--history_path", "-histpath",
                    dest="history_path",
                    default="./pmc_history.json",
                    help="Path of history-file. Can be relative/absolute.")
parser.add_argument("--history_writemode", "-histw",
                    dest="history_writemode",
                    type=int,
                    default=2,
                    help="0 = do not write, 1 = append, 2 = overwrite.")
parser.add_argument("--dedup_target", "-dedupout",
                    dest="dedup_target",
                    type=int,
                    default=0,
                    help="Check for duplicates in target-folder.")
parser.add_argument("--dedup_usehash", "-deduphash",
                    dest="dedup_hash",
                    type=int,
                    default=0,
                    help="Use hashes for dedup-check(s).")
parser.add_argument("--target_protect_existing", "-owp",
                    dest="target_protect",
                    type=int,
                    default=1,
                    help="Overwrite-protection for existing files in target.")
parser.add_argument("--naming_subdir", "-namesub",
                    dest="naming_subdir",
                    default="%y-%m-%d",
                    help="Name scheme for subdirs. For time and date, see strftime.org for reference. \
                          Empty string will create no subdir.")
parser.add_argument("--naming_file", "-namefile",
                    dest="naming_file",
                    default="",
                    help="Name scheme for file names. For time and date, see strftime.org for reference. \
                          Empty string will not change name.")
parser.add_argument("--verify", "-test",
                    dest="verify",
                    type=int,
                    default=1,
                    help="Verify files via checksum")
parser.add_argument("--nosleep",
                    dest="nosleep",
                    type=int,
                    default=1,
                    help="Prevent system from standby.")
parser.add_argument("--preset", "-pres",
                    dest="preset",
                    default="default",
                    help="Preset name")
parser.add_argument("--preset_save_source", "-saveinpath",
                    dest="save_source",
                    type=int,
                    default=0,
                    help="Save source path(s) to preset")
parser.add_argument("--preset_save_target", "-saveoutpath",
                    dest="save_target",
                    type=int,
                    default=0,
                    help="Save target path(s) to preset")
parser.add_argument("--preset_save_settings", "-savesettings",
                    dest="save_settings",
                    type=int,
                    default=0,
                    help="Save settings to preset")
parser.add_argument("--verbose",
                    dest="verbose",
                    type=int,
                    default=1,
                    help="Verbose. 2 = file, 1 = console, 0 = none")
param = parser.parse_args()

# DEFINITION: Set print location (none/terminal/file)
if (param.verbose == 2):
    f = Path("./pmc.log").open(mode='a+')
elif (param.verbose == 0):
    f = open(os.devnull, 'w')
    sys.stdout = f
else:
    f = sys.stdout

#  for glob:
if (sys.hexversion < 0x030500F0):
    print("Cannot run py_media-copy on versions older than 3.5 - sorry! Please update.", file=sys.stderr)
    f.close()
    sys.exit(0)

print('\x1b[1;33;40m' + pmc_version + '\x1b[0m', file=f)

# ==================================================================================================
# ==============================================================================
#    Setting functions:
# ==============================================================================
# ==================================================================================================


def print_time(what):
    global f
    print('\x1b[1;34;40m' + datetime.now().strftime('%H:%M:%S') + ' -- ' + what + '\x1b[0m', file=f)


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


""" def check_remaining_files(to_check):
    if len(to_check) < 1:
        print("No files left!", file=sys.stderr)
        f.close()
        sys.exit(0)
"""


def search_files(where):
    # DEFINITION: Search for files, get basic directories:
    global param, f
    print_time(str("Searching files in " + where))

    def calculate_targetpath(for_what):
        global param, f
        for i in for_what:
            i[5] = datetime.fromtimestamp(i[5]).strftime('%Y-%m-%d-%H:%M')
            # print(i[5], file=f)
        return for_what

    found_files = []
    """ DEFINITION:
        [0] full source path
        [1] file name
        [2] basename
        [3] extension
        [4] size
        [5] mod-date
        [6] hash
        [7] full target path(s) <-- TODO: more than one useful?
    """
    if(param.source_recurse == 1):
        recurse = '**/*.*'
    else:
        recurse = '*/*.*'
    for i in Path(where).glob(recurse):
        i = Path(i).resolve()
        if (param.filter_preference == 1 and re.search(param.filter_list, str(i.as_posix()), re.I) is not None
          or param.filter_preference == -1 and re.search(param.filter_list, str(i.as_posix()), re.I) is None
          or param.filter_preference == 0):
            i_stat = i.stat()
            found_files += [[str(i),
                             i.name,
                             i.stem,
                             i.suffix,
                             i_stat.st_size,
                             i_stat.st_mtime,
                             "XYZ",
                             "XYZ"]]

    found_files = calculate_targetpath(found_files)

    print('    ' + str(len(found_files)) + " files found.", file=f)
    return found_files


def get_hashes(what):
    # DEFINITION: Get hashes for files:
    if sys.hexversion < 0x030600F0:
        algorithm = hashlib.sha1()
        # print("Using SHA1", file=f)
    else:
        algorithm = hashlib.blake2b()
        # print("Using BLAKE2", file=f)
    blocksize = 128*256
    print_time('Getting hashes')
    for i in tqdm(what):
        if i[6] == "XYZ":
            with Path(i[0]).open("rb") as file:
                crcvalue = 0
                while True:
                    buf = file.read(blocksize)
                    if not buf:
                        break
                    algorithm.update(buf)
                    crcvalue = (crc32(buf, crcvalue) & 0xffffffff)
                # i[6] = algorithm.hexdigest()
                i[6] = crcvalue

    return what


def save_json(what, where):
    print_time(str('Saving JSON ' + where))
    try:
        Path(where).write_text(json.dumps(what, ensure_ascii=False, indent="\t",
                                          separators=(',', ':')), encoding='utf-8')
    except Exception:
        print("    Error!", file=f)


def load_json(where):
    global param
    print_time(str('Loading JSON ' + where))
    try:
        with Path(where).open('r+', encoding='utf-8') as file:
            inter = json.load(file)
        print('    ' + str(len(inter)) + " entries loaded.", file=f)
        return list(inter)
    except json.decoder.JSONDecodeError:
        print("    JSONDecodeError!", file=f)
        return set()
    except FileNotFoundError:
        print("    JSON file not found.", file=f)
        return set()


def create_subfolders(for_what):
    print_time('Create folders...')
    for i in for_what:
        if not os.path.exists(i[7]):  # TODO: Pathlib
            os.makedirs(i[7])


def copy_files(what):
    print_time('Copy files')
    for i in tqdm(what):
        try:
            shutil.copy2(i[0], os.path.join(i[7], str(i[2] + i[3])))
        except Exception:
            print('    ' + str(i[0]) + " -> " + os.path.join(i[7], str(i[2] + i[3])) + " failed!", file=f)


def print_files(source_files):
    for i in source_files:
        print("\n" + str(i), end="", file=f)

    print("\n", file=f)


def dedup_files(source, compare):
    global param
    print_time('Dedup files')
    deduped = []
    if len(compare) >= 1:
        for i in source:
            j = 0
            while True:
                """
                if ((param.dedup_hash != 1 and (tuple([i[1], i[4], i[5]]) not in compare)) or
                (param.dedup_hash == 1 and (tuple([i[1], i[4], i[5], i[6]]) not in compare))):
                    deduped.append(i)
                """
                # TODO: try https://stackoverflow.com/a/15544861
                # TODO: try https://stackoverflow.com/q/17555218
                # TODO: try https://www.peterbe.com/plog/uniqifiers-benchmark
                if i[1] == compare[j][0] and i[4] == compare[j][1] and i[5] == compare[j][2]:
                    # print(i[1] + " is a duplicate.", file=f)
                    break
                else:
                    if (j + 1) < len(compare):
                        j += 1
                    else:
                        # print(str(i[1]) + ", " + str(i[4]) + ", " + str(i[5]), file=f)
                        deduped.append(i)
                        break
    else:
        for i in source:
            if tuple([i[1], i[4], i[5]]) not in compare:
                # print(str(i[1]) + str(i[4]) + str(i[5]), file=f)
                deduped.append(i)
                """
                if param.dedup_hash == 1:
                    compare.add(tuple([i[1], i[4], i[5], i[6]]))
                else:
                """
                compare.add(tuple([i[1], i[4], i[5]]))
                # print(compare, file=f)

    print('    ' + str(len(source) - len(deduped)) + " duplicates found.", file=f)
    return deduped


def create_subdirs(source):
    """Create subdirectories per magic string"""
    global param
    if len(param.naming_subdir) == 0:
        try:
            os.makedirs(param.target)
        except FileExistsError:
            pass
    else:
        for i in source:
            try:
                os.makedirs(i[7])
            except FileExistsError:
                pass


def overwrite_protection(source):
    global param
    print_time('Prevent overwriting of files')
    if param.target_protect != 0:
        # output
        for i in source:
            k = 1
            append = ""
            while True:
                if os.path.isfile(os.path.join(i[7], str(i[2] + append + i[3]))):
                    append = "_out" + str(k)
                    k += 1
                else:
                    i[2] = i[2] + append
                    # print(i[2], file=f)
                    break
        # input
        for i in source_files:
            k = 1
            append = ""
            while True:
                if os.path.isfile(os.path.join(i[7], str(i[2] + append + i[3]))):
                    append = "_in" + str(k)
                    k += 1
                else:
                    i[2] = i[2] + append
                    # print(i[2], file=f)
                    break


# ==================================================================================================
# ==============================================================================
#    Chronology / Workflow:
# ==============================================================================
# ==================================================================================================

while True:
    # DEFINITION: search files:
    source_files = search_files(param.source)
    if len(source_files) < 1:
        break

    # DEFINITION: Dedups:
    # dedup source:
    if param.dedup_source == 1:
        # get hashes:
        if param.verify == 1:
            source_files = get_hashes(source_files)
        source_files = dedup_files(source_files, set())
        if len(source_files) < 1:
            break

    # dedup history:
    if param.dedup_history == 1:
        history_files = load_json(param.history_path)
        if len(history_files) > 0:
            # get hashes:
            if param.verify == 1:
                source_files = get_hashes(source_files)
            source_files = dedup_files(source_files, history_files)
            history_files = None
            if len(source_files) < 1:
                break

    # dedup target:
    if param.dedup_target == 1:
        target_files = search_files(param.target)
        target_files = [1], [4], [5]
        # get hashes:
        if param.verify == 1:
            source_files = get_hashes(source_files)
            target_files = get_hashes(target_files)
        source_files = dedup_files(source_files, target_files)
        target_files = None
        if len(source_files) < 1:
            break

    # DEFINITION: get rest of the hashes:
    if param.verify == 1:
        source_files = get_hashes(source_files)

    # DEFINITION: prepare paths:
    # create_subdirs(source_files)

    # DEFINITION: Copy:
    # copy_files(source_files)

    # DEFINITION: Verify:

    # DEFINITION: write history:
    if param.history_writemode > 0:
        history_files = load_json(param.history_path)
        to_save = source_files
        for i in to_save:
            del i[7]
            del i[3]
            del i[2]
            del i[0]

        if param.history_writemode == 1 and history_files is not None:
            to_save += history_files

        to_save.sort()
        to_save = list(to_save for to_save, _ in itertools.groupby(to_save))

        save_json(to_save, param.history_path)
        to_save = None

    # all done:
    break

print_time('\x1b[1;32;40mDone!')
