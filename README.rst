======
README
======


What is pyranoid copy
=====================

A lightweight & granular file copy tool built for DITs and photographers.

This tool should become the sucessor to my `media-copytool <https://github.com/flolilo/media-copytool>`_ (which is
scripted entirely in PowerShell and Windows only). The reason that I created media-copytool is because none of the
existing Digital Asset Management (DAM) programs (to my knowledge) offered the options for importing files from media
cards that I wanted (see `Proposed features`_). pyranoid_copy will be written in Python to maximise compatibility.

**Note that as of now, this tool is not even finished in a rough state - I am still in the progress of writing the main
features and testing them.**


Proposed features
=================

- Will work on all (desktop) OSs that are supported by `Python ≥ 3.5 <https://www.python.org/downloads/>`_,
- Optimised for copying large quantities of mission critical files, e.g. wedding photos,
- Lightweight,
- Standalone binaries (i.e. ``pyranoid_copy.exe``) available,
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
=======

- Lightweight `PySimpleGUI <https://github.com/PySimpleGUI/PySimpleGUI>`_ for the parameters with CLI as option,
- Standalone planned / as little extra dependencies as feasible (and all on `pip <https://pypi.org/>`_) with decent
  usability (planned at the moment: `tqdm <https://github.com/tqdm/tqdm>`_ required,
  `colorama <https://github.com/tartley/colorama>`_ recommended, `crc32c <https://github.com/ICRAR/crc32c>`_ if
  desired) for "source" installation (i.e. not using the binaries, but the script file itself),
- (Smart) renaming options for files and subfolders:
  `Strftime magic strings <https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior>`_ (e.g.
  ``%Y-%m-%d`` for ``2019-11-31``),
- Redundancy checks against history file / target-folder / multiple inputs,
- Checking CRC32 of every file after clearing the disk cache, thus reducing the risk of a bad copy,
- Include/exclude by regex pattern(s) (e.g. ``.*\.jpg`` - see 
  `my regex101.com example <https://regex101.com/r/0WHdUL/2>`_ for what this does).


A high-level overview::

                                +------------+        +-------------------+        +----------------+
    +------START-------+        | Check for  |        | Search files,     |        | Deduplication- |
    |./pyranoid_copy.py| -----> | parameters | -----> | then filter them* | -----> | routines*      |
    +------------------+        | & presets  |        +-------------------+        +----------------+
                                +------------+                                              |         
                                                                                            |         
                                                                                            v         
    +--------------+                                +---------------------+         +--------------+  
    | Get target's |        +--------------+        | Create subfolders*, |         | Get source's |  
    | hash*        | <----- | Copy file(s) | <----- | check for file name | <------ | hash*        |  
    +--------------+        +--------------+        | collisions*         |         +--------------+  
            |                                       +---------------------+                          
            |                                                                                           
            v                                                                                           
    +---------------+         +-----------+                                                            
    | Compare file- |         |           |                                                            
    | attributes*   | ------> |   DONE!   |                                                            
    +---------------+         |           |                                                            
                              +-----------+                                                            
                                                                                                        
    * can be enabled/disabled                                                                           


Installation
============

**This will probably change once this repo is in a working state. At the moment:**

.. code-block:: Shell

    # get the repository:
    git clone https://github.com/flolilo/pyranoid_copy.git
    cd ./pyranoid_copy

    # create virtual environment, activate it:
    python -m venv ./.venv
    <Powershell:> & ./.venv/Scripts/activate.ps1
    <sh:> source ./.venv/bin/activate

    # install requirements:
    python -m pip install -r ./requirements.txt

    # run pyranoid_copy:
    python ./pyranoid_copy.py


Contribution
============

You do not even need to be have an GitHub account to report issues - simply mail to
`pyranoid_copy@fire.fundersclub.com <mailto:pyranoid_copy@fire.fundersclub.com>`_. (It will *not* publish your mail
address or name!)

Please add as much information as possible - e.g. the used OS, Python version, pyranoid version, where the error
occured, what the error is, ...

For all versions < 0.99.x, please see `TODO.rst`_ - it may be that your issue is already seen as a
milestone.

**Any help would be appreciated!**


Milestones
==========

See `TODO.rst`_.


Licenses
========

See `LICENSE.rst`_ - You can use all of my code under either the *GNU GPLv3* or the
*BSD 3-Clause Clear* license. Please note that third party software is used in this project, but as of now, it
requires the user to download the software (and agree to the respective license agreement). If this changes in the
future, it will be reflected in this document.

As coding should not be about reinventing the wheel, some code is copied verbatim (though most of the time, it does
need modifications) from internet sources. See the ``# CREDIT:`` comments for links to my sources.

.. _TODO.rst: https://pyranoid-copy.readthedocs.io/en/latest/todo.html
.. _LICENSE.rst: https://pyranoid-copy.readthedocs.io/en/latest/license.html
