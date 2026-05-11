from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys

class guideUI(QDialog):

    def __init__(self):
        super(guideUI, self).__init__()

        loadUi("user_guide.ui", self)
        with open("user_guide.txt","r") as f:
            contents=f.read()
            self.textEdit.setPlainText(contents)
            f.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = guideUI()
    ui.show()

    sys.exit(app.exec_())