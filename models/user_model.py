from peewee import *
from models.connections import dbconnect


class BaseModel(Model):
    class Meta:
        db = dbconnect()
        database = db


class Users(BaseModel):
    name = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()


class Location(BaseModel):
    name = CharField(unique=True)


class Olt(BaseModel):
    name = CharField(unique=True)
    manufacturer = CharField()
    version = CharField()
    protocol = CharField()
    host = CharField()
    port = CharField()
    username = CharField()
    password = CharField()
    active = BooleanField()


class Olt2location(BaseModel):
    location_id = ForeignKeyField(Location, backref='olt2location')
    olt_id = ForeignKeyField(Location, backref='olt2location')
