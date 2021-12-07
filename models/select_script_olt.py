import time
from models.fiberhome import fiberhone_old
from models.fiberhome_new_version import fiberhome_new
from models.huawei import huawei
from flask import Flask, redirect, url_for, render_template, request, abort, flash


def select_script(olts, serial):
    results = []
    for olt in olts:
        manufacturer = olt['manufacturer']
        version = olt['version']
        name = olt['name']

        if 'FIBERHOME' == manufacturer and len(serial) == 12:
            versions = int(version.split('RP')[1])
            if versions > 700:
                # time.sleep(2)
                # return True, serial
                result = fiberhome_new(olt, serial)

            else:
                # time.sleep(2)
                # return True, serial
                result = fiberhone_old(olt, serial)

        if 'HUAWEI' == manufacturer:
            result = huawei(olt, serial)

        if 'ZTE' == manufacturer:
            print(f'{name}-{manufacturer}')

        results.append([name, result])

    return results
