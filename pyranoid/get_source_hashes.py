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

from time import sleep
from sys import modules
import tqdm
import print_time
import get_hashes


class get_source_hashes():
    def __call__(self, what):
        # TODO: Unify hash-getting with verify_files()
        print_time("Getting hashes...")
        for i in tqdm(what, desc="Files", unit="f",
                      bar_format="    {desc}: {n_fmt}/{total_fmt} |{bar}| {elapsed}<{remaining}"):
            if i[6] == "XYZ":
                i[6] = get_hashes(i[0])
        return what


modules[__name__] = get_source_hashes()
