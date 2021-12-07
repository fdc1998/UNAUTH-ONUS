import requests


def find_onu_id(serial):
    r = requests.get(f'http://172.16.254.13:8080/smo/api/onus/?serial={serial}')
    if r.status_code == 200:
        return r.json()[0]['id']
    else:
        return 'Error'

def remove_onu(id):
    r = requests.post(f'http://172.16.254.13:8080/smo/api/onus/{id}/')
    if requests.status_code == 200:
        return 'OK'
    else:
        return 'Error'
