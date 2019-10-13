# py_media-copy
A lightweight alternative to tools like Rapid Photo Downloader

This should become an alternative to Rapid Photo Downloader, mainly orientated on my media-copytool.

This means highly granular controls and a focus on copying only.

## Features:
 - Small ~~Qt5 GUI~~ [PySimpleGUIWeb (Remi)](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb) for the parameters,
 - Standalone planned / as little extra dependencies as feasible with decent usability (planned at the moment: [tqdm](https://github.com/tqdm/tqdm) required, [colorama](https://github.com/tartley/colorama) recommended, [crc32c](https://github.com/ICRAR/crc32c) if desired) for "source" installation
 - (Smart) renaming options for files and subfolders: Strftime magic strings
 - Redundancy checks against history file / target-folder / multiple inputs
 - **Checksum-/hash-based verification of copied file**
 - Include/exclude by regex pattern(s)

## Milestones:
See the TODO file.
