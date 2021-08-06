# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-3-Clause-Clear OR GPL-3.0-only
"""
    REQUIRES:   string; file (same as print)
    GIVES:      current time + the required string; printed/written to file
    Get hashes for files
"""
__author__ = "flolilo"
__license__ = "See SPDX-License-Identifier"
__contact__ = "See github.com/flolilo/pyranoid_copy"
__version__ = "1.0"  # Module version specifically!

from sys import modules
import crc32c as crc32
from colorama import Fore, Style, init, deinit
init(autoreset=True)


class get_hashes():
    def __call__(self, what):
        blocksize = 128 * 256
        try:
            with Path(what).open("rb") as file:
                crcvalue = 0
                while True:
                    buf = file.read(blocksize)
                    if not buf:
                        break
                    crcvalue = (crc32(buf, crcvalue) & 0xffffffff)
                hashstring = f'{crcvalue:x}'
        except Exception as e:
            print(Style.BRIGHT + Fore.MAGENTA + "    Cannot calculate CRC32 of " + str(what) + " -- " + str(e), file=f)
            hashstring = "XYZ"

        return hashstring


modules[__name__] = get_hashes()
