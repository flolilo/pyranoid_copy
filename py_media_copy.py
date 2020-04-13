#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-3-Clause-Clear OR GPL-3.0-only
from pmc_ver import pmc_version

from os import devnull, system, sync
from sys import hexversion
from sys import stdout as sys_stdout
from sys import exit as sys_exit
try:
    from crc32c import crc32  # crc32c for intel
except ImportError:
    from zlib import crc32  # standard crc32
    pass
import re  # regex
import shutil  # High-level file copy
import json  # saving/loading JSON files
import itertools
from time import sleep  # For timeouts and time output
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

parser = ArgumentParser()
parser.add_argument("--preset", "-pres",
                    dest="preset",
                    default="default",
                    help="Preset name")
parser.add_argument("--source", "-in",
                    dest="source",
                    default="--",
                    help="Source path(s). Can be absolute/relative. Multiple ones like 'path1|path2'")
parser.add_argument("--target", "-out",
                    dest="target",
                    default="--",
                    help="Target path(s). Can be absolute/relative. Multiple ones like 'path1|path2'")
parser.add_argument("--filter_preference", "-filterpref",
                    dest="filter_pref",
                    type=int,
                    default=-1,
                    help="Filter preference. Works with --filter-list. \
                          0 = all (no filter); -1 = exclude listed formats; 1 = include listed formats")
parser.add_argument("--filter_list", "-filterlist",
                    dest="filter_list",
                    default='--',
                    help="Name(s) to include/exclude. Paths are converted to forward slashes (C:\\ becomes C:/) and \
                          case-insensitive regex is used: see regular-expressions.info/refquick.html and regex101.com")
parser.add_argument("--recursive_search", "-r",
                    dest="recursive",
                    type=int,
                    default=-1,
                    help="Search recursively (i.e. including subfolders) in source(s)")
parser.add_argument("--deduplicate_source", "-dedupin",
                    dest="dedup_source",
                    type=int,
                    default=-1,
                    help="Search for duplicates in source(s)")
parser.add_argument("--deduplicate_source_tolerance", "-dedupintol",
                    dest="dedup_source_tolerance",
                    type=int,
                    default=-1,
                    help="Allow 3sec difference for --deduplicate_source")
parser.add_argument("--deduplicate_history", "-deduphist",
                    dest="dedup_history",
                    type=int,
                    default=-1,
                    help="Search for duplicates in history-file.")
parser.add_argument("--history_path", "-histpath",
                    dest="history_path",
                    default="--",
                    help="Path of history-file. Can be relative/absolute. For --history_writemode=3: 'in|out'")
parser.add_argument("--history_writemode", "-histw",
                    dest="history_writemode",
                    type=int,
                    default=-1,
                    help="0 = do not write, 1 = append, 2 = overwrite, 3 = new file/overwrite existing 2nd file.")
parser.add_argument("--dedup_target", "-dedupout",
                    dest="dedup_target",
                    type=int,
                    default=-1,
                    help="Check for duplicates in target-folder.")
parser.add_argument("--dedup_usehash", "-deduphash",
                    dest="dedup_hash",
                    type=int,
                    default=-1,
                    help="Use hashes for dedup-check(s).")
parser.add_argument("--target_protect_existing", "-owp",
                    dest="target_protect",
                    type=int,
                    default=-1,
                    help="Overwrite-protection for existing files in target.")
parser.add_argument("--naming_subdir", "-namesub",
                    dest="naming_subdir",
                    default="--",
                    help="Name scheme for subdirs. For time and date, see strftime.org for reference. \
                          Empty string will create no subdir.%fbn = file basename, %ffn = file full name, \
                          %fe = file extension")
parser.add_argument("--naming_file", "-namefile",
                    dest="naming_file",
                    default="--",
                    help="Name scheme for file names. For time and date, see strftime.org for reference. \
                          Empty string will not change name. %fbn = file basename, %ffn = file full name, \
                          %fe = file extension, %ct# = counter (! sorting (which counting bases on) is \
                          based on the full source path of the file ! # is padding number (e.g. %ct3 = 001)")
parser.add_argument("--verify", "-test",
                    dest="verify",
                    type=int,
                    default=-1,
                    help="Verify files via checksum")
