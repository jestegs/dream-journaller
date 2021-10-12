import sys

from PySide2.QtWidgets import QDialog, QMainWindow, QApplication, QMessageBox

from dj_ui import Ui_window_main, Ui_LoadDialog, Ui_SaveEntry, Ui_NewJournal, Ui_deleteJournal
import dj_database as db

loaded_dream = []
dream_to_save = []


class LoadDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoadDialog()
        self.ui.setupUi(self)

        self.ui.b_load_entry.clicked.connect(self.load_entry)
        self.ui.b_delete.clicked.connect(self.delete_entry)
        self.ui.b_cancel.clicked.connect(self.cancel)

        self.ui.journ_sel.currentTextChanged.connect(self.load_journal)

        for journal in db.get_journal_names():
            self.ui.journ_sel.addItem(journal)
        # self.load_journal(self.ui.journ_sel.itemText(0))

    def load_entry(self):
        global loaded_dream
        if self.ui.list_entries.selectedItems():

            dream_sel = self.ui.list_entries.item(self.ui.list_entries.currentRow())
            dream_number = int(dream_sel.text().split(':')[0])

            loaded_dream = db.get_from_gui(dream_number)

            self.close()

    def load_journal(self, journal_name=None):
        if not journal_name:
            journal_name = self.ui.journ_sel.currentText()

        self.ui.list_entries.clear()
        for dream in db.get_journal_by_text(journal_name):
            self.ui.list_entries.addItem(str(dream[0]) + ": " + dream[1])

    def delete_entry(self):
        confirm = QMessageBox()
        confirm.setIcon(QMessageBox.Warning)
        confirm.setWindowTitle("Delete Entry")
        confirm.setText("Are you sure you want to delete \"" + self.ui.list_entries.selectedItems()[0].text() + "\"?")
        confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirm.buttonClicked.connect(self.delete_confirm)
        confirm.exec_()

    def delete_confirm(self, button):
        dream_entry = self.ui.list_entries.selectedItems()[0].text()
        dream_id = dream_entry[0:dream_entry.find(":")]
        if button.text() == "&Yes":
            db.delete_entry(dream_id)
            self.load_journal()
        else:
            pass

    def cancel(self):
        self.close()


class SaveDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SaveEntry()
        self.ui.setupUi(self)

        self.ui.b_new_journ.clicked.connect(self.new_journ)
        self.ui.b_confirm.clicked.connect(self.confirm_save)
        self.ui.b_cancel.clicked.connect(self.cancel)

        for journal in db.get_journal_names():
            self.ui.journ_sel.addItem(journal)

        self.ui.enter_num.setText(dream_to_save[0])
        self.ui.enter_title.setText(dream_to_save[1])
        self.ui.enter_date.setText(dream_to_save[2])
        self.ui.tags_list.document().setPlainText(dream_to_save[3])

    def new_journ(self):
        new_j_dialog = NewJDialog()
        new_j_dialog.exec_()

        self.ui.journ_sel.clear()
        for journal in db.get_journal_names():
            self.ui.journ_sel.addItem(journal)

    def confirm_save(self):
        global dream_to_save
        journal = self.ui.journ_sel.currentText()

        insert_status = db.insert_from_gui(journal,
                                           self.ui.enter_num.text(),
                                           dream_to_save[1],
                                           dream_to_save[2],
                                           dream_to_save[3],
                                           dream_to_save[4]
                                           )

        save_error = QMessageBox()
        save_error.setIcon(QMessageBox.Warning)
        save_error.setWindowTitle("Save Aborted")

        if insert_status == 0:
            dream_to_save = []
            self.close()
        elif insert_status == -1:
            overwrite_box = QMessageBox()
            overwrite_box.setIcon(QMessageBox.Warning)
            overwrite_box.setWindowTitle("Overwrite Entry")
            overwrite_box.setText("Do you want to overwrite dream \"" + dream_to_save[1] + "\"?")
            overwrite_box.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
            overwrite_box.buttonClicked.connect(self.overwrite_button)
            overwrite_box.exec_()

            dream_to_save = []
            return
        elif insert_status == -2:
            save_error.setText("Dream Number must be a number!")
            save_error.exec_()
        elif insert_status == -3:
            save_error.setText("Please include some content!")
            save_error.exec_()
        elif insert_status == -4:
            save_error.setText("Please choose or create a journal.")
            save_error.exec_()

        dream_to_save = []

    def overwrite_button(self, button):
        journal = self.ui.journ_sel.currentText()
        if button.text() == "Save":
            dream_to_save[0] = self.ui.enter_num.text()
            print("overwrite dream")
            db.insert_from_gui(journal,
                               dream_to_save[0],
                               dream_to_save[1],
                               dream_to_save[2],
                               dream_to_save[3],
                               dream_to_save[4],
                               overwrite=True
                               )
            self.close()
        elif button.text() == "Cancel":
            pass

    def cancel(self):
        self.close()


class NewJDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewJournal()
        self.ui.setupUi(self)

        self.ui.b_save.clicked.connect(self.save)
        self.ui.b_cancel.clicked.connect(self.cancel)

    def save(self):
        db.add_journal(self.ui.enter_new_j.text())
        self.close()

    def cancel(self):
        self.close()


class DelJournalDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_deleteJournal()
        self.ui.setupUi(self)

        self.ui.b_delete.clicked.connect(self.delete)
        self.ui.b_cancel.clicked.connect(self.cancel)

        for journal in db.get_journal_names():
            self.ui.journal_box.addItem(journal)

    def delete(self):
        del_confirm = QMessageBox()
        del_confirm.setIcon(QMessageBox.Warning)
        del_confirm.setWindowTitle("Delete Journal?")
        del_confirm.setText("Are you sure you want to delete \"" + self.ui.journal_box.currentText()
                            + "\" and all its entries?")
        del_confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        del_confirm.buttonClicked.connect(self.delete_entry)
        del_confirm.exec_()

    def delete_entry(self, button):
        if button.text() == "&Yes":
            db.delete_journal(self.ui.journal_box.currentText())
            self.close()
        else:
            pass

    def cancel(self):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_window_main()
        self.ui.setupUi(self)

        self.ui.menu_file_new.triggered.connect(self.new_entry)
        self.ui.menu_file_save.triggered.connect(self.save_entry)
        self.ui.menu_file_load.triggered.connect(self.load_entry)
        self.ui.menu_file_exit.triggered.connect(self.exit_prgm)
        self.ui.menu_del_journal.triggered.connect(self.delete_journal)

        self.ui.b_add_tag.clicked.connect(self.add_tag)
        self.ui.b_remove_tag.clicked.connect(self.remove_tag)
        self.ui.b_delete_tags.clicked.connect(self.delete_tag)

        self.ui.enter_new_tag.returnPressed.connect(self.new_tag)

        #self.ui.enter_number.setText(str(self.get_next_id()))

        self.load_tags_list()

    def load_tags_list(self):
        """
        Load in the global tags list
        :return:
        """
        self.ui.list_tags_list.clear()
        for tag in db.get_tags():
            self.ui.list_tags_list.addItem(tag)

    def get_next_id(self):
        next_id = int(db.get_largest_id() + 1)
        return next_id

    def delete_journal(self):
        del_dialog = DelJournalDialog()
        del_dialog.exec_()

    def new_entry(self):
        """
        Erase current dream entry to make a new one
        :return:
        """

        new_box = QMessageBox()
        new_box.setIcon(QMessageBox.Warning)
        new_box.setWindowTitle("Are you sure?")
        new_box.setText("This will delete the current entry.\nDo you want to continue?")
        new_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        new_box.buttonClicked.connect(self.new_entry_confirm)
        new_box.exec_()

    def new_entry_confirm(self, button):
        global loaded_dream

        if button.text() == "&Yes":
            if loaded_dream:
                self.ui.enter_title.setText(loaded_dream[1])
                self.ui.enter_date.setText(loaded_dream[2])

                self.ui.list_entry_tags.clear()
                for tag in db.tag_str_to_list(loaded_dream[3]):
                    self.ui.list_entry_tags.addItem(tag)
                self.ui.text_entry.setText(loaded_dream[4])
            else:
                #self.ui.enter_number.setText(str(self.get_next_id()))
                self.ui.enter_title.setText("")
                self.ui.enter_date.setText("")
                self.ui.list_entry_tags.clear()
                self.ui.text_entry.setText("")

            loaded_dream = []
        elif button.text() == "&No":
            pass

    def save_entry(self):
        """
        Open save dialog
        :return:
        """
        global dream_to_save
        # self.ui.enter_number.text(), below here
        dream_to_save = [
            str(self.get_next_id()),
            self.ui.enter_title.text(),
            self.ui.enter_date.text()
        ]

        tags = []
        for tag in range(self.ui.list_entry_tags.count()):
            tags.append(self.ui.list_entry_tags.item(tag).text())
        dream_to_save.append(db.tag_list_to_str(tags))

        dream_to_save.append(self.ui.text_entry.toPlainText())

        save_dialog = SaveDialog()
        save_dialog.exec_()

    def load_entry(self):
        """
        Open load dialog
        :return:
        """
        load_dialog = LoadDialog()
        load_dialog.exec_()

        if loaded_dream:
            self.new_entry()

            #self.ui.enter_number.setText(str(loaded_dream[0]))

            #self.ui.enter_title.setText(str(loaded_dream[1]))
            #self.ui.enter_date.setText(str(loaded_dream[2]))

            #self.ui.text_entry.setText(str(loaded_dream[4]))

            #self.ui.list_entry_tags.clear()
            #for tag in db.tag_str_to_list(loaded_dream[3]):
                #self.ui.list_entry_tags.addItem(tag)

    def new_tag(self):
        """
        Create a new tag and add it to the entry
        :return:
        """
        new_tag = self.ui.enter_new_tag.text()
        db.add_tag(new_tag)

        self.load_tags_list()

        entry_tag_duplicate = False
        for i in range(self.ui.list_entry_tags.count()):
            if self.ui.list_entry_tags.item(i).text() == new_tag:
                entry_tag_duplicate = True
                break
        if not entry_tag_duplicate:
            self.ui.list_entry_tags.addItem(new_tag)
            # self.ui.list_entry_tags.sortItems()
        else:
            info_box = QMessageBox()
            info_box.setIcon(QMessageBox.Information)
            info_box.setText("Tag '" + new_tag + "' already exists!")
            info_box.setWindowTitle("Duplicate Tag Entered")
            info_box.setStandardButtons(QMessageBox.Ok)
            info_box.exec_()

        self.ui.enter_new_tag.clear()

    def add_tag(self):
        """
        Add tag to entry
        :return:
        """
        if self.ui.list_tags_list.selectedItems():
            for tag in self.ui.list_tags_list.selectedItems():
                self.ui.list_entry_tags.addItem(tag.text())

    def remove_tag(self):
        """
        Remove tag from entry
        :return:
        """
        if self.ui.list_entry_tags.selectedItems():
            for tag in self.ui.list_entry_tags.selectedItems():
                self.ui.list_entry_tags.takeItem(self.ui.list_entry_tags.row(tag))

    def delete_tag(self):
        """
        Delete tag from tag list
        :return:
        """
        if self.ui.list_tags_list.selectedItems():
            for item in self.ui.list_tags_list.selectedItems():
                db.delete_tag(item.text())

        self.load_tags_list()

    def exit_prgm(self):
        confirm_close = QMessageBox()
        confirm_close.setIcon(QMessageBox.Question)
        confirm_close.setWindowTitle("Exit?")
        confirm_close.setText("Are you sure you want to exit?\nAny unsaved work will be lost.")
        confirm_close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_close.buttonClicked.connect(self.exit_confirm)
        confirm_close.exec_()

    def exit_confirm(self, button):
        if button.text() == "&Yes":
            self.close()
        else:
            pass

    def closeEvent(self, event):
        self.exit_prgm()


