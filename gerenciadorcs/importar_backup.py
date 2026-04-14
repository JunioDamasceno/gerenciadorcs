import csv

def importar_backup(nome_arquivo, aux, ac, nu, se, asu, tabela_ux):
    matriz = [] #matriz limpa onde os dados do arquivo de importação .csv tratados e importados para os binários
    tab_atual = tabela_ux #recebe a lista atual do usuário para comparação com o arquivo de backup

    #Armazena os dados do arquivo de backup .csv na variável matriz
    with open('{}'.format(nome_arquivo), 'r', encoding='utf-8', newline = '') as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        for linha in leitor:
            matriz.append(linha)
    
    #contadores para os loops/repeticções do While
    cta0 = 0
    ctm = 0
    ctac = len(tab_atual) - 1 
    ctmc = len(matriz) - 1
    cor = 0
    cor1 = 0

    tab_atual_formatada = [] #matriz temporária para transformar a tupla da variável tab_atual em lista
    #Transforma a tupla da variável tab_atual em lista
    for tupla in tab_atual:
        nova_tupla = tuple(f"'{campo}'" for campo in tupla)
        tab_atual_formatada.append(nova_tupla)
    
    #limpa a variável tab_atual e armazena nela o dados da variável tab_atual_formatada
    tab_atual = tab_atual_formatada

    tab_atual_lista = [] #matriz temporária para adicionar as aspas adiciionais na string dos dados da tab_atual
    #Há um problema com as aspas das strings da matriz tab_atual aqui adiciona as aspas
    for tupla in tab_atual:
        linha = [f"{elem}" for elem in tupla]  # Adiciona aspas extras
        tab_atual_lista.append(linha)

    #limpa a variável tab_atual e armazena nela o dados da variável tab_atual_lista
    tab_atual = tab_atual_lista

    #remove espaçoes extras do início e do fim de cada string da variável matriz
    while cor <= ctmc:
        matriz[cor][0] = matriz[cor][0].strip()
        matriz[cor][1] = matriz[cor][1].strip()
        matriz[cor][2] = matriz[cor][2].strip()
        cor = cor + 1
    
    #remove espaçoes extras do início e do fim de cada string da variável tab_atual
    while cor1 <= ctac:
        tab_atual[cor1][0] = tab_atual[cor1][0].strip()
        tab_atual[cor1][1] = tab_atual[cor1][1].strip()
        tab_atual[cor1][2] = tab_atual[cor1][2].strip()
        cor1 = cor1 + 1

    #matriz temporária para armazenar somente os dados não duplicados na variável matriz e tab_atual
    matriz2 = []
    
    #Este loop compara os dados de cada linha e coluna da variável matriz com cada linha e coluna da variável tab_atual
    #Busca duplicidades, as duplicidades não podem ser importadas (Ex.: o Usuário ter inserido  cadastro que também contém no backup dele)
    while ctm <= ctmc:
        encontrado = False
        while cta0 <= ctac:
            if matriz[ctm][0].strip() == tab_atual[cta0][0] and matriz[ctm][1] == tab_atual[cta0][1] and matriz[ctm][2] == tab_atual[cta0][2]:
                encontrado = True
                break
            cta0 = cta0 + 1
        if not encontrado:
            matriz2.append(matriz[ctm])
        cta0 = 0
        ctm = ctm + 1
    
    #Os dados foram tratados e agora a variável matriz2 contém somente os dsdos não duplicado
    #limpa a variável matriz e armazena nela o dados da variável matriz2
    matriz = matriz2

    #recebe o nome do usuário que está importando os dados
    aux = bytes.fromhex(aux)
    aux = aux.decode('utf-8')

    #contador
    counter = 0
    #Condição para executar esta parte do código somente se tiver algum dado na variável "matriz"
    if matriz != []: # Se a matriz não for vazia, ou seja, há dados a serem importados, então a importação é criptografada e feita nos arquivos binários
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
     
        return(True) #Ao fim da importação retorna True, isto serve para o programa sinalizar para o usuário que os dados foram importados
    else:
        return(False) # Caso não tenham dados a serem importados, (ex. tudo for duplicado) ele retorna False para o programa sinalizar que os dados não foram importado porque estão duplicados nos binários do programa e no arquivo de backup .csv