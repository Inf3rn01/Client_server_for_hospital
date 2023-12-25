from src.server.database.models import *


def db_fill():
    User.create(
        fullname="Некое Имя Пользователя",
        balance=1000,
        regular=False
    )

    User.create(
        fullname="Имя Постоянного Пользователя",
        balance=3000,
        regular=True
    )

    AuthData.create(
        login="1",
        password="1",
        user_id=User.get(User.id == 1)
    )

    AuthData.create(
        login="2",
        password="2",
        user_id=User.get(User.id == 2)
    ).save()

    Staff.create(
        user_id=User.get(User.id == 1)
    )

    Product.create(
        name="Антипаскалин",
        price=100,
        count=100
    )

    Product.create(
        name="Пиво жигулёвское",
        price=36,
        count=24
    )

    UserOrder.create(
        count=1,
        user_id=User.get(User.id == 2),
        product_id=Product.get(Product.id == 2)
    )

    Discount.create(
        product_id=Product.get(Product.id == 1),
        percent=20,
        active=True
    )

    Discount.create(
        product_id=Product.get(Product.id == 2),
        percent=20,
        active=False
    )

    UserDiscount.create(
        user_id=User.get(User.id == 1),
        product_id=Product.get(Product.id == 1),
        percent=5
    )

    UserDiscount.create(
        user_id=User.get(User.id == 2),
        product_id=Product.get(Product.id == 2),
        percent=5
    )

    Storage.create(
        address="Проспект суспензии из душ, д15"
    )

    StorageOrder.create(
        product_id=Product.get(Product.id == 1),
        storage_id=Storage.get(Storage.id == 1),
        count=10
    )

    ProductInStorage.create(
        product_id=Product.get(Product.id == 1),
        storage_id=Storage.get(Storage.id == 1),
        count=1000
    )
