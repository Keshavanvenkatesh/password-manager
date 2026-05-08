import pickle
from PyQt5.QtWidgets import QMessageBox

class users:
    
    users={}

    #new user
    def __init__(self,username:str,password:str):
        self.username=username
        self.password=password

        self.passwords={}
        
    #make new password
    def new_password(self,name:str,password:str):
        if name in self.passwords.keys():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText(f"THE NAME {name} ALREADY EXISTS")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)

            returnValue = msgBox.exec()

            print("this name already exists for a password")
            # show a error popup critcal messagebox
        else:
            self.passwords[name]=password

    def edit_password(self,name:str,new_password:str):

        if self.passwords.keys()==[]:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(f"NO SAVED PASSWORDS")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)

            returnValue = msgBox.exec()

        for key in self.passwords.keys():
            if key==name:
                self.passwords[key]=new_password
                return
            
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(f"INCORRECT NAME")
        msgBox.setWindowTitle("ERROR")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()

    def remove_password(self,name:str):
            
        if name in self.passwords.keys():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(f"ARE YOU SURE YOU WANT TO REMOVE PASSWORD FOR {name}?")
            msgBox.setWindowTitle("WARNING")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.passwords.pop(name)
            
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText(f"THE NAME {name} DOES NOT EXIST")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)

            returnValue = msgBox.exec()
    
    def show_all(self):
        print()
        print("PASSWORDS:")
        passwords=""
        for key in self.passwords.keys():
            passwords+=f"{key}\n \t password: {self.passwords[key]}\n"
            print(f"{key},password: {self.passwords[key]}")
        return passwords