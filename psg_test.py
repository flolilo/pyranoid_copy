#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import PySimpleGUI as sg

"""
    "--filter_preference"
    "--filter_list"
    "--recursive_search"
    "--limit_timespan"
    "--timespan"
    "--deduplicate_source"
    "--deduplicate_source_tolerance"
    "--deduplicate_history"
    "--history_path"
    "--history_writemode"
    "--dedup_target"
    "--dedup_usehash"
    "--target_protect_existing"
    "--naming_subdir"
    "--naming_file"
    "--verify"
    "--nosleep"
    "--preset_save_source"
    "--preset_save_target"
    "--preset_save_settings"
    "--verbose"
"""

sg.theme('DarkAmber')

tab1_layout = [
                [
                    sg.Text('Preset:'),
                    sg.InputText(key='preset')
                ],
                [
                    sg.Text('Source path(s):', size=(14, None)),
                    sg.InputText(key='source'),
                    sg.FolderBrowse(),
                    sg.Checkbox(text='Save')
                ],
                [
                    sg.Text('Target path(s):', size=(14, None)),
                    sg.InputText(key='target'),
                    sg.FolderBrowse(),
                    sg.Checkbox(text='Save')
                ]
              ]
tab2_layout = [
                [sg.Checkbox(text='Filter', key='filter'), sg.VerticalSeparator(pad=None), sg.Checkbox(text='Filter4', key='filter4')],
                [sg.Checkbox(text='Filter2', key='filter2')],
                [sg.Checkbox(text='Filter3', key='filter3')],
                [sg.Combo(['choice 1', 'choice 2'])]
              ]

layout = [
            [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
            [sg.Button('Ok'), sg.Button('Cancel')]
         ]

# Create the Window
window = sg.Window('PSG Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    print('You entered ', values)

window.close()