parser.add_argument("--nosleep",
                    dest="nosleep",
                    type=int,
                    default=-1,
                    help="Prevent system from standby.")
parser.add_argument("--preset_save_source", "-saveinpath",
                    dest="save_source",
                    type=int,
                    default=-1,
                    help="Save source path(s) to preset")
parser.add_argument("--preset_save_target", "-saveoutpath",
                    dest="save_target",
                    type=int,
                    default=-1,
                    help="Save target path(s) to preset")
parser.add_argument("--preset_save_settings", "-savesettings",
                    dest="save_settings",
                    type=int,
                    default=-1,
                    help="Save settings to preset")
parser.add_argument("--verbose",  # TODO: make verbose also for small prints like "using hash xyz" with more values?
                    dest="verbose",
                    type=int,
                    default=-1,
                    help="Verbose. 2 = file, 1 = console, 0 = none")
param = vars(parser.parse_args())  # convert namespace to dictionary

# DEF: Set print location (none/terminal/file)
if (param['verbose'] == 2):
    f = Path("./pmc.log").resolve().open(mode='a+', encoding='utf-8')
elif (param['verbose'] == 0):
    f = open(devnull, 'w')
    sys_stdout = f
else:
    f = sys_stdout

#  for glob, we need Python >= v3.5:
if (hexversion < 0x030500F0):
    f.close()
    deinit()
    sys_exit("Cannot run py_media-copy on python < v3.5! Please update.")


# ==================================================================================================
# ==============================================================================
#    Setting functions:
# ==============================================================================
# ==================================================================================================

def print_time(what):
    global f
    print(Style.BRIGHT + Fore.BLUE + datetime.now().strftime('%H:%M:%S') + ' -- ' + what, file=f)


def check_remaining_files(to_check):
    global f
    if len(to_check) < 1:
        print("No files left!", file=f)
        return 0
    else:
        return 1


def read_presets(preset_file=str(Path("./pmc_presets.json").resolve())):
    """Read parameters for all params that were not set by user."""
    global param, f  # TODO: mayble delete global
    # (https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python)
    try:
        with Path(preset_file).open('r+', encoding='utf-8') as file:
            presets_from_file = json.load(file)
    except Exception:
        print("Preset-file could not be loaded!", file=f)

    return presets_from_file


def merge_params():
    presets_from_file = read_presets()
    preset_specified = dict()
    for i in presets_from_file:
        if str(i['preset']) == str(param['preset']):
            preset_specified = i
            break
    if len(preset_specified) == 0:
        print(Style.BRIGHT + Fore.MAGENTA + "Preset not found!", file=f)

    for key, value in param.items():
        if str(param[key]) == "-1" and key in preset_specified:
            param[key] = preset_specified[key]


