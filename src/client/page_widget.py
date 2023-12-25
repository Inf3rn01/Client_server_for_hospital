from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPixmap


class PageWidget(QtWidgets.QFrame):
    img_path: str
    title: str
    power_level: int

    def __init__(self, parent: QtWidgets.QWidget, img_path: str, title: str, power_level: int) -> None:
        super().__init__(parent)
        self.img_path = img_path
        self.title = title
        self.power_level = power_level
        self.init_ui()
        self.show()

    def init_ui(self) -> None:
        self.setFixedSize(120, 48)

        main_layout = QtWidgets.QHBoxLayout()
        pixmap_label = QtWidgets.QLabel()
        title_label = QtWidgets.QLabel()

        main_layout.addWidget(pixmap_label)
        main_layout.addWidget(title_label)

        self.setLayout(main_layout)
        pixmap_label.setFixedSize(24, 24)

        pixmap_label.setPixmap(QPixmap(self.img_path))
        pixmap_label.setScaledContents(True)
        title_label.setText(self.title)
        self.setProperty("power_level", self.power_level)

        main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def enterEvent(self, event) -> None:
        self.setStyleSheet("""
        QWidget {
            background-color: rgb(220,220,220);
            border-radius: 10px;
            }""")

    def leaveEvent(self, event) -> None:
        self.setStyleSheet("""
        QWidget {
            background-color: rgba(220,220,220, 0);
            border-radius: 10px;
            }""")
