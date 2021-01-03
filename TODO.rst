========================
py_media-copy - TODO.rst
========================


Milestones
----------

All v0.0.x-versions are considered alpha-stage! **Any version jump could break anything (i.e. no semantic versioning below 0.99.x), first stable is expected to be v0.99.1.**

.. contents:: Versions:


v0.0.1++
''''''''

- [x] Proof of concept GUI (rudimentary controls, interaction with script)
- [x] Copy a single file from ``S`` to ``T``, check checksums
- [-] Copy same file from ``T`` to ``B``, check cheksums
- [x] Dupli-check a single file against history
- [x] Dupli-check a single file against ``T`` (& ``B``) files
- [x] Make **v0.0.1** code (except GUI) capable for multiple files
- [x] Offer parameters
    - [~] Check parameters (done mostly, some missing yet)
- [x] File renaming
    - [x] Some wildcards, dates/time
    - [x] User-chosen prefix
    - [x] Counter
- [x] File overwrite-protection:
    - [x] Sources
    - [x] Targets
- [x] Include/exclude files per extension
- [x] Offer presets for settings (Saving/storing presets)
    - [ ] LOW: Store paths relative when feasible
    - [ ] LOW: ``re.sub(r'[?a-zA-z0-9-_','', param['preset'])`` (i.e. preset names only alphanumeric plus dash and underscore)
- [ ] Implement GUI for setting things up (output via console)
    - [ ] Create fallback to script-only for people without GUI-dependencies
    - [ ] ? Implement output via GUI ?
- [ ] ? Prevent computer from going to sleep ? (needs investigation whether feasible or not)
- [x] Evaluate ``exception`` for as much functions as possible.
- [x] LOW: Option to ignore files with date before/after set date (i.e. only files before 2020-04-01).
- [ ] LOW: create a paranoid-mode that re-reads hash values, maybe in second hash (e.g. CRC32/xxhash and blake2)


v0.99.0
'''''''

- [ ] All of the above are tested and work reasonably (beta-stage)
- [ ] Create ``devel``-branch
- [ ] Create binaries for Win/OSX/Linux, add to releases
- [ ] Create source package with only necessary stuff (vs. ``master``/``devel`` branch's ``requirements.txt``)


v1.0.0
''''''

- [ ] Like **v0.99.x**, but long-term tested. *(Therefore, not likely to be released soon - this should become a production tool and as such, I don't want your files to vanish!)*
- [ ] Create 1.0.0 release (binaries & source package)
