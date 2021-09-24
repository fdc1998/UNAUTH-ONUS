from models.user_model import Olt, Location, Olt2location

# dados = ["OLT-TUS-MGNET-CENTRO;FIBERHOME;RP700;TELNET;23;172.31.5.122;GEPON;GEPON;SIM",
#          "OLT-TUS-CIANET-CENTRO;FIBERHOME;RP1000;TELNET;23;172.31.11.142;GEPON;GEPON;SIM",
#          "OLT-TUS-MGNET-CAJOEIRO;FIBERHOME;RP700;TELNET;23;192.168.168.10;GEPON;GEPON;SIM",
#          "OLT-SMG-MGNET-CENTRO;FIBERHOME;RP700;TELNET;23;172.31.7.42;GEPON;GEPON;SIM",
#          "OLT-SMG-CIANET-CENTRO-01;FIBERHOME;RP1000;TELNET;23;172.31.11.122;GEPON;GEPON;SIM",
#          "OLT-SMG-CIANET-CENTRO-02;FIBERHOME;RP700;TELNET;23;172.31.11.150;GEPON;GEPON;SIM",
#          "OLT-PG-MGNET-ENXU;FIBERHOME;RP700;TELNET;23;172.31.5.214;GEPON;GEPON;SIM",
#          "OLT-PRZ-MGNET-CENTRO;FIBERHOME;RP700;TELNET;23;172.31.8.86;GEPON;GEPON;SIM",
#          "OLT-PBR-CIANET-CENTRO;FIBERHOME;RP1000;TELNET;23;172.31.11.130;GEPON;GEPON;SIM",
#          "OLT-CAY-MGNET-MURIU;FIBERHOME;RP700;TELNET;23;172.17.4.254;GEPON;GEPON;SIM",
#          "OLT-EXT-MGNET-PITANGUI;FIBERHOME;RP700;TELNET;23;172.31.5.98;GEPON;GEPON;SIM",
#          "OLT-MXP-MGNET-CENTRO;FIBERHOME;RP700;TELNET;23;172.31.8.146;GEPON;GEPON;SIM",
#          "OLT-MXP-MGNET-MARACAJAU;FIBERHOME;RP700;TELNET;23;172.31.5.130;GEPON;GEPON;SIM",
#          "OLT-RFOG-MGNET-ZUMBI;FIBERHOME;RP700;TELNET;23;172.31.11.2;GEPON;GEPON;SIM",
#          "OLT-RFOG-MGNET-CENTRO;FIBERHOME;RP700;TELNET;23;172.31.5.218;GEPON;GEPON;SIM",
#          "OLT-TUS-MGNET-SANTA-LUZIA;FIBERHOME;RP700;TELNET;23;172.31.30.254;GEPON;GEPON;SIM",
#          "OLT-MXP-CIANET-DOM-MARCULINO;FIBERHOME;RP700;TELNET;23;172.31.11.30;GEPON;GEPON;SIM",
#          "OLT-PZA-MGNET-CENTRO;FIBERHOME;RP700;TELNET;23;172.31.11.6;GEPON;GEPON;SIM",
#          "OLT-RHE-MGNET-CENTRO;FIBERHOME;RP700;TELNET;23;172.31.11.106;GEPON;GEPON;SIM",
#          "OLT-PG-ONLINE-CENTRO;HUAWEI;;TELNET;23887;45.167.60.1;sgpsgp;sgp142536;SIM",
#          "OLT-CCRA-MGNET;HUAWEI;;TELNET;23;172.17.50.2;;;SIM",
#          "OLT-CCRA-ONLINE;HUAWEI;;TELNET;23888;45.167.60.1;sgpsgp;sgphw18;SIM",
#          "OLT-PRZ-CIANET-CENTRO;HUAWEI;;TELNET;23;172.31.11.146;sgpuser;123@sgp;NÃO",
#          "OLT-JOA-CIANET-QUEIMADAS;HUAWEI;;TELNET;23;;;;SIM",
#          "OLT-JOA-CIANET-CENTRO;HUAWEI;;TELNET;23;172.16.19.4;digicontrol;123@mudar;SIM",
#          "OLT-PBR-MGNET-CENTRO;HUAWEI;;TELNET;23;172.19.0.2;root;admin;SIM",
#          "OLT-TPU-CIANET-CENTRO;HUAWEI;;TELNET;23;172.31.11.134;SGPSGP;123@SGP;SIM",
#          "OLT-TUS-CIANET-BOA-CICA;HUAWEI;;TELNET;23;172.31.11.114;sgpsgp;123@mudar;SIM",
#          "OLT-SMT-MGNET-CENTRO;HUAWEI;;TELNET;2338;138.97.224.54;sistema;101203kiara;SIM",
#          "OLT-NTL-MGNET-PLANALTO;HUAWEI;;TELNET;2326;138.97.224.54;sistema;101203kiara;SIM",
#          "OLT-JOA-MGNET-CENTRO;ZTE;;TELNET;23;172.31.1170;mgnet;mgn3t1qaz;SIM"]
#
# for d in dados:
#     d = d.split(';')
#
#     if d[8] == 'SIM':
#         active = 1
#     else:
#         active = 0
#
#     data = Olt(
#         name=d[0],
#         manufacturer=d[1],
#         version=d[2],
#         protocol=d[3],
#         host=d[5],
#         port=d[4],
#         username=d[6],
#         password=d[7],
#         active=active
#     )
#     data.save()
# #
dados = ["OLT-TUS-MGNET-CENTRO;TOUROS-CENTRO;CARNAUBINHA;LAGOA_DO_SAL", "OLT-TUS-CIANET-CENTRO;TOUROS-CENTRO",
         "OLT-TUS-MGNET-CAJOEIRO;CAJOEIRO;KM-0;LAGOA_DO_SAL",
         "OLT-SMG-MGNET-CENTRO;SÃO_MIGUEL-CENTRO;MONTE_ALEGRE;SÃO_JOSE",
         "OLT-SMG-CIANET-CENTRO;SÃO_MIGUEL-CENTRO;MONTE_ALEGRE;SÃO_JOSE;VILA_MAYNE;BAIXA_DO_QUINQUIN;VILA_ASSIS",
         "OLT-PG-MGNET-ENXU;ENXU;BARREIROS", "OLT-PG-ONLINE-CENTRO;PEDRA_GRANDE", "OLT-CCRA-MGNET;CAICARA",
         "OLT-CCRA-ONLINE;CAICARA", "OLT-PRZ-MGNET-CENTRO;PARAZINHO;PEDRA_GRANDE", "OLT-PRZ-CIANET-CENTRO;PARAZINHO",
         "OLT-JOA-CIANET-QUEIMADAS;QUEIMADAS", "OLT-JOA-CIANET-CENTRO;JOAO_CAMARA", "OLT-JOA-MGNET-CENTRO;JOAO_CAMARA",
         "OLT-PBR-MGNET-CENTRO;POCO_BRANCO", "OLT-PBR-CIANET-CENTRO;POCO_BRANCO;CONTADOR",
         "OLT-TPU-CIANET-CENTRO;TAIPU", "OLT-CAY-MGNET-MURIU;MURIU;JACUMA;CAIANA", "OLT-EXT-MGNET-PITANGUI;PITANGUI",
         "OLT-MXP-MGNET-CENTRO;MAXARANGUAPE;CARAUBAS;ANINGAS", "OLT-MXP-MGNET-MARACAJAU;MARACAJAU",
         "OLT-RFOG-MGNET-ZUMBI;ZUMBI;PITITINGA", "OLT-RFOG-MGNET-CENTRO;RIO_DO_FOGO;PEROBAS",
         "OLT-TUS-MGNET-SANTA-LUZIA;SANTA_LUZIA;PUNAU",
         "OLT-TUS-CIANET-BOA-CICA;BOA_CICA;CANA_BRAVA;CARNAUBAU;BOQUEIRA",
         "OLT-MXP-CIANET-DOM-MARCULINO;DOM_MARCULINO;PUNAU", "OLT-PZA-MGNET-CENTRO;PUREZA;OLHO_DAGUA",
         "OLT-RHE-MGNET-CENTRO;RIACHUELO", "OLT-SMT-MGNET-CENTRO;SANTA_MARIA",
         "OLT-NTL-MGNET-PLANALTO;PLANALTO;MANGABEIRA"]

