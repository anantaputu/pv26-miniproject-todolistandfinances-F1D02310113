import os
import sys

from PySide6.QtWidgets import QApplication

from app.config import STYLE_PATH
from app.controllers.main_controller import MainController


def load_stylesheet() -> str:
    if not os.path.exists(STYLE_PATH):
        return ""
    with open(STYLE_PATH, "r", encoding="utf-8") as file:
        return file.read()


def main() -> int:
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet())

    controller = MainController()
    controller.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
