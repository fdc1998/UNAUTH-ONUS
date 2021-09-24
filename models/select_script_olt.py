from models.fiberhome import fiberhone_old
from models.fiberhome_new_version import fiberhome_new



def select_script(olts, serial):
    for olt in olts:
        manufacturer = olt['manufacturer']
        version = olt['version']
        name = olt['name']

        if 'FIBERHOME' == manufacturer:
            versions = int(version.split('RP')[1])
            if versions > 700:
                result = fiberhome_new(olt, serial)
            else:
                result = fiberhone_old(olt, serial)

        if 'HUAWEI' == manufacturer:
            print(f'{name}-{manufacturer}')

        if 'ZTE' == manufacturer:
            print(f'{name}-{manufacturer}')


    return result
