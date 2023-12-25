from PySide6 import QtWidgets, QtCore
from src.client.info_widget import InfoWidget
from src.client.page_list_widget import PageListWidget
import settings
from src.client.api.session import Session


class MainWindow(QtWidgets.QWidget):
    session: Session = Session()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

        if self.session.server_available:
            self.show()
        else:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Ошибка",
                'Сервер недоступен'
            ).exec_()
            exit()

    def init_ui(self):
        self.setWindowTitle("PharmacyEnt App")
        self.resize(940, 620)

        # Init layouts

        main_h_layout = QtWidgets.QHBoxLayout()

        # Init widgets

        page_list_widget = PageListWidget(self)
        content_widget = QtWidgets.QWidget()
        info_widget = InfoWidget(self)

        # Settings layouts

        self.setLayout(main_h_layout)
        main_h_layout.addWidget(page_list_widget)
        main_h_layout.addWidget(content_widget)
        main_h_layout.addWidget(info_widget)
        main_h_layout.setContentsMargins(0, 0, 0, 0)

        # Settings widgets

        info_widget.setObjectName("infoWidget")
        content_widget.setObjectName("contentWidget")

        self.setStyleSheet("""
            #contentWidget{
                border-right: 2px solid rgb(192,192,192);
                border-left: 2px solid rgb(192,192,192);
            }
        """)

        content_widget.setMinimumSize(300, 400)