def check_params():
    """check all parameters"""
    global param, f  # TODO: mayble delete global
    # (https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python)

    def print_error(what):
        global f
        print(Style.BRIGHT + Fore.RED + "    " + what, file=f)
        f.close()
        deinit()
        sleep(1)
        sys_exit(what)

    # --source:
    try:
        if type(param['source']) == str:
        param['source'] = [str(Path(i).resolve()) for i in re.split('\|', param['source']) if len(i) > 0]
        elif type(param['source']) == list:
            for i in param['source']:
                param['source'] = [str(Path(i).resolve()) for i in param['source'] if len(i) > 0]
        else:
            raise Exception('--source is neither list nor string!')
    except Exception:
        print_error("Error in --source!")
    if (len(param['source']) < 1):
        print_error("No source path(s) actually found!")

    # --target:
    try:
        if type(param['target']) == str:
        param['target'] = [str(Path(i).resolve()) for i in re.split('\|', param['target']) if len(i) > 0]
        elif type(param['target']) == list:
            for i in param['target']:
                param['target'] = [str(Path(i).resolve()) for i in param['target'] if len(i) > 0]
        else:
            raise Exception('--target is neither list nor string!')
    except Exception:
        print_error("Error in --target!")
    if (len(param['target']) < 1):
        print_error("No target path(s) actually found!")

    # --filter_preference & --filter_list:
    if (not -1 <= param['filter_pref'] <= 1):
        print_error("No valid int for --filter_preference!")
    elif (param['filter_pref'] != 0 and len(param['filter_list']) < 1):
        print_error("--filter_list is empty!")

    # --recursive_search:
    if (not 0 <= param['recursive'] <= 1):
        print_error("No valid int for --recursive_search!")

    # --deduplicate_source & --deduplicate_source_tolerance:
    if (not 0 <= param['dedup_source'] <= 1):
        print_error("No valid int for --deduplicate_source!")
    elif(param['dedup_source'] == 1 and not 0 <= param['dedup_source_tolerance'] <= 1):
        print_error("No valid int for --deduplicate_source_tolerance!")

    # TODO: --deduplicate_history & --history_path & --history_writemode:
    if(not 0 <= param['dedup_history'] <= 1):
        print_error("No valid int for --deduplicate_history!")
    if(not 0 <= param['history_writemode'] <= 3):
        print_error("No valid int for --history_writemode!")
    if(param['dedup_history'] == 1 or param['history_writemode'] > 0):
        param['history_path'] = [str(Path(i).resolve()) for i in re.split('\|', param['history_path'])]
        if(len(param['history_path']) > 0):
            if(param['history_writemode'] <= 2):
                param['history_path'] = param['history_path'][0]
            else:
                if(len(param['history_path']) > 1):
                    param['history_path'] = [param['history_path'][0], param['history_path'][1]]
                else:
                    print_error("Not enough paths for --history_writemode 3!")
        else:
            print_error("No history-path!")
    else:
        print_error("TODO:")

    # --dedup_target:
    if (not 0 <= param['dedup_target'] <= 1):
        print_error("No valid int for --dedup_target!")

    # --dedup_usehash
    if (not 0 <= param['dedup_hash'] <= 1):
        print_error("No valid int for --dedup_usehash!")

    # --target_protect_existing
    if (not 0 <= param['target_protect'] <= 1):
        print_error("No valid int for --target_protect_existing!")

    # TODO: --naming_subdir:

    # TODO: --naming_file:

    # --verify:
    if (not 0 <= param['verify'] <= 1):
        print_error("No valid int for --verify!")

    # --nosleep:
    if (not 0 <= param['nosleep'] <= 1):
        print_error("No valid int for --nosleep!")

    # --preset:
    if (len(param['preset']) < 1):
        print_error("No valid string for --preset!")

    # --preset_save_source:
    if (not 0 <= param['save_source'] <= 1):
        print_error("No valid int for --preset_save_source!")

    # --preset_save_target:
    if (not 0 <= param['save_target'] <= 1):
        print_error("No valid int for --preset_save_target!")

    # --preset_save_settings:
    if (not 0 <= param['save_settings'] <= 1):
        print_error("No valid int for --preset_save_settings!")

    # --verbose:
    if (not 0 <= param['verbose'] <= 2):
        print_error("No valid int for --verbose!")


def save_params(preset_file=str(Path("./pmc_presets.json").resolve())):
    """Save parameters in file."""
    global param  # TODO: mayble delete global
    # (https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python)
    params_to_save = param.copy()
    del params_to_save['save_settings']
    if params_to_save['save_source'] < 1:
        del params_to_save['source']
    del params_to_save['save_source']
    if params_to_save['save_target'] < 1:
        del params_to_save['target']
    del params_to_save['save_target']

    presets_from_file = read_presets()
    # TODO: leave non-i untouched, change i with params, then save non-i and i
    x = 0
    for i in presets_from_file:
        if str(i['preset']) == str(param['preset']):
            for key, value in i.items():
                if str(param[key]) != "-1":
                    i[key] = param[key]
                x = 1
            break
    if x == 0:
        all_presets = presets_from_file + [params_to_save]
    else:
        all_presets = presets_from_file

    # CREDIT: https://stackoverflow.com/a/9428041/8013879
    to_save = [i for n, i in enumerate(all_presets) if i not in all_presets[n + 1:]]

    save_json(to_save, Path(preset_file).resolve())


