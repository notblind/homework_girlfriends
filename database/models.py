from peewee import Model, PrimaryKeyField, CharField, IntegerField, ForeignKeyField, BooleanField, DateTimeField

from database.settings import db_handle


class Group(Model):
    id = PrimaryKeyField(null=False)

    resource_id = CharField(max_length=100)  # Id группы в вк
    name = CharField(max_length=100)  # Наименование группы
    screen_name = CharField(max_length=100)  # Краткое имя группы

    class Meta:
        database = db_handle
        db_table = "group"


class Post(Model):
    id = PrimaryKeyField(null=False)

    group = ForeignKeyField(Group, to_field="id")  # Ссылка на таблицу группу, к которой относится пост
    resource_id = CharField(max_length=100)  # Id поста в вк
    likes = IntegerField()  # Кол-во лайков
    reactions = IntegerField()  # Кол-во реакций
    views = IntegerField()  # Кол-во просмотров
    comments = IntegerField()  # Кол-во комментов
    reposts = IntegerField()  # Кол-во репостов
    text = CharField(max_length=100)  # Текст поста
    date = DateTimeField()

    has_photo = BooleanField(default=False)  # У поста есть фото
    has_video = BooleanField(default=False)  # У поста есть видео

    class Meta:
        database = db_handle
        db_table = "post"