# todo: add format html to gui


if __name__ == "__main__":
    # assemble the data base, and/or check if it already exists
    db.create_journ_name_table()
    db.create_dreams_table()
    db.create_tags_list()

    app = QApplication(sys.argv)
    main_win = MainWindow()

    app.setStyleSheet(
        """
        QWidget 
        { 
            background: #deaf83;
            color: #411c0f;
            selection-color: #deaf83;
            selection-background-color: #911818;
        }
        
        QPushButton { color: #911818; font: italic }
        QPushButton:hover { background: #e4bb95 }
        
        QGroupBox 
        {
            border: 1px solid #411c0f;
            margin-top: 5px;
        }
        QGroupBox:title
        {
            subcontrol-position: top left;
            top: -7px;
            left: 5px;
        }
        
        QLineEdit
        {
            border: 1px solid grey;
        }
        QLineEdit:focus
        {
            border: 1px solid #411c0f;
        }
        
        QListWidget
        {
            border: 1px solid grey;
        }
        QListWidget:focus
        {
            border: 1px solid #411c0f;
        }
        QListWidget:item:selected
        {
            background: #911818;
        }
        QListWidget:item:hover
        {
            background: #e4bb95;
        }
        QListWidget:item:selected:hover
        {
            background: #944b32;
        }
        
        QTextEdit
        {
            
        }
        QTextEdit:focus
        {
            border: 1px solid #411c0f;
        }
        
        QMenu:item:selected
        {
            color: #411c0f;
            background: #e4bb95;
        }
        
        QMenuBar:item:selected
        {
            background: #e4bb95;
        }
        """
    )

    main_win.show()
    sys.exit(app.exec_())