def search_files(where):
    """Search for files, get basic attributes"""
    global param, f
    print_time("Searching files...")

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
    if(param['recursive'] == 1):
        recurse = '**/*.*'
    else:
        recurse = '*/*.*'

    for i in tqdm(where, desc="Paths", unit="Paths",
                  bar_format="    {desc}: {n_fmt}/{total_fmt} |{bar}| {elapsed}<{remaining}"):
        for j in Path(i).glob(recurse):
            j = Path(j).resolve()
            if (param['filter_pref'] == 1 and re.search(param['filter_list'], str(j.as_posix()), re.I) is not None
              or param['filter_pref'] == -1 and re.search(param['filter_list'], str(j.as_posix()), re.I) is None
              or param['filter_pref'] == 0):
                j_stat = j.stat()
                found_files += [[str(j),
                                j.name,
                                j.stem,
                                j.suffix,
                                j_stat.st_size,
                                j_stat.st_mtime,
                                "XYZ",
                                []]]

    print('    ' + str(len(found_files)) + " files found.", file=f)
    found_files = sorted(found_files, key=lambda attris: attris[0])  # For %c in param['naming_file'].
    return found_files


def get_source_hashes(what):
    """Get hashes for files"""
    # TODO: Unify hash-getting with verify_files()
    print_time("Getting hashes...")
    for i in tqdm(what, desc="Files", unit="f",
                  bar_format="    {desc}: {n_fmt}/{total_fmt} |{bar}| {elapsed}<{remaining}"):
        if i[6] == "XYZ":
            i[6] = get_hashes(i[0])
    return what


def get_hashes(what):
    blocksize = 128*256
            try:
        with Path(what).open("rb") as file:
                    crcvalue = 0
                    while True:
                        buf = file.read(blocksize)
                        if not buf:
                            break
                        crcvalue = (crc32(buf, crcvalue) & 0xffffffff)
            hashstring = f'{crcvalue:x}'
            except Exception:
        print(Style.BRIGHT + Fore.MAGENTA + "    Cannot calculate CRC32 of " + str(what), file=f)
        hashstring = "XYZ"

    return hashstring


def dedup_files(source, compare, what_string):
    global param, f
    print_time("Dedup " + what_string + " files...")
    deduped = []
    if (len(compare) > 0):
        for i in tqdm(source, desc="Files", unit="f",
                      bar_format="    {desc}: {n_fmt}/{total_fmt} |{bar}| {elapsed}<{remaining}"):
            j = 0
            while True:
                """
                    if ((param['dedup_hash'] != 1 and (tuple([i[1], i[4], i[5]]) not in compare)) or
                    (param['dedup_hash'] == 1 and (tuple([i[1], i[4], i[5], i[6]]) not in compare))):
                        deduped.append(i)
                """
                # TODO: try https://stackoverflow.com/a/15544861
                # TODO: try https://stackoverflow.com/q/17555218
                # TODO: try https://www.peterbe.com/plog/uniqifiers-benchmark
                if (i[1] == compare[j][0] and i[4] == compare[j][1] and i[5] == compare[j][2]):
                    # print(i[1] + " is a duplicate.", file=f)
                    break
                else:
                    if ((j + 1) < len(compare)):
                        j += 1
                    else:
                        # print(str(i[1]) + ", " + str(i[4]) + ", " + str(i[5]), file=f)
                        deduped.append(i)
                        break
    else:
        for i in tqdm(source, desc="Files", unit="f",
                      bar_format="    {desc}: {n_fmt}/{total_fmt} |{bar}| {elapsed}<{remaining}"):
            if (tuple([i[1], i[4], i[5]]) not in compare):
                # print(str(i[1]) + str(i[4]) + str(i[5]), file=f)
                deduped.append(i)
                """
                    if param['dedup_hash'] == 1:
                        compare.add(tuple([i[1], i[4], i[5], i[6]]))
                    else:
                """
                compare.add(tuple([i[1], i[4], i[5]]))
                # print(compare, file=f)

    print('    ' + str(len(source) - len(deduped)) + " duplicates found.", file=f)
    return deduped


