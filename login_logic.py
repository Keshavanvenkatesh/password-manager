from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys

from PyQt5.QtWidgets import QMessageBox
import pickle
from user_class import users
from latest_main_logic import MainUI

class LoginUI(QDialog):

    def __init__(self):
        super(LoginUI, self).__init__()

        loadUi("login_ui.ui", self)

        self.pushButton.clicked.connect(self.login_button)

    def login_button(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        if self.checkBox.isChecked():       # new user
            if len(password)<6 or len(username)<6:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(f"USERNAME AND PASSWORD SHOULD HAVE 6 CHARACTERS ATLEAST")
                msgBox.setWindowTitle("ERROR")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
                return
            
            with open("user_data.txt","rb") as fr:

                user_data_list=pickle.load(fr)
                for user in user_data_list:
                    if user.username==username:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setText(f"THIS USERNAME ALREADY EXISTS")
                        msgBox.setWindowTitle("ERROR")
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        returnValue = msgBox.exec()
                        print("this username already exits")
                        return
                    
                user_data_list.append(users(username,password))

                with open("user_data.txt",'wb') as fw:
                    pickle.dump(user_data_list,fw)
                    fw.close()
                fr.close()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(f"sign up complete")
            msgBox.setWindowTitle("WELCOME")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

        else:           # login
            with open("user_data.txt",'rb') as f:
                user_data_list=pickle.load(f)
                for user in user_data_list:
                    if user.username==username and user.password==password:
                        print("logged in")
                        # open main window
                        self.window = MainUI(user)
                        self.window.show()

                        self.lineEdit.setText("")
                        self.lineEdit_2.setText("")
                        return
                    
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Invalid Login Credentials")
                msg.setInformativeText("Please check your username or password and try again.")
                msg.setWindowTitle("Login Failed")

                result = msg.exec_()
                f.close()
                return

    def forgot_password_button(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = LoginUI()
    ui.show()

    sys.exit(app.exec_())