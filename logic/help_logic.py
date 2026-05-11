import sys
import urllib.parse
import webbrowser
import platform
from pathlib import Path

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMessageBox
)
from PyQt5.uic import loadUi


class HelpUI(QDialog):

    def __init__(self):
        super(HelpUI, self).__init__()

        BASE_DIR = Path(__file__).resolve().parent

        ui_path = BASE_DIR.parent / "ui" / "help_page.ui"

        self.report_path = (
            BASE_DIR.parent
            / "data"
            / "complaint_report.txt"
        )

        loadUi(str(ui_path), self)

        self.pushButton.clicked.connect(self.send_help)

    def send_help(self):

        email = self.lineEdit.text()
        complaint = self.textEdit.toPlainText()

        if email.strip() == "" or complaint.strip() == "":

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("email and complaint cannot be empty")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

            return

        support_info = f"""
OS: {platform.system()}
Platform: {platform.platform()}
Python: {platform.python_version()}
Architecture: {platform.machine()}

User Email:
{email}

Complaint:
{complaint}
"""

        with open(self.report_path, "w", encoding="utf-8") as f:
            f.write(support_info)

        to_email = "keshavanvenkatesh7@gmail.com"

        subject = urllib.parse.quote(
            "Password Manager Support"
        )

        body = urllib.parse.quote(support_info)

        url = (
            "https://mail.google.com/mail/?view=cm"
            f"&fs=1&to={to_email}"
            f"&su={subject}"
            f"&body={body}"
        )

        webbrowser.open(url)

        self.lineEdit.setText("")
        self.textEdit.clear()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ui = HelpUI()
    ui.show()

    sys.exit(app.exec_())