# listalocalidades = []
# for d in dados:
#     d = d.split(';')
#     # d = d.pop(0)
#     for l in d[1:]:
#         if l != '':
#             if l not in listalocalidades:
#                 listalocalidades.append(l)
#
# for l in listalocalidades:
#     data = Location(
#         name=l
#     )
#     data.save()
#
# #
olts = list(Olt.select().dicts())
result = list(Location.select().dicts())


for d in dados:
    d = d.split(';')
    oltname = d[0]
    for localidade in d[1:]:
        for i in result:
            localidade == i['name']
            if localidade == i['name']:
                localidadeid = i['id']
                for o in olts:
                    oltname = o['name']
                    if oltname == o['name']:
                        oltid = o['id']
                print(f'{localidade}-{oltname}')

        # data = Olt2location(
        #     location_id=localidadeid,
        #     olt_id=oltid
        # )
        # data.save()
#
# for r in result:
#     localidadename = r['name']
#     localidadeid = r['id']
#     for d in dados:
#         if localidadename in d:
#             oltname = d.split(';')[0]
#             for olt in olts:
#                 if olt['name'] == oltname:
#                     oltid = olt['id']
#                     data = Olt2localidade(
#                                    localidade_id = localidadeid,
#                                     olt_id = oltid
#                             )
#                     data.save()
