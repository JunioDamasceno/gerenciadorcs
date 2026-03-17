#encoding: utf-8

import pathlib
import os
import locale

def diretorio():
    idioma = locale.getdefaultlocale()
    print(idioma)
    snap_root = os.environ.get('SNAP', '.') 
    base_path = pathlib.Path(snap_root)

    interface = ''

    if idioma == ('pt_BR', 'UTF-8'):
        print('The Language of the system is Portugese of Brazil')
        interface = next(base_path.glob('**/interface-pt-BR.glade'))

    elif idioma == ('en_US', 'UTF-8'):
        print('The language of the system is English USA')
        interface = next(base_path.glob('**/interface-en-US.glade'))
    elif idioma == ('es_ES', 'UTF-8'):
        print('The Language of the system is Spanish of Spain')
        interface = next(base_path.glob('**/interface-ES.glade'))
    else:
        interface = next(base_path.glob('**/interface-en-US.glade'))
    
    type(interface)
    print(interface)

    return(str(interface))
