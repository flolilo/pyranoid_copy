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
    - [ ] Check parameters (done mostly, some missing yet)
- [ ] File renaming
    - [x] Some wildcards, dates/time
    - [x] User-chosen prefix
    - [ ] Counter
- [ ] File overwrite-protection:
    - [ ] Sources
    - [x] Targets
- [x] Include/exclude files per extension
- [ ] Offer presets for settings
    - [ ] Saving/storing presets
- [ ] Implement GUI for setting things up (output via console)
    - [ ] Create fallback to script-only for people without GUI-dependencies
    - [ ] Implement output via GUI?
- [ ] ? Prevent computer from going to sleep ? (needs investigation whether feasible or not)
- [ ] Make ``exceptions``
- [ ] LOW: create a paranoid-mode that re-reads hash values.


v0.99.0
'''''''

- [ ] All of the above are tested and work reasonably (beta-stage)
- [ ] Create ``devel``-branch


v1.0.0
''''''

- [ ] Like **v0.99.x**, but long-term tested. *(Therefore, not likely to be released soon - this should become a production tool and as such, I don't want your files to vanish!)*
