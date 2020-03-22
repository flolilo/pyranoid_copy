# -*- coding: utf-8 -*-
from pathlib import Path


# CREDIT: https://stackoverflow.com/a/56245722/8013879
def get_git_revision(base_path):
    git_dir = Path(base_path) / '.git'
    with (git_dir / 'HEAD').open('r') as head:
        ref = head.readline().split(' ')[-1].strip()

    with (git_dir / ref).open('r') as git_hash:
        return git_hash.readline().strip()[:7]


try:
    git_ver = get_git_revision("./")
except Exception:
    git_ver = "N/A"

pmc_version = "py_media-copy v0.0.3" + " (git: " + str(git_ver) + ")"
