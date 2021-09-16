from models.connections import *
from models.user_model import  *


db = dbconnect()
db.create_tables([Localidade, Olt])
