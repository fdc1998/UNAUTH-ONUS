import sqlite3
from peewee import SqliteDatabase
from flask import current_app
import os


def dbconnect():
    sqlite_db = SqliteDatabase('my_app.db')
    return sqlite_db