from peewee import Model, PrimaryKeyField, CharField, IntegerField, ForeignKeyField, BooleanField

from database.settings import db_handle


class Group(Model):
    id = PrimaryKeyField(null=False)

    resource_id = CharField(max_length=100)
    name = CharField(max_length=100)
    screen_name = CharField(max_length=100)

    class Meta:
        database = db_handle
        db_table = "group"


class Post(Model):
    id = PrimaryKeyField(null=False)

    group = ForeignKeyField(Group, to_field="id")
    resource_id = CharField(max_length=100)
    likes = IntegerField()
    reactions = IntegerField()
    views = IntegerField()
    comments = IntegerField()
    reposts = IntegerField()
    text = CharField(max_length=100)

    has_photo = BooleanField(default=False)
    has_video = BooleanField(default=False)

    class Meta:
        database = db_handle
        db_table = "post"
