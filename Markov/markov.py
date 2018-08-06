import numpy as np
import json
'''
x1 = np.array([0.9, 0.075, 0.025],[0.15, 0.8, 0.05],[0.25, 0.25, 0.5]])

x = x1*x1
y = np.power(x1, 3)
z = np.power(x1, 1000)
print(x)
print(y)
print(z)

p = 0.9**100000
print(p)
'''
'''
x1 = np.matrix([
    [0.8, 0.1, 0.1],
    [0.1, 0.7, 0.2],
    [0.0, 0.1, 0.9]
])
x2 = np.matrix([
    [30, 20, 50]
])

x = np.dot(x2, x1)
print(x)

x1 = np.matrix([
    [0.4, 0.2, 0.4],
    [0.15, 0.575, 0.225],
    [0.05, 0.1, 0.85]
])
x2 = np.matrix([
    [80, 15, 5]
])

x = np.dot(x2, x1)
print(x)

dic = {}
dic['lc1'] = ['k', 'l']
print(dic['lc1'])
'''

class Markov:

    def qtd_de_pessoas(lista_pessoa):

        total = len(lista_pessoa)

        return total

    def localizacao_pessoa(lista_pessoa):

        localizacao = {}
        localizacao['local_1'] = []
        localizacao['local_2'] = []
        localizacao['local_3'] = []
        for pessoa in lista_pessoa:
            if pessoa['local'] == 'local_1':
                localizacao['local_1'].append(pessoa)
            elif pessoa['local'] == 'local_2':
                localizacao['local_2'].append(pessoa)
            elif pessoa['local'] == 'local_3':
                localizacao['local_3'].append(pessoa)

        return localizacao

    def qtd_de_pessoas_em_cada_local(dicionario_locais_pessoas):

        qtd_pessoas_local = {}
        local_1 = len(dicionario_locais_pessoas['local_1'])
        qtd_pessoas_local['local_1'] = local_1
        local_2 = len(dicionario_locais_pessoas['local_2'])
        qtd_pessoas_local['local_2'] = local_2
        local_3 = len(dicionario_locais_pessoas['local_3'])
        qtd_pessoas_local['local_3'] = local_3

        return qtd_pessoas_local



    def calcular_matriz_de_transicao(qtd_pessoas_local, localizacao_pessoa_inicial_1_min, localizacao_pessoa_60_min):

        total_de_pessoas_local_1 = qtd_pessoas_local['local_1']
        total_de_pessoas_local_2 = qtd_pessoas_local['local_2']
        total_de_pessoas_local_3 = qtd_pessoas_local['local_3']

        total_a11 = total_de_pessoas_local_1
        total_a12 = 0
        total_a13 = 0
        total_a21 = 0
        total_a22 = total_de_pessoas_local_2
        total_a23 = 0
        total_a31 = 0
        total_a32 = 0
        total_a33 = total_de_pessoas_local_3

        for local, lista_pessoa in localizacao_pessoa_inicial_1_min.items():
            if local == 'local_1':
                for pessoa in lista_pessoa:
                    mac = pessoa['Peer MAC']
                    for local_60, lista_pessoa_60 in localizacao_pessoa_60_min.items():
                        if local_60 == 'local_2':
                            for pessoa_60 in lista_pessoa_60:
                                mac_60 = pessoa_60['Peer MAC']
                                if mac == mac_60:
                                    print("mac achado no 2")
                                    total_a11 -= 1
                                    total_a12 += 1
                    for local_60_2, lista_pessoa_60_2 in localizacao_pessoa_60_min.items():
                        if local_60_2 == 'local_3':
                            for pessoa_60_2 in lista_pessoa_60_2:
                                mac_60_2 = pessoa_60_2['Peer MAC']
                                if mac == mac_60_2:
                                    print("mac achado no 3")
                                    total_a11 -= 1
                                    total_a13 += 1

            elif local == 'local_2':
                for pessoa in lista_pessoa:
                    mac = pessoa['Peer MAC']
                    for local_60, lista_pessoa_60 in localizacao_pessoa_60_min.items():
                        if local_60 == 'local_1':
                            for pessoa_60 in lista_pessoa_60:
                                mac_60 = pessoa_60['Peer MAC']
                                if mac == mac_60:
                                    total_a22 -= 1
                                    total_a21 += 1
                                    
                    for local_60_2, lista_pessoa_60_2 in localizacao_pessoa_60_min.items():
                        if local_60_2 == 'local_3':
                            for pessoa_60_2 in lista_pessoa_60_2:
                                mac_60_2 = pessoa_60_2['Peer MAC']
                                if mac == mac_60_2:
                                     total_a22 -= 1
                                     total_a23 += 1

            elif local == 'local_3':
                for pessoa in lista_pessoa:
                    mac = pessoa['Peer MAC']
                    for local_60, lista_pessoa_60 in localizacao_pessoa_60_min.items():
                        if local_60 == 'local_1':
                            for pessoa_60 in lista_pessoa_60:
                                mac_60 = pessoa_60['Peer MAC']
                                if mac == mac_60:
                                    total_a33 -= 1
                                    total_a31 += 1
                    for local_60_2, lista_pessoa_60_2 in localizacao_pessoa_60_min.items():
                        if local_60_2 == 'local_2':
                            for pessoa_60_2 in lista_pessoa_60_2:
                                mac_60_2 = pessoa_60_2['Peer MAC']
                                if mac == mac_60_2:
                                     total_a33 -= 1
                                     total_a32 += 1

        a11 = total_a11/total_de_pessoas_local_1

        a12 = total_a12/total_de_pessoas_local_1

        a13 = total_a13/total_de_pessoas_local_1

        a21 = total_a21/total_de_pessoas_local_2

        a22 = total_a22/total_de_pessoas_local_2

        a23 = total_a23/total_de_pessoas_local_2

        a31 = total_a31/total_de_pessoas_local_3

        a32 = total_a32/total_de_pessoas_local_3

        a33 = total_a33/total_de_pessoas_local_3

        print(total_a11)
        print(total_a12)
        print(total_a13)
        print(total_a21)
        print(total_a22)
        print(total_a23)
        print(total_a31)
        print(total_a32)
        print(total_a33)

        print(a11)
        print(a12)
        print(a13)
        print(a21)
        print(a22)
        print(a23)
        print(a31)
        print(a32)
        print(a33)

        matriz = np.matrix([
            [a11, a12, a13],
            [a21, a22, a23],
            [a31, a32, a33],
        ])

        return matriz

arq= open('imagem.txt','r')
x = arq.read()
listaImagem = json.loads(x)
arq = open('real.txt','r')
x = arq.read()
listaReal = json.loads(x)


localizacao_imagem = Markov.localizacao_pessoa(listaImagem)
localizacao_real = Markov.localizacao_pessoa(listaReal)

print(localizacao_imagem)

qtd_pessoas_em_cada_local_imagem = Markov.qtd_de_pessoas_em_cada_local(localizacao_imagem)
print(qtd_pessoas_em_cada_local_imagem)

matriz_transicao = Markov.calcular_matriz_de_transicao(qtd_pessoas_em_cada_local_imagem, localizacao_imagem, localizacao_real)
print(matriz_transicao)

matriz_transicao_passada = matriz_transicao

array_atual = np.matrix([
    [20, 30, 50]
])

x = np.dot(array_atual, matriz_transicao_passada)
print(x)