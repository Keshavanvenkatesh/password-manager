from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys

from PyQt5.QtWidgets import QMessageBox
import urllib.parse
import webbrowser
import platform

class HelpUI(QDialog):

    def __init__(self):
        super(HelpUI, self).__init__()

        loadUi("help_page.ui", self)

        self.pushButton.clicked.connect(self.send_help)

    def send_help(self):

        email = self.lineEdit.text()
        complaint = self.textEdit.toPlainText()

        if email.strip()=="" or complaint.strip()=="":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText(f"email and complaint cannot be empty")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            return

        self.lineEdit.setText("")
        self.textEdit.clear()

        support_info = f"""
OS: {platform.system()}
Platform: {platform.platform()}
Python: {platform.python_version()}
Architecture: {platform.machine()}
Email: {email}
Complaint: {complaint}
"""
        print(support_info)

        with open("complaint report.txt","w") as f:
            f.write(support_info)
            f.close()
        
        to_email = "keshavanvenkatesh7@gmail.com"
        subject = urllib.parse.quote("Password Manager Support")

        with open("complaint report.txt","r") as f:
            lines=f.readlines()
            content=""
            for line in lines:
                content+=line
            f.close()
        
        body=complaint+content
        body = urllib.parse.quote(body)

        url = f"https://mail.google.com/mail/?view=cm&fs=1&to={to_email}&su={subject}&body={body}"
        webbrowser.open(url)
    

if __name__ == "__main__":

    app = QApplication(sys.argv)

    ui = HelpUI()
    ui.show()

    sys.exit(app.exec_())