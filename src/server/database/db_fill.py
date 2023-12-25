from src.server.database.models import *


def db_fill():
    Post.create(
        title="Хирург"
    )

    Department.create(
        title="Хирургическое"
    )

    Role.create(
        title="User"
    )

    Users.create(
        FIO="Абдуржмаев Энакентий Эдуардович",
        id_role=Role.get(id)
    )

    AuthData.create(
        login="user",
        password="user",
        user_id=Users.get(id)
    )

    Staff.create(
        id_post=Post.get(id),
        id_user=Users.get(id),
        id_department=Department.get(id)
    )

    Type_of_treatment.create(
        title="Трансплантация"
    )

    Status_request.create(
        title="Принята"
    )

    Status_request.create(
        title="Отменена"
    ).save()

    Request.create(
        add_data="11/12/23 19:23",
        id_status_req=Status_request.get(id),
        id_user=Users.get(id)
    )

    Type_of_disease.create(
        title="Наследственный"
    )

    Disease.create(
        title="Синдром Дауна",
        description="Наследственное заболевание, обусловленное трисомией по 21-й хромосоме.",
        id_type_of_disease=Type_of_disease.get(id)
    )

    Reception.create(
        id_req=Request.get(id),
        id_staff=Staff.get(id),
        id_disease=Disease.get(id),
        id_type_of_treatment=Type_of_treatment.get(id),
        description_of_treatment="Трансплантация костного мозга, также назначаются иммуноглобулины, цитостатики, антибиотик"
    )

    Treatment_status.create(
        title="Выписан"
    )

    Treatment_status.create(
        title="На больничном"
    ).save()

    Patients.create(
        id_reception=Reception.get(id),
        id_status=Treatment_status.get(id),
        data_of_discharge="26/12/23 10:00"
    )
