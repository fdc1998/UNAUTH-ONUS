from peewee import *
from models.connections import dbconnect

# create a peewee database instance -- our models will use this database to
# persist information
db = dbconnect()


class Localidade(Model):
    class Meta:
        database = db
        db_table = 'localidades'

    name = CharField(unique=True)


class Olt(Model):
    class Meta:
        database = db
        db_table = 'olts'

    localidadeid = ForeignKeyField(Localidade, backref='localidadeid')
    name = CharField(unique=True)
    manufacturer = CharField()
    version = CharField()
    protocol = CharField()
    host = CharField()
    port = CharField()
    username = CharField()
    password = CharField()
