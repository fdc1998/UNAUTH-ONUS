import os
from flask import current_app
from peewee import SqliteDatabase
import sys
import logging


def dbconnect():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
    db = SqliteDatabase(f'{ROOT_DIR}/my_app.db')
    return db

