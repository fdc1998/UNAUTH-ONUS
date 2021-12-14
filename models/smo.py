import requests
import time

def find_onu_id(serial):
    r = requests.get(f'http://172.16.254.13:8080/smo/api/onus/?serial={serial}')
    if r.status_code == 200:
        try:
            return r.json()[0]['id']
        except:
            return 'Error'
    else:
        return 'Error'

def remove_onu(id):
    r = requests.delete(f'http://172.16.254.13:8080/smo/api/onus/{id}/')
    if requests.status_code == 200:
        return 'OK'
    else:
        return 'Error'
