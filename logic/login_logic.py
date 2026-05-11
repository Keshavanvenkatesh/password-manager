import sys
import pickle
from pathlib import Path

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMessageBox
)
from PyQt5.uic import loadUi

from models.user_class import users
from logic.latest_main_logic import MainUI


class LoginUI(QDialog):

    def __init__(self):
        super(LoginUI, self).__init__()

        BASE_DIR = Path(__file__).resolve().parent

        ui_path = BASE_DIR.parent / "ui" / "login_ui.ui"

        self.data_path = BASE_DIR.parent / "data" / "user_data.txt"

        loadUi(str(ui_path), self)

        self.pushButton.clicked.connect(self.login_button)

    def login_button(self):

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if self.checkBox.isChecked():  # new user

            if len(password) < 6 or len(username) < 6:

                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(
                    "USERNAME AND PASSWORD SHOULD HAVE 6 CHARACTERS ATLEAST"
                )
                msgBox.setWindowTitle("ERROR")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

                return

            with open(self.data_path, "rb") as fr:

                user_data_list = pickle.load(fr)

                for user in user_data_list:

                    if user.username == username:

                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setText("THIS USERNAME ALREADY EXISTS")
                        msgBox.setWindowTitle("ERROR")
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec()

                        return

                user_data_list.append(users(username, password))

            with open(self.data_path, "wb") as fw:
                pickle.dump(user_data_list, fw)

            self.lineEdit.setText("")
            self.lineEdit_2.setText("")

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("sign up complete")
            msgBox.setWindowTitle("WELCOME")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        else:  # login

            with open(self.data_path, "rb") as f:

                user_data_list = pickle.load(f)

                for user in user_data_list:

                    if (
                        user.username == username
                        and user.password == password
                    ):

                        print("logged in")

                        self.window = MainUI(user)
                        self.window.show()

                        self.lineEdit.setText("")
                        self.lineEdit_2.setText("")

                        return

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid Login Credentials")
            msg.setInformativeText(
                "Please check your username or password and try again."
            )
            msg.setWindowTitle("Login Failed")

            msg.exec()

    def forgot_password_button(self):
        pass


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ui = LoginUI()
    ui.show()

    sys.exit(app.exec_())