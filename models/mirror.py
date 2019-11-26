from mongoengine import Document, EmbeddedDocument
from mongoengine import StringField, IntField, EmbeddedDocumentField, ListField, BooleanField

class TodoModel(EmbeddedDocument):
    name = StringField()

    time = IntField()

    important = IntField()

    check = BooleanField()


class CharModel(EmbeddedDocument):
    head = StringField(null=True)

    body = StringField(null=True)


class MirrorModel(Document):
    mirror_key = StringField(primary_key=True)

    character = EmbeddedDocumentField(CharModel)


    stuff = ListField(
        list = StringField(null=True)
    )

    name = StringField()

    exp = IntField()

    todo = ListField(
        list = EmbeddedDocumentField(TodoModel),
    )