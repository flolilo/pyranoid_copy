# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-3-Clause-Clear OR GPL-3.0-only
"""
    REQUIRES:   string; file (same as print)
    GIVES:      current time + the required string; printed/written to file
"""
__author__ = "flolilo"
__license__ = "See SPDX-License-Identifier"
__contact__ = "See github.com/flolilo/pyranoid_copy"
__version__ = "1.0"  # Module version specifically!

from time import sleep
from datetime import datetime
from sys import modules
try:
    from colorama import Fore, Style, init, deinit
    init(autoreset=True)
except ImportError:
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


class print_time():
    def __call__(self, what, where):
        print(Style.BRIGHT + Fore.BLUE + datetime.now().strftime('%H:%M:%S') + ' -- ' + what, file=where)


modules[__name__] = print_time()
