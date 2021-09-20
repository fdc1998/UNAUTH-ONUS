from models.user_model import Olt2localidade, Localidade, Olt


def get_olt_id_from_localidade(localidade):
    id = Localidade.get(Localidade.name == localidade).id
    # olts = Olt2localidade.select(Olt2localidade.localidade_id == id)
    olts = Olt2localidade.select().where(Olt2localidade.localidade_id == id)
    for i in olts:
        print(i.olt_id)
