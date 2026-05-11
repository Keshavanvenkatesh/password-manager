from pathlib import Path
import pickle
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)
from PyQt5.uic import loadUi

from models.user_class import users
from logic.help_logic import HelpUI
from logic.user_guide import guideUI


class MainUI(QMainWindow):

    def __init__(self, user: users):
        super(MainUI, self).__init__()

        BASE_DIR = Path(__file__).resolve().parent

        ui_path = BASE_DIR.parent / "ui" / "latest_main_ui_2.ui"

        self.data_path = BASE_DIR.parent / "data" / "user_data.txt"

        loadUi(str(ui_path), self)

        self.current_user = user

        self.pushButton_4.clicked.connect(self.new_password)
        self.pushButton_3.clicked.connect(self.edit_password)

        self.pushButton_6.clicked.connect(self.remove_password)
        self.pushButton.clicked.connect(self.show_passwords)

        self.pushButton_2.clicked.connect(self.clear_screen)

        self.actionhelp_page.triggered.connect(self.help)
        self.actionguide.triggered.connect(self.user_guide)

    def new_password(self):

        name = self.lineEdit_10.text()
        password = self.lineEdit_11.text()

        if name.strip() == "" or password.strip() == "":

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("these fields cannot be empty")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

            return

        self.current_user.new_password(name, password)

        with open(self.data_path, "rb") as f:

            user_data_list = pickle.load(f)

            for i, user in enumerate(user_data_list):

                if (
                    user.username == self.current_user.username
                    and user.password == self.current_user.password
                ):
                    user_data_list[i] = self.current_user

        with open(self.data_path, "wb") as fw:
            pickle.dump(user_data_list, fw)

        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")

    def edit_password(self):

        name_to_edit = self.lineEdit_9.text()
        new_password = self.lineEdit_8.text()

        if name_to_edit.strip() == "" or new_password.strip() == "":

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("these fields cannot be empty")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

            return

        self.current_user.edit_password(name_to_edit, new_password)

        with open(self.data_path, "rb") as f:

            user_data_list = pickle.load(f)

            for i, user in enumerate(user_data_list):

                if (
                    user.username == self.current_user.username
                    and user.password == self.current_user.password
                ):
                    user_data_list[i] = self.current_user

        with open(self.data_path, "wb") as fw:
            pickle.dump(user_data_list, fw)

        self.lineEdit_9.setText("")
        self.lineEdit_8.setText("")

    def remove_password(self):

        name_to_remove = self.lineEdit_16.text()

        if name_to_remove.strip() == "":

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("this field cannot be empty")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

            return

        self.current_user.remove_password(name_to_remove)

        with open(self.data_path, "rb") as f:

            user_data_list = pickle.load(f)

            for i, user in enumerate(user_data_list):

                if (
                    user.username == self.current_user.username
                    and user.password == self.current_user.password
                ):
                    user_data_list[i] = self.current_user

        with open(self.data_path, "wb") as fw:
            pickle.dump(user_data_list, fw)

        self.lineEdit_16.setText("")

    def show_passwords(self):

        passwords = self.current_user.show_all()

        if passwords == "":
            self.textEdit.setPlainText("NO PASSWORDS SAVED")

        else:
            self.textEdit.setPlainText(passwords)

    def clear_screen(self):

        self.textEdit.setText("")

    def help(self):

        self.help_window = HelpUI()
        self.help_window.show()

    def user_guide(self):

        self.user_guide_window = guideUI()
        self.user_guide_window.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    dummy_user = users("test", "123456")

    ui = MainUI(dummy_user)
    ui.show()

    sys.exit(app.exec_())