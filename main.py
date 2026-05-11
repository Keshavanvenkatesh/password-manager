import sys

from PyQt5.QtWidgets import QApplication

from logic.login_logic import LoginUI


app = QApplication(sys.argv)

window = LoginUI()
window.show()

sys.exit(app.exec_())