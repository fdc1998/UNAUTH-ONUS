from telnetlib import Telnet
import time
from enum import Enum
import re
from loguru import logger



# connect to OLT

def create_connection(olt):

    try:
        session = Telnet(host=olt['host'], port=olt['port'])
        index, match_obj, text = session.expect(["Login:".encode('latin-1')], timeout=3)

        if match_obj:
            # print("Sending username")
            session.write((olt['username'] + '\r').encode('latin-1'))


        index, match_obj, text = session.expect(["assword:".encode('latin-1')], timeout=3)

        if match_obj:
            session.write((olt['password'] + '\r').encode('latin-1'))


        logger.debug("Checking for failed login")
        index, match_obj, text = session.expect(["Login failed, incorrect username or password".encode('latin-1')],

                                                timeout=3)

        if match_obj:
            session.close()


        else:
            logger.debug("Setting terminal length")
            session.write(('terminal length 0' + '\r').encode('latin-1'))
            index, match_obj, text = session.expect(["User>".encode('latin-1')], timeout=3)


            if match_obj:
                session.write(("enable" + '\r').encode('latin-1'))


            logger.debug("Checking if someone is loged")
            index, match_obj, text = session.expect(["assword:".encode('latin-1')], timeout=3)


            if match_obj:
                session.write((olt['username'] + '\r').encode('latin-1'))
                time.sleep(1)


            index, match_obj, text = session.expect(["Admin".encode('latin-1')], timeout=2)


            if match_obj:
                return session

            else:

                False



    except Exception as e:
        logger.info("type error: {}".format(str(e)))
        session.close()


def close_connection(session):

    try:
        session.close()
        logger.info("*** Successfully logout ***")

    except:
        pass


# get SLOT, PON and onu_index of ONU

def get_onu_by_serial(session, serial):
    try:
        cmd = """show whitelist phy_addr select address {serial}""".format(serial=serial)
        session.write(("cd gpononu" + '\r').encode('latin-1'))
        index, match_obj, text = session.expect(["gpononu".encode('latin-1')], timeout=3)

        if match_obj:
            session.write(bytes(cmd + '\n', 'utf-8'))
            time.sleep(1)
            index, match_obj, text = session.expect(["gpononu".encode('latin-1')], timeout=3)


            if match_obj:
                result = session.read_very_eager().decode('latin-1')

                if 'ITEM=1' in result:
                    return True

                else:
                    return False

    except Exception as e:
        logger.info('Error getting ONU slot, pon and onu_index: {}'.format(str(e)))
        return False



# UNAUTH ONU

def deauth_onu(session, serial):

    try:
        cmd = 'set whitelist phy_addr address {serial} password null action delete'.format(serial=serial)
        session.write(("cd gpononu" + '\r').encode('latin-1'))
        index, match_obj, text = session.expect(["gpononu".encode('latin-1')], timeout=3)

        if match_obj:
            session.write(bytes(cmd + '\n', 'utf-8'))
            index, match_obj, text = session.expect(["gpononu".encode('latin-1')], timeout=3)

            if match_obj:
                result = session.read_very_eager().decode('latin-1')

                if 'whitelist' in result:
                    return True
                else:
                    return False

    except Exception as e:
        logger.info('Error deauth ONU: {}'.format(str(e)))
        return False



def fiberhone_old(olt, serial):
    session = create_connection(olt)
    if session:
        result = get_onu_by_serial(session, serial)
        if result:
            result = deauth_onu(session, serial)
            if result:
                close_connection(session)
                return True
            else:
                close_connection(session)
                return False, 'NOT REMOVE'
        else:
            close_connection(session)
            return False, 'NOT FOUND'

if __name__ == '__main__':
    fiberhone_old()


