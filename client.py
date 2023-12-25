from PySide6.QtWidgets import QApplication
import sys
from src.client.main_window import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    app.exec()

