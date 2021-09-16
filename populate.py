import peewee
from models.user_model import *

dados = [
    {
        "host": "172.31.5.122",
        "name": "OLT-MGNET-SEDE-TUS",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.8.86",
        "name": "OLT-MGNET-SEDE-PRZ",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.7.42",
        "name": "OLT-MGNET-SEDE-SMDT ",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.5.218",
        "name": "OLT-MGNET-SEDE-ROFG",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.8.146",
        "name": "OLT-MGNET-SEDE-MXE",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.2",
        "name": "OLT-MGNET-ZUMBI-ROFG",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.6",
        "name": "OLT-MGNET-SEDE-PZA",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.17.4.254",
        "name": "OLT-MGNET-MURIU-CAY",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.5.130",
        "name": "OLT-MGNET-MXE-MRJU",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.30.254",
        "name": "OLT-SANTALUZIA/PUNAU",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.17.50.2",
        "name": "OLT-MGNET-CAICARA",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Huawei",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.5.214",
        "name": "OLT-MGNET-ENXU-QUEIMADO",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "192.168.168.10",
        "name": "OLT-MGNET-CAJUEIRO",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.38",
        "name": "OLT-DOM-MARCULINO",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "V-Solution",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.50",
        "name": "OLT-VILA-ISRAEL/ASSIS",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "V-Solution",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.70",
        "name": "OLT-MGNET-SEDE-JOA",
        "username": "mgnet",
        "localidadeid": "MUDAR",
        "password": "mgn3t1qaz",
        "manufacturer": "ZTE",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.106",
        "name": "OLT-RIACHUELO",
        "username": "SMO",
        "localidadeid": "MUDAR",
        "password": "mgn3tpr0v3d0r",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.19.0.6",
        "name": "OLT-CAY-CEN-01",
        "username": "mgnet",
        "localidadeid": "MUDAR",
        "password": "mgn3t1qaz",
        "manufacturer": "ZTE",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.54",
        "name": "OLT-CANABRAVA/BOACICA",
        "username": "",
        "localidadeid": "MUDAR",
        "password": "",
        "manufacturer": "V-SOL",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.62",
        "name": "OLT-QUEIMADAS",
        "username": "",
        "localidadeid": "MUDAR",
        "password": "",
        "manufacturer": "V-SOL",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.74",
        "name": "OLT-MGNET-TUS-ZA",
        "username": "",
        "localidadeid": "MUDAR",
        "password": "",
        "manufacturer": "V-SOL",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "172.31.11.78",
        "name": "OLT-MGNET-TUS-ART",
        "username": "",
        "localidadeid": "MUDAR",
        "password": "",
        "manufacturer": "V-SOL",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "177.73.112.134",
        "name": "OLT-MGNET-POCO-BRANCO",
        "username": "root",
        "localidadeid": "MUDAR",
        "password": "admin",
        "manufacturer": "huawei",
        "version": "RP700",
        "port": 2324,
        "protocol": "telnet"
    },
    {
        "host": "172.16.254.254",
        "name": "OLT-LLNET-STM",
        "username": "sistema",
        "localidadeid": "MUDAR",
        "password": "101203kiara",
        "manufacturer": "huawei",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "138.97.227.0",
        "name": "OLT-LLNET-PLANALTO",
        "username": "sistema",
        "localidadeid": "MUDAR",
        "password": "101203kiara",
        "manufacturer": "huawei",
        "version": "RP700",
        "port": 2326,
        "protocol": "telnet"
    },
    {
        "host": "172.31.5.98",
        "name": "OLT-PITANGUI",
        "username": "GEPON",
        "localidadeid": "MUDAR",
        "password": "GEPON",
        "manufacturer": "Fiberhome",
        "version": "RP700",
        "port": 23,
        "protocol": "telnet"
    },
    {
        "host": "128.97.227.0",
        "name": "OLT-LLNET-TRAIRAS",
        "username": "admin",
        "localidadeid": "MUDAR",
        "password": "100806",
        "manufacturer": "V-SOL",
        "version": "RP700",
        "port": 2324,
        "protocol": "telnet"
    },
    {
        "host": "128.97.227.0",
        "name": "OLT-LLNET-RETIRO-16P",
        "username": "admin",
        "localidadeid": "MUDAR",
        "password": "101203kiara",
        "manufacturer": "V-SOL",
        "version": "RP700",
        "port": 2327,
        "protocol": "telnet"
    },
    {
        "host": "128.97.227.0",
        "name": "OLT-LLNET-RETIRO-4P",
        "username": "admin",
        "localidadeid": "MUDAR",
        "password": "101203Kiara",
        "manufacturer": "V-SOL",
        "version": "RP700",
        "port": 2325,
        "protocol": "telnet"
    }
]

# data = Localidade(name="MUDAR")
# data.save()

localidadeid = Localidade.get(Localidade.name=='MUDAR').id


for d in dados:
    data = Olt(
                localidadeid=localidadeid,
                name=d['name'],
                manufacturer=d['manufacturer'],
                version=d['version'],
                protocol=d['protocol'],
                host=d['host'],
                port=d['port'],
                username=d['username'],
                password=d['password']
    )
    data.save()

