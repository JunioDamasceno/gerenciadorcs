#!/usr/bin/python
# encoding: utf-8

import os
import getpass
import shutil

def verificar_arquivos():
    usuario = getpass.getuser()
    # 1. Define as bases de caminho
    # 'SNAP' aponta para a pasta restrita (onde estão os binários iniciais)
    origem_base = '/home/' + usuario + '/snap/gerenciadorcs/current/bin'
    
    # 'SNAP_USER_COMMON' aponta para a pasta de dados persistente do usuário
    snap_data = os.environ.get('SNAP_USER_COMMON', os.path.expanduser('~'))
    destino_base = os.path.join(snap_data, '.gerenciadorcs4-0')

    arquivo_antigo = ['ac.bin', 'asu.bin', 'nu.bin', 'se.bin', 'sx.bin', 'ux.bin']

    # 2. Cria a pasta de destino se não existir
    if not os.path.exists(destino_base):
        os.makedirs(destino_base)

    # 3. Processa cada arquivo
    for i in arquivo_antigo:
        caminho_origem = os.path.join(origem_base, i)
        caminho_destino = os.path.join(destino_base, i)

        # Se o arquivo já existe no destino (pasta do usuário), não fazemos nada
        if os.path.exists(caminho_destino):
            print(f'Arquivo {i} já existe no diretório atual.')
        
        # Se NÃO existe no destino, tentamos migrar da origem (pacote)
        else:
            if os.path.exists(caminho_origem):
                try:
                    # USAMOS COPY2 PARA EVITAR ERRO DE PERMISSÃO (READ-ONLY)
                    shutil.copy2(caminho_origem, caminho_destino)
                    print(f'Arquivo {i} foi migrado da versão anterior com sucesso.')
                except Exception as e:
                    print(f'Erro ao migrar {i}: {e}')

            # Se não existe em lugar nenhum, criamos um novo do zero
            else:
                print(f'O arquivo binário {i} não existe na versão anterior. Criando novo...')
                with open(caminho_destino, 'w') as f:
                    pass
                print(f'Arquivo {i} foi criado.')