def calculate_targetpath(source):
    # i[1] = i[2]+i[3]      %fbn|%fe|%ffn
    """check if target path(s) are already existing (i.e. a file with this name already exists)"""
    global param
    if param['target_protect'] > 0:
        expl = 'Calculate target paths (prevent overwriting)'
    else:
        expl = 'Calculate target paths (do not prevent overwriting)'
    print_time(expl)

    counter = 1
    already_used_names = []
    for i in source:
        for j in param['target']:
            # BaseName (pre-OWP):
            if len(param['naming_file']) > 0:
                inter_base = param['naming_file']
                inter_base = re.sub(r'%ffn', i[1], inter_base, re.I)
                inter_base = re.sub(r'%fbn', i[2], inter_base, re.I)
                inter_base = re.sub(r'%fe', i[3], inter_base, re.I)
                counter_list = re.split(r'%ct(\d)', inter_base)
                inter_counter = ""
                for k in counter_list:
                    if re.match(r'^\d{1}$', k, re.MULTILINE):
                        inter_counter += str(counter).zfill(int(k))
                    else:
                        inter_counter += k
                inter_base = inter_counter
                inter_base = datetime.fromtimestamp(i[5]).strftime(inter_base)
            else:
                inter_base = i[2]
            # Subfolder:
            if len(param['naming_subdir']) > 0:
                inter_sub = param['naming_subdir']
                inter_sub = re.sub(r'%ffn', i[1], inter_sub, re.I)
                inter_sub = re.sub(r'%fbn', i[2], inter_sub, re.I)
                inter_sub = re.sub(r'%fe', i[3], inter_sub, re.I)
                inter_sub = datetime.fromtimestamp(i[5]).strftime(inter_sub)
            else:
                inter_sub = ""
            inter_sub += "/"
            # Test for output already existing:
            if param['target_protect'] > 0:
                k_out = 1
                k_in = 1
                inter_test = Path(j).joinpath(inter_sub + inter_base).resolve()
                while True:
                    if Path(inter_test).joinpath(i[3]).resolve().is_file():  # if file alread exists...
                        inter_test = Path(j).joinpath(inter_sub + inter_base + "_out" + str(k_out)).resolve()
                        k_out += 1
                    else:  # if file does not exist with that name...
                        inter_test_in = inter_test
                        while True:  # if file with this name already will be copied...
                            if (str(Path(inter_test_in).resolve()) + i[3]) in already_used_names:
                                inter_test_in = str(Path(inter_test).resolve()) + "_in" + str(k_in)
                                k_in += 1
                            else:
                                i[7] = [str(Path(inter_test_in).resolve()) + i[3]] + i[7]
                                already_used_names = [str(Path(inter_test_in).resolve()) + i[3]] + already_used_names
                                break
                        break
            else:  # No OWP:
                i[7] = [str(Path(j).joinpath(inter_sub + inter_base + i[3]).resolve())] + i[7]
        counter += 1

    return source


def verify_files(what):
    # TODO: Unify hash-getting with get_hashes()
    errors = 0
    print_time("Verifying hashes...")
    for i in tqdm(what, desc="Files", unit="f",
                  bar_format="    {desc}: {n_fmt}/{total_fmt} |{bar}| {elapsed}<{remaining}"):
        for j in range(len(i[7])):
            target_hash = get_hashes(i[7][j])
            if i[6] != target_hash:
                errors += 1
            else:
                i[7].pop(j)

    print("    " + str(errors) + " files not properly copied")

    return what


def save_json(what, where):
    print_time(str('Saving JSON ' + str(where)))
    try:
        Path(where).write_text(json.dumps(what, ensure_ascii=False, indent="\t",
                                          separators=(',', ':')), encoding='utf-8')
    except Exception:
        print(Style.BRIGHT + Fore.MAGENTA + "    Error!", file=f)


def load_json(where):
    global param, f
    print_time('Loading JSON ' + str(where))
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


def copy_files(what):
    print_time('Copy files')
    for i in tqdm(what, desc="Files", unit="f",
                  bar_format="    {desc}: {n_fmt}/{total_fmt} |{bar}| {elapsed}<{remaining}"):
        for j in i[7]:
            try:
                shutil.copy2(i[0], Path(j).resolve())
            except Exception:
                print('    ' + str(i[0]) + " -> " + str(Path(j).joinpath(str(i[2] + i[3])).resolve()) +
                      " failed!", file=f)


