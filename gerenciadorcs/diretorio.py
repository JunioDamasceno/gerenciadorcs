#encoding: utf-8

import pathlib
import os
import locale

def diretorio():
    idioma = ''
    local = locale.getdefaultlocale()
    if local[0].startswith('pt'):
        idioma = ('pt_BR', 'UTF-8')
    if local[0].startswith('es'):
        idioma = ('es_ES', 'UTF-8')
    if local[0].startswith('en'):
        idioma = ('en_US', 'UTF-8')


    snap_root = os.environ.get('SNAP', '.') 
    base_path = pathlib.Path(snap_root)

    interface = ''

    if idioma == ('pt_BR', 'UTF-8'):
        print('The Language of the Gerenciador CS is Portugese of Brazil')
        interface = next(base_path.glob('**/interface-pt-BR.glade'))

    elif idioma == ('en_US', 'UTF-8'):
        print('The language of the Gerenciador CS is English USA')
        interface = next(base_path.glob('**/interface-en-US.glade'))
    elif idioma == ('es_ES', 'UTF-8'):
        print('The Language of the Gerenciador CS is Spanish of Spain')
        interface = next(base_path.glob('**/interface-ES.glade'))
    else:
        print('The language of the Gerenciador CS is English USA')
        interface = next(base_path.glob('**/interface-en-US.glade'))
    
    type(interface)

    return(str(interface))
