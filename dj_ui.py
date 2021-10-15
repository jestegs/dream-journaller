# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'journallerqWZnyg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_window_main(object):
    def setupUi(self, window_main):
        if not window_main.objectName():
            window_main.setObjectName(u"window_main")
        window_main.resize(655, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window_main.sizePolicy().hasHeightForWidth())
        window_main.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        window_main.setFont(font)
        window_main.setWindowTitle(u"Dream Journaller")
        icon = QIcon()
        icon.addFile(u"images/journal_book.ico", QSize(), QIcon.Normal, QIcon.Off)
        window_main.setWindowIcon(icon)
        self.menu_file_new = QAction(window_main)
        self.menu_file_new.setObjectName(u"menu_file_new")
        self.menu_file_saveas = QAction(window_main)
        self.menu_file_saveas.setObjectName(u"menu_file_saveas")
        self.menu_file_load = QAction(window_main)
        self.menu_file_load.setObjectName(u"menu_file_load")
        self.menu_file_exit = QAction(window_main)
        self.menu_file_exit.setObjectName(u"menu_file_exit")
        self.menu_file_save = QAction(window_main)
        self.menu_file_save.setObjectName(u"menu_file_save")
        self.menu_del_journal = QAction(window_main)
        self.menu_del_journal.setObjectName(u"menu_del_journal")
        self.actionLoad_Journal = QAction(window_main)
        self.actionLoad_Journal.setObjectName(u"actionLoad_Journal")
        self.central_widget = QWidget(window_main)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy1)
        self.central_widget.setAutoFillBackground(True)
        self.formLayout = QFormLayout(self.central_widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.layout_tags_list = QGroupBox(self.central_widget)
        self.layout_tags_list.setObjectName(u"layout_tags_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.layout_tags_list.sizePolicy().hasHeightForWidth())
        self.layout_tags_list.setSizePolicy(sizePolicy2)
        self.layout_tags_list.setMinimumSize(QSize(131, 0))
        self.layout_tags_list.setMaximumSize(QSize(151, 16777215))
        self.layout_tags_list.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(self.layout_tags_list)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_new_tag = QLabel(self.layout_tags_list)
        self.label_new_tag.setObjectName(u"label_new_tag")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_new_tag.sizePolicy().hasHeightForWidth())
        self.label_new_tag.setSizePolicy(sizePolicy3)
        self.label_new_tag.setFont(font)
        self.label_new_tag.setAutoFillBackground(False)

        self.verticalLayout_3.addWidget(self.label_new_tag)

        self.enter_new_tag = QLineEdit(self.layout_tags_list)
        self.enter_new_tag.setObjectName(u"enter_new_tag")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.enter_new_tag.sizePolicy().hasHeightForWidth())
        self.enter_new_tag.setSizePolicy(sizePolicy4)
        self.enter_new_tag.setMinimumSize(QSize(111, 0))
        self.enter_new_tag.setFont(font)
        self.enter_new_tag.setAutoFillBackground(False)

        self.verticalLayout_3.addWidget(self.enter_new_tag)

        self.list_tags_list = QListWidget(self.layout_tags_list)
        self.list_tags_list.setObjectName(u"list_tags_list")
        sizePolicy.setHeightForWidth(self.list_tags_list.sizePolicy().hasHeightForWidth())
        self.list_tags_list.setSizePolicy(sizePolicy)
        self.list_tags_list.setMinimumSize(QSize(111, 0))
        self.list_tags_list.setMaximumSize(QSize(111, 16777215))
        self.list_tags_list.setFont(font)
        self.list_tags_list.setAutoFillBackground(False)
        self.list_tags_list.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_tags_list.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.list_tags_list)

        self.b_delete_tags = QPushButton(self.layout_tags_list)
        self.b_delete_tags.setObjectName(u"b_delete_tags")
        sizePolicy4.setHeightForWidth(self.b_delete_tags.sizePolicy().hasHeightForWidth())
        self.b_delete_tags.setSizePolicy(sizePolicy4)
        self.b_delete_tags.setMinimumSize(QSize(111, 0))
        self.b_delete_tags.setAutoFillBackground(False)

        self.verticalLayout_3.addWidget(self.b_delete_tags)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.layout_tags_list)

        self.layout_entry = QGroupBox(self.central_widget)
        self.layout_entry.setObjectName(u"layout_entry")
        sizePolicy2.setHeightForWidth(self.layout_entry.sizePolicy().hasHeightForWidth())
        self.layout_entry.setSizePolicy(sizePolicy2)
        self.layout_entry.setMinimumSize(QSize(500, 0))
        self.layout_entry.setMaximumSize(QSize(500, 16777215))
        self.layout_entry.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.layout_entry)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_header = QFrame(self.layout_entry)
        self.layout_header.setObjectName(u"layout_header")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.layout_header.sizePolicy().hasHeightForWidth())
        self.layout_header.setSizePolicy(sizePolicy5)
        self.layout_header.setMinimumSize(QSize(0, 181))
        self.layout_header.setMaximumSize(QSize(16777215, 181))
        self.layout_header.setAutoFillBackground(False)
        self.layout_header.setFrameShape(QFrame.StyledPanel)
        self.layout_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.layout_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_entry_tags = QGroupBox(self.layout_header)
        self.layout_entry_tags.setObjectName(u"layout_entry_tags")
        sizePolicy3.setHeightForWidth(self.layout_entry_tags.sizePolicy().hasHeightForWidth())
        self.layout_entry_tags.setSizePolicy(sizePolicy3)
        self.layout_entry_tags.setMinimumSize(QSize(131, 160))
        self.layout_entry_tags.setMaximumSize(QSize(131, 160))
        self.layout_entry_tags.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.layout_entry_tags)
        self.gridLayout.setObjectName(u"gridLayout")
        self.b_remove_tag = QPushButton(self.layout_entry_tags)
        self.b_remove_tag.setObjectName(u"b_remove_tag")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.b_remove_tag.sizePolicy().hasHeightForWidth())
        self.b_remove_tag.setSizePolicy(sizePolicy6)
        self.b_remove_tag.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.b_remove_tag, 2, 2, 1, 1)

        self.b_add_tag = QPushButton(self.layout_entry_tags)
        self.b_add_tag.setObjectName(u"b_add_tag")
        sizePolicy6.setHeightForWidth(self.b_add_tag.sizePolicy().hasHeightForWidth())
        self.b_add_tag.setSizePolicy(sizePolicy6)
        self.b_add_tag.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.b_add_tag, 2, 1, 1, 1)

        self.list_entry_tags = QListWidget(self.layout_entry_tags)
        self.list_entry_tags.setObjectName(u"list_entry_tags")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.list_entry_tags.sizePolicy().hasHeightForWidth())
        self.list_entry_tags.setSizePolicy(sizePolicy7)
        self.list_entry_tags.setMinimumSize(QSize(111, 100))
        self.list_entry_tags.setMaximumSize(QSize(111, 100))
        self.list_entry_tags.setFont(font)
        self.list_entry_tags.setAutoFillBackground(False)
        self.list_entry_tags.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_entry_tags.setSortingEnabled(True)

        self.gridLayout.addWidget(self.list_entry_tags, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.layout_entry_tags)

        self.heading = QFrame(self.layout_header)
        self.heading.setObjectName(u"heading")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.heading.sizePolicy().hasHeightForWidth())
        self.heading.setSizePolicy(sizePolicy8)
        self.heading.setMaximumSize(QSize(16777215, 150))
        self.heading.setFrameShape(QFrame.StyledPanel)
        self.heading.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.heading)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(-1, -1, 9, -1)
        self.label_title = QLabel(self.heading)
        self.label_title.setObjectName(u"label_title")
        sizePolicy6.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy6)
        self.label_title.setFont(font)
        self.label_title.setAutoFillBackground(False)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_title)

        self.layout_title = QHBoxLayout()
        self.layout_title.setObjectName(u"layout_title")
        self.enter_title = QLineEdit(self.heading)
        self.enter_title.setObjectName(u"enter_title")
        sizePolicy6.setHeightForWidth(self.enter_title.sizePolicy().hasHeightForWidth())
        self.enter_title.setSizePolicy(sizePolicy6)
        self.enter_title.setMinimumSize(QSize(200, 20))
        self.enter_title.setMaximumSize(QSize(250, 20))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(84, 84, 84, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.enter_title.setPalette(palette)
        self.enter_title.setFont(font)
        self.enter_title.setToolTipDuration(-1)
        self.enter_title.setAutoFillBackground(False)
        self.enter_title.setAlignment(Qt.AlignCenter)

        self.layout_title.addWidget(self.enter_title)


        self.verticalLayout_4.addLayout(self.layout_title)

        self.label_date = QLabel(self.heading)
        self.label_date.setObjectName(u"label_date")
        sizePolicy6.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy6)
        self.label_date.setFont(font)
        self.label_date.setAutoFillBackground(False)
        self.label_date.setStyleSheet(u"")
        self.label_date.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_date)

        self.layout_date = QHBoxLayout()
        self.layout_date.setObjectName(u"layout_date")
        self.enter_date = QLineEdit(self.heading)
        self.enter_date.setObjectName(u"enter_date")
        sizePolicy6.setHeightForWidth(self.enter_date.sizePolicy().hasHeightForWidth())
        self.enter_date.setSizePolicy(sizePolicy6)
        self.enter_date.setMinimumSize(QSize(100, 20))
        self.enter_date.setMaximumSize(QSize(100, 20))
        self.enter_date.setFont(font)
        self.enter_date.setAutoFillBackground(False)
        self.enter_date.setAlignment(Qt.AlignCenter)

        self.layout_date.addWidget(self.enter_date)


        self.verticalLayout_4.addLayout(self.layout_date)


        self.horizontalLayout.addWidget(self.heading)


        self.verticalLayout_2.addWidget(self.layout_header)

        self.text_entry = QTextEdit(self.layout_entry)
        self.text_entry.setObjectName(u"text_entry")
        sizePolicy1.setHeightForWidth(self.text_entry.sizePolicy().hasHeightForWidth())
        self.text_entry.setSizePolicy(sizePolicy1)
        self.text_entry.setAutoFillBackground(False)
        self.text_entry.setFrameShape(QFrame.StyledPanel)
        self.text_entry.setLineWidth(1)
        self.text_entry.setMidLineWidth(0)
        self.text_entry.setTabStopWidth(40)
        self.text_entry.setAcceptRichText(False)

        self.verticalLayout_2.addWidget(self.text_entry)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.layout_entry)

        window_main.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(window_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 655, 23))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        window_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(window_main)
        self.statusbar.setObjectName(u"statusbar")
        window_main.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.enter_title, self.enter_date)
        QWidget.setTabOrder(self.enter_date, self.enter_new_tag)
        QWidget.setTabOrder(self.enter_new_tag, self.text_entry)
        QWidget.setTabOrder(self.text_entry, self.list_entry_tags)
        QWidget.setTabOrder(self.list_entry_tags, self.b_add_tag)
        QWidget.setTabOrder(self.b_add_tag, self.b_remove_tag)
        QWidget.setTabOrder(self.b_remove_tag, self.b_delete_tags)
        QWidget.setTabOrder(self.b_delete_tags, self.list_tags_list)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.menu_file_new)
        self.menu_file.addAction(self.menu_file_save)
        self.menu_file.addAction(self.menu_file_saveas)
        self.menu_file.addAction(self.menu_file_load)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionLoad_Journal)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_file_exit)

        self.retranslateUi(window_main)

        QMetaObject.connectSlotsByName(window_main)
    # setupUi

    def retranslateUi(self, window_main):
        self.menu_file_new.setText(QCoreApplication.translate("window_main", u"New Entry", None))
