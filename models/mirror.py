from mongoengine import Document, EmbeddedDocument
from mongoengine import StringField, IntField, EmbeddedDocumentField, ListField, BooleanField

class TodoModel(EmbeddedDocument):
    name = StringField()

    time = IntField()

    important = IntField()

    check = BooleanField()


class MirrorModel(Document):
    mirror_key = StringField(primary_key=True)

    skin = StringField()

    stuff = ListField(
        list = StringField(null=True)
    )

    level = IntField()

    name = StringField()

    exp = IntField()

    money = IntField()

    todo = ListField(
        list = EmbeddedDocumentField(TodoModel),
    )