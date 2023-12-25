from PySide6 import QtCore, QtWidgets


class RegisterWidget(QtWidgets.QWidget):
    fullname_line_edit: QtWidgets.QLineEdit
    login_line_edit: QtWidgets.QLineEdit
    password_line_edit: QtWidgets.QLineEdit
    confirm_line_edit: QtWidgets.QLineEdit

    def __init__(self, parent) -> None:
        super(RegisterWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self) -> None:
        # Init layouts

        main_layout = QtWidgets.QVBoxLayout()
        line_edit_label_layout = QtWidgets.QHBoxLayout()
        line_edit_layout = QtWidgets.QVBoxLayout()
        label_layout = QtWidgets.QVBoxLayout()

        # Init elements

        fullname_label = QtWidgets.QLabel("ФИО")
        login_label = QtWidgets.QLabel("Логин")
        password_label = QtWidgets.QLabel("Пароль")
        confirm_label = QtWidgets.QLabel("Ещё раз")
        self.fullname_line_edit = QtWidgets.QLineEdit()
        self.login_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        self.confirm_line_edit = QtWidgets.QLineEdit()

        # Setting layouts

        self.setLayout(main_layout)
        main_layout.addLayout(line_edit_label_layout)
        line_edit_label_layout.addLayout(label_layout)
        line_edit_label_layout.addLayout(line_edit_layout)
        label_layout.addWidget(fullname_label)
        label_layout.addWidget(login_label)
        label_layout.addWidget(password_label)
        label_layout.addWidget(confirm_label)
        line_edit_layout.addWidget(self.fullname_line_edit)
        line_edit_layout.addWidget(self.login_line_edit)
        line_edit_layout.addWidget(self.password_line_edit)
        line_edit_layout.addWidget(self.confirm_line_edit)
        line_edit_label_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        # Setting elements

        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        main_layout.setContentsMargins(0, 0, 0, 0)