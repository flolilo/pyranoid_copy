=============
py_media-copy
=============

A lightweight alternative to tools like Rapid Photo Downloader

This tool is mainly orientated on my `media-copytool <https://github.com/flolilo/media-copytool>`_, which I created
because none of the existing Digital Asset Management (DAM) programs (to my knowledge) offered the options for
importing fiels from media cards that I wanted (see `Features`_). The goal is to provide a faster implementation with
at least feature parity to media-copytool. Note that the goal is not to recreate the code, but the features.

**Note that as of now, this tool is not even finished in a rough state - I am still in the progress of writing the main
features and testing them.**

.. contents:: Index:


Features
--------

- Will work on all (desktop) OSs that are supported by `Python ≥ 3.5 <https://www.python.org/downloads/>`_,
- Optimised for copying large quantities of mission critical files, e.g. wedding photos:
- Lightweight,
- Standalone binaries (i.e. ``py_media_copy.exe``) available,
- Highly granular controls:
    - Use one or multiple source and/or target path(s),
    - Rename files while copying them (magic strings available!),
    - Create subfolders (magic strings available!),
    - Filter files to copy -- inclusion & exclusion possible,
- Option to avoid overwriting existing files by searching iterations of the name that are not yet used,
- Option to avoid duplicates based on:
    - a history file (user specified `JSON file <https://en.wikipedia.org/wiki/JSON#Example>`_),
    - duplicate files in the input folder(s),
    - duplicate files in the target path,
- Option to prevent the device from going to sleep (likely by using a built-in version of
  `espresso-python <https://github.com/piedar/espresso-python>`_),
- Proper documentation *(or so I hope ;-) )*


Details
-------

- Small `PySimpleGUIWeb (Remi) <https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb>`_
  for the parameters,
- Standalone planned / as little extra dependencies as feasible (and all on `pip <https://pypi.org/>`_) with decent
  usability (planned at the moment: `tqdm <https://github.com/tqdm/tqdm>`_ required,
  `colorama <https://github.com/tartley/colorama>`_ recommended, `crc32c <https://github.com/ICRAR/crc32c>`_ if
  desired) for "source" installation (i.e. not using the binaries, but the script file itself),
- (Smart) renaming options for files and subfolders:
  `Strftime magic strings <https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior>`_ (e.g.
  ``%Y-%m-%d`` for ``2019-11-31``),
- Redundancy checks against history file / target-folder / multiple inputs,
- Checking CRC32 of every file after clearing the disk cache, thus reducing the risk of a bad copy,
- Include/exclude by regex pattern(s) (e.g. ``.*\.jpg`` - see `my regex101.com example <https://regex101.com/r/0WHdUL/2>`_
  for what this does).


Installation
------------

**This will probably change once this repo is in a working state. At the moment:**

.. code-block:: Shell

    # get the repository:
    git clone https://github.com/flolilo/py_media-copy.git
    cd ./py_media-copy

    # create virtual environment, activate it:
    python -m venv ./.venv
    <Powershell:> & ./.venv/Scripts/activate.ps1
    <sh:> source ./.venv/bin/activate

    # install requirements:
    python -m pip install -r ./requirements.txt

    # run py_media-copy:
    python ./py_media_copy.py


Contribution
------------

You do not even need to be have an GitHub account to report issues - simply mail to
`py_media-copy@fire.fundersclub.com <mailto:py_media-copy@fire.fundersclub.com>`_. (It will *not* publish your mail
address or name!)

Please add as much information as possible - e.g. the used OS, Python version, pmc version, where the error occured,
what the error is, ...

For all versions < 0.99.x, please see the `TODO.rst file <./TODO.rst>`_ - it may be that your issue is already seen as a
milestone.

**Any help would be appreciated!**


Milestones
----------

See the `TODO.rst file <./TODO.rst>`_.


Licenses
--------

See the `LICENSE.rst file <./LICENSE.rst>`_ - You can use all of my code under either the *GNU GPLv3* or the
*BSD 3-Clause Clear* license. Please note that third party software is used in this project, but as of now, it
requires the user to download the software (and agree to the respective license agreement). If this changes in the
future, it will be reflected in this document.

As coding should not be about reinventing the wheel, some code is copied verbatim (though most of the time, it does
need modifications) from internet sources. See the ``# CREDIT:`` comments for links to my sources.
