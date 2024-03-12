import peewee

from odv import enum


database_connection = peewee.Proxy()


class BaseModel(peewee.Model):
    class Meta:
        database = database_connection


class Account(BaseModel):
    username = peewee.TextField(primary_key=True, index=True, unique=True)
    password = peewee.TextField(unique=True, default="")
    email = peewee.TextField(default="")

    plain = peewee.TextField(default="")
    secure = peewee.TextField(default="")
    
    salt = peewee.TextField(default="")
    nonce = peewee.TextField(default="")


def change_database_to(database: peewee.Database, create_tables: bool | None = False):
    database_connection.initialize(database)

    if create_tables:
        database.create_tables([
            Account
        ])