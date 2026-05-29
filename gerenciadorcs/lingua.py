import locale

def lingua():
    idioma = ''
    local = locale.getdefaultlocale() #Obtém a localização/País para fins de idioma
    if local[0].startswith('pt'):
        idioma = ('pt_BR', 'UTF-8')
    if local[0].startswith('es'):
        idioma = ('es_ES', 'UTF-8')
    if local[0].startswith('en'):
        idioma = ('en_US', 'UTF-8')
    
    return(idioma)

