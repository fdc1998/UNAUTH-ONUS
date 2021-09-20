from peewee import *
from models.connections import dbconnect

# create a peewee database instance -- our models will use this database to
# persist information
db = dbconnect()

class Users(Model):
    class Meta:
        database = db
        db_table = 'users'

    name = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()


class Localidade(Model):
    class Meta:
        database = db
        db_table = 'localidades'

    name = CharField(unique=True)


class Olt(Model):
    class Meta:
        database = db
        db_table = 'olts'

    name = CharField(unique=True)
    manufacturer = CharField()
    version = CharField()
    protocol = CharField()
    host = CharField()
    port = CharField()
    username = CharField()
    password = CharField()
    active = BooleanField()


class Olt2localidade(Model):
    class Meta:
        database = db
        db_table = 'oltsporlocalidade'

    localidade_id = ForeignKeyField(Localidade, backref='localidade_id')
    olt_id = ForeignKeyField(Olt, backref='olt_id')