def create_subdirs(source):
    """Create subdirectories per magic string"""
    print_time("Create subdirectories")
    for i in source:
        for j in i[7]:
            try:
                Path(j).resolve().parent.mkdir(parents=True, exist_ok=True)
            except Exception:
                print(Fore.RED + "    " + "Could not create folder " + str(Path(j).parents[0].resolve()), file=f)


def save_history(what):
    history_files = load_json(param['history_path'])
    for i in what:
        del i[7]
        del i[3]
        del i[2]
        del i[0]

    if param['history_writemode'] == 1 and history_files is not None:
        what += history_files

    what.sort()
    what = list(what for what, _ in itertools.groupby(what))

    save_json(what, param['history_path'])


# ==================================================================================================
# ==============================================================================
#    Chronology / Workflow:
# ==============================================================================
# ==================================================================================================

print(Style.BRIGHT + Fore.YELLOW + pmc_version, file=f)
while True:
    merge_params()
    check_params()
    if param['save_settings'] == 1:
        save_params()

    # DEF: search files:
    source_files = search_files(param['source'])
    if(check_remaining_files(source_files) == 0):
        break

    # DEF: Dedups:
    # dedup source:
    if param['dedup_source'] == 1:
        # get hashes:
        if param['dedup_hash'] == 1:
            source_files = get_source_hashes(source_files)
        source_files = dedup_files(source_files, set(), "source")
        if(check_remaining_files(source_files) == 0):
            break
    # dedup history:
    if param['dedup_history'] == 1:
        history_files = load_json(param['history_path'])
        if len(history_files) > 0:
            # get hashes:
            if param['dedup_hash'] == 1:
                source_files = get_source_hashes(source_files)
            source_files = dedup_files(source_files, history_files, "history")
            history_files = None
            if(check_remaining_files(source_files) == 0):
                break
    # dedup target:
    if param['dedup_target'] == 1:
        target_files = search_files(param['target'])
        target_files = [1], [4], [5]
        # get hashes:
        if param['dedup_hash'] == 1:
            source_files = get_source_hashes(source_files)
            target_files = get_source_hashes(target_files)
        source_files = dedup_files(source_files, target_files)
        target_files = None
        if(check_remaining_files(source_files) == 0):
            break

    # DEF: get rest of the hashes:
    if param['verify'] == 1:
        source_files = get_source_hashes(source_files)

    # DEF: prepare paths:
    source_files = calculate_targetpath(source_files)
    create_subdirs(source_files)

    # DEF: Looping copying and verifying until all files are properly copied
    while True:
    # DEF: Copy:
    copy_files(source_files)

    # DEF: Flush write cache
    if system == "posix":
        print_time("Flushing disk write cache...")
        try:
            sync()
        except Exception:
            print(Style.BRIGHT + Fore.MAGENTA + "    " +
                  "Error occured during os.sync(). This should not be too troubling...", file=f)
            sleep(5)
    elif system == "Windows":
        # TODO: powershell Write-VolumeCache -DriveLetter
        # "$($(Split-Path -Path $UserParams.OutputPath -Qualifier).Replace(":",''))" -ErrorAction Stop
        print_time("Flushing disk write cache is not yet implemented for your system")
        sleep(5)
    else:
        print_time("Flushing disk write cache is not implemented for your system")
        sleep(5)

    # DEF: Verify:
        if param['verify'] == 1:
    source_files = verify_files(source_files)
    source_files = [i for n, i in enumerate(source_files) if len(i[7]) >= 1]
            if len(source_files) == 0:
                break
            elif input(str(len(source_files)) + " could not be verified. Try again? y/n\t") not in ["yes", "y", "1"]:
                break
        else:
            break

    # DEF: write history:
    if param['history_writemode'] > 0:
        save_history(source_files)

    # all done:
    break

print_time(Style.BRIGHT + Fore.GREEN + "Done!")
print(Style.RESET_ALL + Fore.RESET, file=f)
deinit()
f.close()
sys_exit(0)