#if QT_CONFIG(shortcut)
        self.menu_file_new.setShortcut(QCoreApplication.translate("window_main", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.menu_file_saveas.setText(QCoreApplication.translate("window_main", u"Save As...", None))
        self.menu_file_load.setText(QCoreApplication.translate("window_main", u"Load Entry...", None))
        self.menu_file_exit.setText(QCoreApplication.translate("window_main", u"Exit", None))
        self.menu_file_save.setText(QCoreApplication.translate("window_main", u"Save", None))
#if QT_CONFIG(shortcut)
        self.menu_file_save.setShortcut(QCoreApplication.translate("window_main", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.menu_del_journal.setText(QCoreApplication.translate("window_main", u"Delete Journal...", None))
        self.actionLoad_Journal.setText(QCoreApplication.translate("window_main", u"Load Journal...", None))
        self.layout_tags_list.setTitle(QCoreApplication.translate("window_main", u"Tags List", None))
        self.label_new_tag.setText(QCoreApplication.translate("window_main", u"Enter New Tag", None))
        self.b_delete_tags.setText(QCoreApplication.translate("window_main", u"Delete Tags", None))
        self.layout_entry.setTitle(QCoreApplication.translate("window_main", u"Dream", None))
        self.layout_entry_tags.setTitle(QCoreApplication.translate("window_main", u"Entry Tags", None))
        self.b_remove_tag.setText(QCoreApplication.translate("window_main", u"-", None))
        self.b_add_tag.setText(QCoreApplication.translate("window_main", u"+", None))
        self.label_title.setText(QCoreApplication.translate("window_main", u"Title", None))
        self.enter_title.setText("")
        self.label_date.setText(QCoreApplication.translate("window_main", u"Date", None))
        self.menu_file.setTitle(QCoreApplication.translate("window_main", u"File", None))
        self.menu_edit.setTitle(QCoreApplication.translate("window_main", u"Edit", None))
        self.menu_help.setTitle(QCoreApplication.translate("window_main", u"Help", None))
        pass
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadDialogfkoxFd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_LoadDialog(object):
    def setupUi(self, LoadDialog):
        if not LoadDialog.objectName():
            LoadDialog.setObjectName(u"LoadDialog")
        LoadDialog.resize(272, 602)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadDialog.sizePolicy().hasHeightForWidth())
        LoadDialog.setSizePolicy(sizePolicy)
        LoadDialog.setMinimumSize(QSize(272, 602))
        LoadDialog.setMaximumSize(QSize(272, 602))
        font = QFont()
        font.setPointSize(10)
        LoadDialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(LoadDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(LoadDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(151, 0))
        self.groupBox.setMaximumSize(QSize(151, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_journ_sel = QLabel(self.groupBox)
        self.label_journ_sel.setObjectName(u"label_journ_sel")
        self.label_journ_sel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_journ_sel)

        self.journ_sel = QComboBox(self.groupBox)
        self.journ_sel.setObjectName(u"journ_sel")

        self.verticalLayout.addWidget(self.journ_sel)

        self.list_entries = QListWidget(self.groupBox)
        self.list_entries.setObjectName(u"list_entries")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_entries.sizePolicy().hasHeightForWidth())
        self.list_entries.setSizePolicy(sizePolicy2)
        self.list_entries.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.list_entries)


        self.horizontalLayout.addWidget(self.groupBox)

        self.frame = QFrame(LoadDialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.b_load_entry = QPushButton(self.frame)
        self.b_load_entry.setObjectName(u"b_load_entry")

        self.verticalLayout_3.addWidget(self.b_load_entry)

        self.b_delete = QPushButton(self.frame)
        self.b_delete.setObjectName(u"b_delete")

        self.verticalLayout_3.addWidget(self.b_delete)

        self.b_cancel = QPushButton(self.frame)
        self.b_cancel.setObjectName(u"b_cancel")

        self.verticalLayout_3.addWidget(self.b_cancel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(LoadDialog)

        QMetaObject.connectSlotsByName(LoadDialog)
    # setupUi

    def retranslateUi(self, LoadDialog):
        LoadDialog.setWindowTitle(QCoreApplication.translate("LoadDialog", u"LoadEntry", None))
        self.groupBox.setTitle(QCoreApplication.translate("LoadDialog", u"Entries", None))
        self.label_journ_sel.setText(QCoreApplication.translate("LoadDialog", u"Journal", None))
        self.b_load_entry.setText(QCoreApplication.translate("LoadDialog", u"Load Entry", None))
        self.b_delete.setText(QCoreApplication.translate("LoadDialog", u"Delete", None))
        self.b_cancel.setText(QCoreApplication.translate("LoadDialog", u"Cancel", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveDialogeZZVGP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_SaveEntry(object):
    def setupUi(self, SaveEntry):
        if not SaveEntry.objectName():
            SaveEntry.setObjectName(u"SaveEntry")
        SaveEntry.resize(364, 356)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SaveEntry.sizePolicy().hasHeightForWidth())
        SaveEntry.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        SaveEntry.setFont(font)
        self.verticalLayout = QVBoxLayout(SaveEntry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.entry_layout = QVBoxLayout()
        self.entry_layout.setObjectName(u"entry_layout")
        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.entry_layout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_journ_sel = QLabel(SaveEntry)
        self.label_journ_sel.setObjectName(u"label_journ_sel")
        self.label_journ_sel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_journ_sel)

        self.journ_sel = QComboBox(SaveEntry)
        self.journ_sel.setObjectName(u"journ_sel")

        self.horizontalLayout_2.addWidget(self.journ_sel)


        self.entry_layout.addLayout(self.horizontalLayout_2)

        self.label_num = QLabel(SaveEntry)
        self.label_num.setObjectName(u"label_num")
        self.label_num.setAlignment(Qt.AlignCenter)

        self.entry_layout.addWidget(self.label_num)

        self.enter_num = QLineEdit(SaveEntry)
        self.enter_num.setObjectName(u"enter_num")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enter_num.sizePolicy().hasHeightForWidth())
        self.enter_num.setSizePolicy(sizePolicy1)
        self.enter_num.setReadOnly(False)

        self.entry_layout.addWidget(self.enter_num)

        self.label_title = QLabel(SaveEntry)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.entry_layout.addWidget(self.label_title)

        self.enter_title = QLineEdit(SaveEntry)
        self.enter_title.setObjectName(u"enter_title")
        sizePolicy1.setHeightForWidth(self.enter_title.sizePolicy().hasHeightForWidth())
        self.enter_title.setSizePolicy(sizePolicy1)
        self.enter_title.setReadOnly(True)

        self.entry_layout.addWidget(self.enter_title)

        self.label_date = QLabel(SaveEntry)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setAlignment(Qt.AlignCenter)

        self.entry_layout.addWidget(self.label_date)

        self.enter_date = QLineEdit(SaveEntry)
        self.enter_date.setObjectName(u"enter_date")
        sizePolicy1.setHeightForWidth(self.enter_date.sizePolicy().hasHeightForWidth())
        self.enter_date.setSizePolicy(sizePolicy1)
        self.enter_date.setReadOnly(True)

        self.entry_layout.addWidget(self.enter_date)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.entry_layout.addItem(self.verticalSpacer)

        self.label_tags = QLabel(SaveEntry)
        self.label_tags.setObjectName(u"label_tags")
        self.label_tags.setAlignment(Qt.AlignCenter)

        self.entry_layout.addWidget(self.label_tags)

        self.tags_list = QPlainTextEdit(SaveEntry)
        self.tags_list.setObjectName(u"tags_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tags_list.sizePolicy().hasHeightForWidth())
        self.tags_list.setSizePolicy(sizePolicy2)
        self.tags_list.setMaximumSize(QSize(16777215, 100))
        self.tags_list.setTextInteractionFlags(Qt.NoTextInteraction)

        self.entry_layout.addWidget(self.tags_list)


        self.horizontalLayout.addLayout(self.entry_layout)

        self.button_layout = QVBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.b_new_journ = QPushButton(SaveEntry)
        self.b_new_journ.setObjectName(u"b_new_journ")

        self.button_layout.addWidget(self.b_new_journ)

        self.b_confirm = QPushButton(SaveEntry)
        self.b_confirm.setObjectName(u"b_confirm")

        self.button_layout.addWidget(self.b_confirm)

        self.b_cancel = QPushButton(SaveEntry)
        self.b_cancel.setObjectName(u"b_cancel")

        self.button_layout.addWidget(self.b_cancel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.button_layout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.button_layout)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SaveEntry)

        QMetaObject.connectSlotsByName(SaveEntry)
    # setupUi

    def retranslateUi(self, SaveEntry):
        SaveEntry.setWindowTitle(QCoreApplication.translate("SaveEntry", u"Dialog", None))
        self.label_journ_sel.setText(QCoreApplication.translate("SaveEntry", u"Journal", None))
        self.label_num.setText(QCoreApplication.translate("SaveEntry", u"Entry Number", None))
        self.label_title.setText(QCoreApplication.translate("SaveEntry", u"Title", None))
        self.label_date.setText(QCoreApplication.translate("SaveEntry", u"Date", None))
        self.label_tags.setText(QCoreApplication.translate("SaveEntry", u"Tags", None))
        self.b_new_journ.setText(QCoreApplication.translate("SaveEntry", u"New Journal", None))
        self.b_confirm.setText(QCoreApplication.translate("SaveEntry", u"Save Entry", None))
        self.b_cancel.setText(QCoreApplication.translate("SaveEntry", u"Cancel", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newJournalNbYQov.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_NewJournal(object):
    def setupUi(self, NewJournal):
        if not NewJournal.objectName():
            NewJournal.setObjectName(u"NewJournal")
        NewJournal.resize(236, 117)
        self.verticalLayout_2 = QVBoxLayout(NewJournal)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_new_j = QLabel(NewJournal)
        self.label_new_j.setObjectName(u"label_new_j")
        font = QFont()
        font.setPointSize(10)
        self.label_new_j.setFont(font)

        self.verticalLayout.addWidget(self.label_new_j)

        self.enter_new_j = QLineEdit(NewJournal)
        self.enter_new_j.setObjectName(u"enter_new_j")
        self.enter_new_j.setFont(font)

        self.verticalLayout.addWidget(self.enter_new_j)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.b_save = QPushButton(NewJournal)
        self.b_save.setObjectName(u"b_save")
        self.b_save.setFont(font)

        self.verticalLayout_3.addWidget(self.b_save)

        self.b_cancel = QPushButton(NewJournal)
        self.b_cancel.setObjectName(u"b_cancel")
        self.b_cancel.setFont(font)

        self.verticalLayout_3.addWidget(self.b_cancel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(NewJournal)

        QMetaObject.connectSlotsByName(NewJournal)
    # setupUi

    def retranslateUi(self, NewJournal):
        NewJournal.setWindowTitle(QCoreApplication.translate("NewJournal", u"Dialog", None))
        self.label_new_j.setText(QCoreApplication.translate("NewJournal", u"New Journal Name:", None))
        self.b_save.setText(QCoreApplication.translate("NewJournal", u"Save Journal", None))
        self.b_cancel.setText(QCoreApplication.translate("NewJournal", u"Cancel", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delJournalDialogJLDFLW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_deleteJournal(object):
    def setupUi(self, deleteJournal):
        if not deleteJournal.objectName():
            deleteJournal.setObjectName(u"deleteJournal")
        deleteJournal.resize(334, 72)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deleteJournal.sizePolicy().hasHeightForWidth())
        deleteJournal.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(deleteJournal)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.journal_box = QComboBox(deleteJournal)
        self.journal_box.setObjectName(u"journal_box")
        sizePolicy.setHeightForWidth(self.journal_box.sizePolicy().hasHeightForWidth())
        self.journal_box.setSizePolicy(sizePolicy)
        self.journal_box.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.journal_box)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b_delete = QPushButton(deleteJournal)
        self.b_delete.setObjectName(u"b_delete")

        self.verticalLayout.addWidget(self.b_delete)

        self.b_cancel = QPushButton(deleteJournal)
        self.b_cancel.setObjectName(u"b_cancel")

        self.verticalLayout.addWidget(self.b_cancel)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(deleteJournal)

        QMetaObject.connectSlotsByName(deleteJournal)
    # setupUi

    def retranslateUi(self, deleteJournal):
        deleteJournal.setWindowTitle(QCoreApplication.translate("deleteJournal", u"Dialog", None))
        self.b_delete.setText(QCoreApplication.translate("deleteJournal", u"Delete", None))
        self.b_cancel.setText(QCoreApplication.translate("deleteJournal", u"Cancel", None))
    # retranslateUi



#if __name__ == "__main__":
    #import sys
    #app = QApplication(sys.argv)
    #MainWindow = QMainWindow()
    #ui = Ui_window_main()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())
