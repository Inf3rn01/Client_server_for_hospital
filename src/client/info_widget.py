from PySide6 import QtCore, QtWidgets
from src.client.auth_widget import AuthWidget


class InfoWidget(QtWidgets.QWidget):
    auth_widget: AuthWidget

    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super(InfoWidget, self).__init__(parent)
        self.init_ui()
        self.show()

    def init_ui(self) -> None:
        self.setFixedWidth(220)

        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        self.auth_widget = AuthWidget(self)

        main_layout.addWidget(self.auth_widget)

