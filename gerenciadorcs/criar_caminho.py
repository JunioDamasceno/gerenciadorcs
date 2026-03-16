#!/usr/bin/python
# encoding: utf-8

import os
import getpass
import shutil

def verificar_arquivos():
    usuario = getpass.getuser()
    caminho_antigo = '/home/' + usuario + '/snap/gerenciadorcs/current/bin'
    snap_data = os.environ.get('SNAP_USER_DATA', os.path.expanduser('~'))

    arquivo_antigo = ['ac.bin', 'asu.bin', 'nu.bin', 'se.bin', 'sx.bin', 'ux.bin']

    if not os.path.exists(snap_data + '/.gerenciadorcs4-0'):
        os.makedirs(snap_data + '/.gerenciadorcs4-0')

    for i in arquivo_antigo:
        if not os.path.exists(caminho_antigo + '/{}'.format(i)):
            print('não existe')
            open(snap_data + '/.gerenciadorcs4-0' + '/{}'.format(i), 'w')
            print('Arquivo {} foi criado.'.format(i))
        else:
            print('existe')
            shutil.move(caminho_antigo + '/{}'.format(i), snap_data + '/.gerenciadorcs4-0' + '/{}'.format(i))
            print('O arquivo {} não foi criado porque já existe.'.format(i))
