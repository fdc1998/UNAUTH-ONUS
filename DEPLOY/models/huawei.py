import time
from telnetlib import Telnet
from loguru import logger


def connect_olt(olt):
    try:
        logger.info(f'Checando conexão com a OLT')
        tn = Telnet(host=olt['host'], port=olt['port'], timeout=5)

        index, match_obj, text = tn.expect(["name:".encode('latin-1')], timeout=5)
        logger.info('Estabelecendo conexão com: ' + olt['name'])
        if match_obj:
            tn.write((olt['username'] + '\r').encode('latin-1'))

        index, match_obj, text = tn.expect(["assword:".encode('latin-1')], timeout=5)
        if match_obj:
            tn.write((olt['password'] + '\r').encode('latin-1'))

        index, match_obj, text = tn.expect([">".encode('latin-1')], timeout=5)
        if match_obj:
            tn.write(('enable' + '\r').encode('latin-1'))

        index, match_obj, text = tn.expect(["#".encode('latin-1')], timeout=5)
        if match_obj:
            tn.write(('config' + '\r').encode('latin-1'))

        index, match_obj, text = tn.expect(["config".encode('latin-1')], timeout=5)
        if match_obj:
            return tn

    except Exception as e:
        logger.error("type error: {}".format(str(e)))
        logger.error('A Conexão não foi estabelecida.')


def close_connection(tn):
    try:
        tn.close()
        logger.info("*** Successfully logout ***")

    except:
        pass


def find_onu(tn, serial_onu):
    try:
        index, match_obj, text = tn.expect(["config".encode('latin-1')], timeout=5)
        if match_obj:
            tn.write((f'display ont info by-sn {serial_onu}' + '\r\r').encode('latin-1'))

        index, match_obj, text = tn.expect(["Q".encode('latin-1')], timeout=5)

        if match_obj:
            saida = text.decode('latin-1').splitlines()

            for a in saida:
                if 'F/S/P' in a:
                    a = a.strip()
                    a = a.split(':')
                    a = a[1].strip().split('/')
                    frame = a[0]
                    slot = a[1]
                    pon = a[2]
                if 'ONT-ID' in a:
                    a = a.strip()
                    a = a.split(':')
                    ont_id = a[1].strip()

            # logger.info(f'F/S/P = {frame}/{slot}/{pon}  Ont-id: {ont_id}')

        else:
            logger.info('ONU não encontrada')
            return False

        tn.write(('q' + '\r').encode('latin-1'))
        index, match_obj, text = tn.expect(["(config)".encode('latin-1')], timeout=5)

        if match_obj:
            return [frame, slot, pon, ont_id]

    except Exception as e:
        logger.error("type error: {}".format(str(e)))
        tn.close()


def delete_service_port(tn, onuinfo):
    try:
        frame = onuinfo[0]
        slot = onuinfo[1]
        pon = onuinfo[2]
        ont_id = onuinfo[3]

        logger.info('Procurando o Service-port da ONU')

        tn.write((f'display service-port port {frame}/{slot}/{pon} ont {ont_id}' + '\r\r').encode('latin-1'))

        index, match_obj, text = tn.expect(["Total".encode('latin-1')], timeout=5)

        if match_obj:
            saida = text.decode('latin-1').splitlines()

            for b in saida:
                if 'common' in b:
                    b = b.strip()
                    b = b.split()
                    service_port = b[0]
                    logger.info(f'Index do service-port: {service_port}')
                    tn.write((f'undo service-port {service_port}' + '\r').encode('latin-1'))
                    return True
        else:
            logger.info('Service-port não encontrado.')
            return True

    except Exception as e:
        logger.error("type error: {}".format(str(e)))
        return False

def delete_onu(tn, onuinfo):
    try:
        frame = onuinfo[0]
        slot = onuinfo[1]
        pon = onuinfo[2]
        ont_id = onuinfo[3]

        logger.info('Removendo ONU...')
        tn.write((f'interface gpon {frame}/{slot}' + '\r').encode('latin-1'))
        index, match_obj, text = tn.expect([f"gpon".encode('latin-1')], timeout=5)

        if match_obj:
            tn.write((f'ont delete {pon} {ont_id}' + '\r').encode('latin-1'))
            index, match_obj, text = tn.expect(["success".encode('latin-1')], timeout=5)
            if match_obj:
                logger.info('ONU Removida!')
                return True
            else:
                logger.error('Falha ao remover ONU')
                return False

    except Exception as e:
        logger.error("type error: {}".format(str(e)))
        tn.close()


def huawei(olt, serial_onu):
    cont = 0
    onudelete = False
    tn = connect_olt(olt)
    if tn:
        onuinfo = find_onu(tn, serial_onu)
        if onuinfo:
            while not onudelete and cont < 2:
                cont += 1
                srvdelete = delete_service_port(tn, onuinfo)

                if srvdelete:
                    onudelete = delete_onu(tn, onuinfo)

                    if not onudelete:
                        close_connection(tn)
                        return True

                
            close_connection(tn)
            return False

        else:
            close_connection(tn)
            return False


if __name__ == '__main__':
    fiberhone_old()
