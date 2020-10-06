#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import devnull, system, sync
import timeit
from crc32c import crc32c # crc32c for intel
from zlib import crc32  # standard crc32
import xxhash
import re  # regex
import itertools
from time import sleep, mktime  # For timeouts and time output
from datetime import datetime
from pathlib import Path

# ##################################################################################################
# ##############################################################################
#    Setting functions:
# ##############################################################################
# ##################################################################################################


def search_files(where):
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
    found_files = []
    recurse = '**/*'

    for i in where:
        for j in Path(i).glob(recurse):
            if j.is_file():
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
    # print(len(found_files))
    return found_files


def get_source_hashes_CRC32C(what):
    blocksize = 128*256
    for i in what:
        with Path(i[0]).open("rb") as file:
            crcvalue = 0
            while True:
                buf = file.read(blocksize)
                if not buf:
                    break
                crcvalue = (crc32c(buf, crcvalue) & 0xffffffff)
            hashstring = f'{crcvalue:x}'
        i[6] = hashstring
    # return what


def get_source_hashes_CRC32(what):
    blocksize = 128*256
    for i in what:
        with Path(i[0]).open("rb") as file:
            crcvalue = 0
            while True:
                buf = file.read(blocksize)
                if not buf:
                    break
                crcvalue = (crc32(buf, crcvalue) & 0xffffffff)
            hashstring = f'{crcvalue:x}'
        i[6] = hashstring
    # return what


def get_source_hashes_xxhash_256(what):
    blocksize = 128*256
    xxh = xxhash.xxh3_64()
    for i in what:
        xxh.reset()
        with Path(i[0]).open("rb") as file:
            while True:
                buf = file.read(blocksize)
                if not buf:
                    break
                xxh.update(buf)
        crcvalue = xxh.hexdigest()
        i[6] = crcvalue
    # return what


def get_source_hashes_xxhash_4096(what):
    blocksize = 1024*4096
    xxh = xxhash.xxh3_64()
    for i in what:
        xxh.reset()
        with Path(i[0]).open("rb") as file:
            while True:
                buf = file.read(blocksize)
                if not buf:
                    break
                xxh.update(buf)
        crcvalue = xxh.hexdigest()
        i[6] = crcvalue
    # return what


# ##################################################################################################
# ##############################################################################
#    Chronology / Workflow:
# ##############################################################################
# ##################################################################################################

source_files = search_files(["/tmp/py_media-copy/.testing/in/"])
print("Files:\t" + str(len(source_files)))
sleep(5)


time_crc32c = timeit.timeit('get_source_hashes_CRC32C(source_files)', 'from __main__ import source_files, get_source_hashes_CRC32C', number=1)
print("CRC32C:\t" + str(time_crc32c))
sleep(5)

time_crc32 = timeit.timeit('get_source_hashes_CRC32(source_files)', 'from __main__ import source_files, get_source_hashes_CRC32', number=1)
print("CRC32:\t" + str(time_crc32))
sleep(5)

time_xxhash256 = timeit.timeit('get_source_hashes_xxhash_256(source_files)', 'from __main__ import source_files, get_source_hashes_xxhash_256', number=1)
print("xxHash (256):\t" + str(time_xxhash256))
sleep(5)

time_xxhash4096 = timeit.timeit('get_source_hashes_xxhash_4096(source_files)', 'from __main__ import source_files, get_source_hashes_xxhash_4096', number=1)
print("xxHash (4096):\t" + str(time_xxhash4096))
sleep(5)
