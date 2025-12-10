import csv

def importar_backup(nome_arquivo, aux, ac, nu, se, asu):
    matriz = []
    counter = 0
    aux = bytes.fromhex(aux)
    aux = aux.decode('utf-8')
    with open('{}'.format(nome_arquivo), 'r', encoding='utf-8', newline = '') as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        for linha in leitor:
            matriz.append(linha)
    
    counter = len(matriz)
    cac = 1
    c2 = 0
    c3 = 0
    texto = ""
    
    arq_ac = open(ac, 'a+')
    while cac <= counter:
        texto = matriz[c3][c2].rstrip().replace("'", "")
        texto = texto.encode('utf-8')
        texto = texto.hex()
        arq_ac.write("{}\n".format(texto))
        cac = cac + 1
        c3 = c3 + 1
    arq_ac.seek(0)
    arq_ac.close()
    c3 = 0
    texto = ""

    cnu = 1
    c2 = 1
    while cnu <= counter:
        arq_nu = open(nu, 'a+')
        texto = matriz[c3][c2].rstrip().replace("'", "")
        texto = texto.encode('utf-8')
        texto = texto.hex()
        arq_nu.write("{}\n".format(texto))
        cnu = cnu + 1
        c3 = c3 + 1
    arq_nu.seek(0)
    arq_nu.close()
    c3 = 0
    texto = ""

    cse = 1
    c2 = 2
    while cse <= counter:
        arq_se = open(se, 'a+')
        texto = matriz[c3][c2].rstrip().replace("'", "")
        texto = texto.encode('utf-8')
        texto = texto.hex()
        arq_se.write("{}\n".format(texto))
        cse = cse + 1
        c3 = c3 + 1
    arq_se.seek(0)
    arq_se.close()
    c3 = 0
    texto = ""

    casu = 1
    while casu <= counter:
        arq_asu = open(asu, 'a+')
        texto = aux
        texto = texto.encode('utf-8')
        texto = texto.hex()
        arq_asu.write("{}\n".format(texto))
        casu = casu + 1
    arq_asu.seek(0)
    arq_asu.close()

    print("Backup importado!")