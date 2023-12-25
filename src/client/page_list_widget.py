from PySide6 import QtWidgets, QtCore
from settings import IMG_DIR
from src.client.page_widget import PageWidget


class PageListWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(PageListWidget, self).__init__(parent)
        self.init_ui()
        self.show()

    def init_ui(self):
        main_layout = QtWidgets.QVBoxLayout()

        self.setLayout(main_layout)
        self.setObjectName("PageListWidget")
        self.setFixedWidth(130)

        market_widget = PageWidget(self, f"{IMG_DIR}/drugs.png", "Каталог", 1)
        cart_widget = PageWidget(self, f"{IMG_DIR}/shopping-cart.png", "Корзина", 2)

        main_layout.addWidget(market_widget)
        main_layout.addWidget(cart_widget)
        main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        main_layout.setContentsMargins(8, 10, 0, 0)
