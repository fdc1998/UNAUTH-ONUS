from models.user_model import Olt, Location, Olt2location


def get_olt_id_from_localidade(local):
    listolts = []
    id = Location.get(Location.name == local)
    olts = list(Olt2location.select().where(Olt2location.location_id == id).dicts())
    for i in olts:
        listolts.append(list(Olt.select().where(Olt.id == i['olt_id']).dicts())[0])

    return listolts
