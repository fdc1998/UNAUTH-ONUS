from models.connections import *
from models.user_model import Olt2location, Olt, Location, Users


db = dbconnect()
db.create_tables([Location, Olt, Users, Olt2location])
