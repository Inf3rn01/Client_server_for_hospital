from PySide6 import QtCore, QtWidgets
from src.client.register_widget import RegisterWidget
from src.client.login_widget import LoginWidget
from src.client.api.resolvers import register, login


class AuthWidget(QtWidgets.QWidget):
    login_widget: LoginWidget
    register_widget: RegisterWidget

    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super(AuthWidget, self).__init__(parent)
        self.init_ui()
        self.show()

    def init_ui(self) -> None:
        main_layout = QtWidgets.QVBoxLayout()
        input_layout = QtWidgets.QHBoxLayout()
        buttons_layout = QtWidgets.QHBoxLayout()

        self.setLayout(main_layout)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(buttons_layout)

        self.login_widget = LoginWidget(self)
        self.register_widget = RegisterWidget(self)
        login_button = QtWidgets.QPushButton("Войти")
        register_button = QtWidgets.QPushButton("Регистрация")

        input_layout.addWidget(self.login_widget)
        input_layout.addWidget(self.register_widget)
        buttons_layout.addWidget(login_button)
        buttons_layout.addWidget(register_button)

        main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        main_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setContentsMargins(0, 15, 0, 0)

        self.register_widget.hide()

        login_button.clicked.connect(self.on_login_click)
        register_button.clicked.connect(self.on_register_click)

    def on_register_click(self) -> None:
        if not self.register_widget.isVisible():
            self.login_widget.hide()
            self.register_widget.show()
            return

        if self.register_widget.password_line_edit.text() != self.register_widget.confirm_line_edit.text():
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Ошибка",
                "Пароль и подтверждение не совпадают"
            ).exec_()
            return

        if (self.register_widget.fullname_line_edit.text() == "" or self.register_widget.login_line_edit.text() == ""
                or self.register_widget.password_line_edit.text() == "" or self.register_widget.confirm_line_edit == ""):
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Ошибка",
                "Одно или несколько обязательных полей пусты"
            ).exec_()
            return

        register(
            self.register_widget.fullname_line_edit.text(),
            self.register_widget.login_line_edit.text(),
            self.register_widget.password_line_edit.text()
        )

        self.on_login_click()  # Just switch to login

        QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Information,
            "Успех",
            "Успешная регистрация"
        ).exec_()

    def on_login_click(self) -> None:
        if not self.login_widget.isVisible():
            self.login_widget.show()
            self.register_widget.hide()
            return

        session = self.parent().parent().session
        session.login(
            login_str=self.login_widget.login_line_edit.text(),
            password=self.login_widget.password_line_edit.text()
        )

        if session.error != '':
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Ошибка",
                'Неверный логин или пароль'
            ).exec_()
