# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'py_media_copy.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 667)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 1280))
        self.mainwidget = QtWidgets.QWidget(MainWindow)
        self.mainwidget.setObjectName("mainwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabwidget = QtWidgets.QTabWidget(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabwidget.sizePolicy().hasHeightForWidth())
        self.tabwidget.setSizePolicy(sizePolicy)
        self.tabwidget.setMinimumSize(QtCore.QSize(0, 160))
        self.tabwidget.setMaximumSize(QtCore.QSize(16777215, 260))
        self.tabwidget.setToolTip("")
        self.tabwidget.setObjectName("tabwidget")
        self.tab_paths = QtWidgets.QWidget()
        self.tab_paths.setObjectName("tab_paths")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_paths)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_source = QtWidgets.QLabel(self.tab_paths)
        self.label_source.setObjectName("label_source")
        self.verticalLayout.addWidget(self.label_source)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textedit_source = QtWidgets.QTextEdit(self.tab_paths)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_source.sizePolicy().hasHeightForWidth())
        self.textedit_source.setSizePolicy(sizePolicy)
        self.textedit_source.setDocumentTitle("")
        self.textedit_source.setObjectName("textedit_source")
        self.horizontalLayout_3.addWidget(self.textedit_source)
        self.toolButton_source = QtWidgets.QToolButton(self.tab_paths)
        self.toolButton_source.setObjectName("toolButton_source")
        self.horizontalLayout_3.addWidget(self.toolButton_source)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_target = QtWidgets.QLabel(self.tab_paths)
        self.label_target.setObjectName("label_target")
        self.verticalLayout.addWidget(self.label_target)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textedit_target = QtWidgets.QTextEdit(self.tab_paths)
        self.textedit_target.setObjectName("textedit_target")
        self.horizontalLayout_2.addWidget(self.textedit_target)
        self.toolbutton_target = QtWidgets.QToolButton(self.tab_paths)
        self.toolbutton_target.setObjectName("toolbutton_target")
        self.horizontalLayout_2.addWidget(self.toolbutton_target)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabwidget.addTab(self.tab_paths, "")
        self.tab_settings_source = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_settings_source.sizePolicy().hasHeightForWidth())
        self.tab_settings_source.setSizePolicy(sizePolicy)
        self.tab_settings_source.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_settings_source.setToolTip("")
        self.tab_settings_source.setObjectName("tab_settings_source")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_settings_source)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.radiobutton_extensions_all = QtWidgets.QRadioButton(self.tab_settings_source)
        self.radiobutton_extensions_all.setObjectName("radiobutton_extensions_all")
        self.verticalLayout_5.addWidget(self.radiobutton_extensions_all)
        self.radiobutton_extensions_include = QtWidgets.QRadioButton(self.tab_settings_source)
        self.radiobutton_extensions_include.setObjectName("radiobutton_extensions_include")
        self.verticalLayout_5.addWidget(self.radiobutton_extensions_include)
        self.radiobutton_extensions_exclude = QtWidgets.QRadioButton(self.tab_settings_source)
        self.radiobutton_extensions_exclude.setObjectName("radiobutton_extensions_exclude")
        self.verticalLayout_5.addWidget(self.radiobutton_extensions_exclude)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.textedit_extensions = QtWidgets.QTextEdit(self.tab_settings_source)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_extensions.sizePolicy().hasHeightForWidth())
        self.textedit_extensions.setSizePolicy(sizePolicy)
        self.textedit_extensions.setMinimumSize(QtCore.QSize(60, 60))
        self.textedit_extensions.setMaximumSize(QtCore.QSize(120, 120))
        self.textedit_extensions.setObjectName("textedit_extensions")
        self.horizontalLayout_4.addWidget(self.textedit_extensions)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.checkbox_source_recursive = QtWidgets.QCheckBox(self.tab_settings_source)
        self.checkbox_source_recursive.setObjectName("checkbox_source_recursive")
        self.verticalLayout_6.addWidget(self.checkbox_source_recursive)
        self.line_3 = QtWidgets.QFrame(self.tab_settings_source)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.checkbox_source_dupli = QtWidgets.QCheckBox(self.tab_settings_source)
        self.checkbox_source_dupli.setChecked(False)
        self.checkbox_source_dupli.setObjectName("checkbox_source_dupli")
        self.verticalLayout_6.addWidget(self.checkbox_source_dupli)
        self.checkbox_source_dupli_tolerance = QtWidgets.QCheckBox(self.tab_settings_source)
        self.checkbox_source_dupli_tolerance.setObjectName("checkbox_source_dupli_tolerance")
        self.verticalLayout_6.addWidget(self.checkbox_source_dupli_tolerance)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.line = QtWidgets.QFrame(self.tab_settings_source)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkbox_history_check = QtWidgets.QCheckBox(self.tab_settings_source)
        self.checkbox_history_check.setChecked(False)
        self.checkbox_history_check.setObjectName("checkbox_history_check")
        self.verticalLayout_7.addWidget(self.checkbox_history_check)
        self.lineedit_history_path = QtWidgets.QLineEdit(self.tab_settings_source)
        self.lineedit_history_path.setObjectName("lineedit_history_path")
        self.verticalLayout_7.addWidget(self.lineedit_history_path)
        self.ccheckbox_history_hash = QtWidgets.QCheckBox(self.tab_settings_source)
        self.ccheckbox_history_hash.setObjectName("ccheckbox_history_hash")
        self.verticalLayout_7.addWidget(self.ccheckbox_history_hash)
        self.combobox_history = QtWidgets.QComboBox(self.tab_settings_source)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_history.sizePolicy().hasHeightForWidth())
        self.combobox_history.setSizePolicy(sizePolicy)
        self.combobox_history.setMinimumSize(QtCore.QSize(90, 0))
        self.combobox_history.setObjectName("combobox_history")
        self.combobox_history.addItem("")
        self.combobox_history.addItem("")
        self.combobox_history.addItem("")
        self.verticalLayout_7.addWidget(self.combobox_history)
        self.line_2 = QtWidgets.QFrame(self.tab_settings_source)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.checkbox_target_duplicates = QtWidgets.QCheckBox(self.tab_settings_source)
        self.checkbox_target_duplicates.setObjectName("checkbox_target_duplicates")
        self.verticalLayout_7.addWidget(self.checkbox_target_duplicates)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.tabwidget.addTab(self.tab_settings_source, "")
        self.tab_settings_target = QtWidgets.QWidget()
        self.tab_settings_target.setToolTip("")
        self.tab_settings_target.setObjectName("tab_settings_target")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_settings_target)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.checkbox_target_overwrite = QtWidgets.QCheckBox(self.tab_settings_target)
        self.checkbox_target_overwrite.setObjectName("checkbox_target_overwrite")
        self.verticalLayout_8.addWidget(self.checkbox_target_overwrite)
        self.line_6 = QtWidgets.QFrame(self.tab_settings_target)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_8.addWidget(self.line_6)
        self.label = QtWidgets.QLabel(self.tab_settings_target)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.lineedit_rename_subfolder = QtWidgets.QLineEdit(self.tab_settings_target)
        self.lineedit_rename_subfolder.setObjectName("lineedit_rename_subfolder")
        self.verticalLayout_8.addWidget(self.lineedit_rename_subfolder)
        self.label_2 = QtWidgets.QLabel(self.tab_settings_target)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.lineedit_rename_file = QtWidgets.QLineEdit(self.tab_settings_target)
        self.lineedit_rename_file.setObjectName("lineedit_rename_file")
        self.verticalLayout_8.addWidget(self.lineedit_rename_file)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_settings_target)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(120, 120))
        self.textBrowser.setMaximumSize(QtCore.QSize(180, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_6.addWidget(self.textBrowser)
        self.tabwidget.addTab(self.tab_settings_target, "")
        self.tab_settings_etc = QtWidgets.QWidget()
        self.tab_settings_etc.setObjectName("tab_settings_etc")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_settings_etc)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.checkbox_verify = QtWidgets.QCheckBox(self.tab_settings_etc)
        self.checkbox_verify.setObjectName("checkbox_verify")
        self.verticalLayout_3.addWidget(self.checkbox_verify)
        self.combobox_hashselect = QtWidgets.QComboBox(self.tab_settings_etc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_hashselect.sizePolicy().hasHeightForWidth())
        self.combobox_hashselect.setSizePolicy(sizePolicy)
        self.combobox_hashselect.setMinimumSize(QtCore.QSize(80, 0))
        self.combobox_hashselect.setMaximumSize(QtCore.QSize(120, 16777215))
        self.combobox_hashselect.setObjectName("combobox_hashselect")
        self.combobox_hashselect.addItem("")
        self.combobox_hashselect.addItem("")
        self.combobox_hashselect.addItem("")
        self.verticalLayout_3.addWidget(self.combobox_hashselect)
        self.line_4 = QtWidgets.QFrame(self.tab_settings_etc)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.checkbox_mirror_compress = QtWidgets.QCheckBox(self.tab_settings_etc)
        self.checkbox_mirror_compress.setObjectName("checkbox_mirror_compress")
        self.verticalLayout_3.addWidget(self.checkbox_mirror_compress)
        self.line_5 = QtWidgets.QFrame(self.tab_settings_etc)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.checkbox_standby = QtWidgets.QCheckBox(self.tab_settings_etc)
        self.checkbox_standby.setObjectName("checkbox_standby")
        self.verticalLayout_3.addWidget(self.checkbox_standby)
        spacerItem5 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.line_8 = QtWidgets.QFrame(self.tab_settings_etc)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_10.addWidget(self.line_8)
        self.line_7 = QtWidgets.QFrame(self.tab_settings_etc)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_10.addWidget(self.line_7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.label_3 = QtWidgets.QLabel(self.tab_settings_etc)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox = QtWidgets.QComboBox(self.tab_settings_etc)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.tab_settings_etc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.label_4 = QtWidgets.QLabel(self.tab_settings_etc)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_settings_etc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(90, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_settings_etc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(180, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.label_5 = QtWidgets.QLabel(self.tab_settings_etc)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.tab_settings_etc)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.horizontalGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalGroupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalGroupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalGroupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.horizontalGroupBox)
        spacerItem7 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.tabwidget.addTab(self.tab_settings_etc, "")
        self.verticalLayout_2.addWidget(self.tabwidget)
        self.textedit_outputconsole = QtWidgets.QTextEdit(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_outputconsole.sizePolicy().hasHeightForWidth())
        self.textedit_outputconsole.setSizePolicy(sizePolicy)
        self.textedit_outputconsole.setMinimumSize(QtCore.QSize(0, 0))
        self.textedit_outputconsole.setReadOnly(True)
        self.textedit_outputconsole.setObjectName("textedit_outputconsole")
        self.verticalLayout_2.addWidget(self.textedit_outputconsole)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.pushbutton_start = QtWidgets.QPushButton(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushbutton_start.sizePolicy().hasHeightForWidth())
        self.pushbutton_start.setSizePolicy(sizePolicy)
        self.pushbutton_start.setMinimumSize(QtCore.QSize(60, 20))
        self.pushbutton_start.setMaximumSize(QtCore.QSize(100, 36))
        self.pushbutton_start.setObjectName("pushbutton_start")
        self.horizontalLayout.addWidget(self.pushbutton_start, 0, QtCore.Qt.AlignHCenter)
        spacerItem9 = QtWidgets.QSpacerItem(156, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.pushbutton_exit = QtWidgets.QPushButton(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushbutton_exit.sizePolicy().hasHeightForWidth())
        self.pushbutton_exit.setSizePolicy(sizePolicy)
        self.pushbutton_exit.setMinimumSize(QtCore.QSize(60, 20))
        self.pushbutton_exit.setMaximumSize(QtCore.QSize(100, 36))
        self.pushbutton_exit.setObjectName("pushbutton_exit")
        self.horizontalLayout.addWidget(self.pushbutton_exit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.mainwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.retranslateUi(MainWindow)
        self.tabwidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_source.setText(_translate("MainWindow", "Source(s):"))
        self.textedit_source.setToolTip(_translate("MainWindow", "For >1 sources, use a line for each"))
        self.toolButton_source.setText(_translate("MainWindow", "..."))
        self.label_target.setText(_translate("MainWindow", "Target(s):"))
        self.textedit_target.setToolTip(_translate("MainWindow", "For >1 targets, use a line for each"))
        self.toolbutton_target.setText(_translate("MainWindow", "..."))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_paths), _translate("MainWindow", "Paths"))
        self.radiobutton_extensions_all.setText(_translate("MainWindow", "A&ll files"))
        self.radiobutton_extensions_include.setText(_translate("MainWindow", "Incl&ude:"))
        self.radiobutton_extensions_exclude.setText(_translate("MainWindow", "E&xclude:"))
        self.checkbox_source_recursive.setText(_translate("MainWindow", "Recursive search in source(s)"))
        self.checkbox_source_dupli.setText(_translate("MainWindow", "Search for duplicates in source(s)"))
        self.checkbox_source_dupli_tolerance.setText(_translate("MainWindow", "Allow 3sec difference in sources"))
        self.checkbox_history_check.setText(_translate("MainWindow", "Search for duplicates in history"))
        self.ccheckbox_history_hash.setText(_translate("MainWindow", "Include checksum in history-dedup"))
        self.combobox_history.setItemText(0, _translate("MainWindow", "Append new history"))
        self.combobox_history.setItemText(1, _translate("MainWindow", "Override history"))
        self.combobox_history.setItemText(2, _translate("MainWindow", "Don\'t add new history"))
        self.checkbox_target_duplicates.setText(_translate("MainWindow", "Search for duplicates in target(s)"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_settings_source), _translate("MainWindow", "Settings - Source"))
        self.checkbox_target_overwrite.setText(_translate("MainWindow", "Prevent overwriting existing files"))
        self.label.setText(_translate("MainWindow", "Sulbolder naming:"))
        self.label_2.setText(_translate("MainWindow", "File naming:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Magic strings:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%y2%    17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%y4%    2017</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%M%    05</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%d%    31</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%h%    14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%m%    26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s%    59</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%n%    file name</p></body></html>"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_settings_target), _translate("MainWindow", "Settings - Target"))
        self.checkbox_verify.setText(_translate("MainWindow", "Verify copied files using checksums"))
        self.combobox_hashselect.setItemText(0, _translate("MainWindow", "CRC"))
        self.combobox_hashselect.setItemText(1, _translate("MainWindow", "MD5"))
        self.combobox_hashselect.setItemText(2, _translate("MainWindow", "SHA1"))
        self.checkbox_mirror_compress.setText(_translate("MainWindow", "Compress files in target #n > 1"))
        self.checkbox_standby.setText(_translate("MainWindow", "Prevent computer from sleeping"))
        self.label_3.setText(_translate("MainWindow", "Load preset:"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.label_4.setText(_translate("MainWindow", "Save preset:"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "What to save:"))
        self.checkBox_2.setText(_translate("MainWindow", "Target(s)"))
        self.checkBox_3.setText(_translate("MainWindow", "Source(s)"))
        self.checkBox.setText(_translate("MainWindow", "Settings"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_settings_etc), _translate("MainWindow", "Settings"))
        self.pushbutton_start.setText(_translate("MainWindow", "Start"))
        self.pushbutton_exit.setText(_translate("MainWindow", "Exit"))
        self.actionLoad.setText(_translate("MainWindow", "&Load"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))


