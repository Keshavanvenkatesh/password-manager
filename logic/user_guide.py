import sys
from pathlib import Path

from PyQt5.QtWidgets import (
    QApplication,
    QDialog
)
from PyQt5.uic import loadUi


class guideUI(QDialog):

    def __init__(self):
        super(guideUI, self).__init__()

        BASE_DIR = Path(__file__).resolve().parent

        ui_path = (
            BASE_DIR.parent
            / "ui"
            / "user_guide.ui"
        )

        guide_path = (
            BASE_DIR.parent
            / "data"
            / "user_guide.txt"
        )

        loadUi(str(ui_path), self)

        with open(guide_path, "r", encoding="utf-8") as f:

            contents = f.read()

            self.textEdit.setPlainText(contents)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ui = guideUI()
    ui.show()

    sys.exit(app.exec_())