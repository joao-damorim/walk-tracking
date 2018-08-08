import numpy as np

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
'''
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

class Markov:

    def qtd_de_pessoas(self, lista_pessoa):

        total = len(lista_pessoa)

        return total

    def localizacao_pessoa(self, lista_pessoa):

        localizacao = {}
        localizacao['local_1'] = []
        localizacao['local_2'] = []
        for pessoa in lista_pessoa:
            if pessoa['local'] == 'local_1':
                localizacao['local_1'].append(pessoa)
            elif pessoa['local'] == 'local_2':
                localizacao['local_2'].append(pessoa)

        return localizacao

    def qtd_de_pessoas_em_cada_local(self, dicionario_locais_pessoas):

        qtd_pessoas_local = {}
        local_1 = len(dicionario_locais_pessoas['local_1'])
        qtd_pessoas_local['local_1'] = local_1
        local_2 = len(dicionario_locais_pessoas['local_2'])
        qtd_pessoas_local['local_2'] = local_2

        return qtd_pessoas_local

    def calcular_matriz_de_transicao(self, qtd_pessoas_local, localizacao_pessoa_inicial_1_min, localizacao_pessoa_60_min):

        total_de_pessoas_local_1 = qtd_pessoas_local['local_1']
        total_de_pessoas_local_2 = qtd_pessoas_local['local_2']

        total_a11 = total_de_pessoas_local_1
        total_a12 = 0
        total_a21 = 0
        total_a22 = total_de_pessoas_local_2

        for local, lista_pessoa in localizacao_pessoa_inicial_1_min.items():
            if local == 'local_1':
                for pessoa in lista_pessoa:
                    mac = pessoa['MAC']
                    for local_60, lista_pessoa_60 in localizacao_pessoa_60_min.items():
                        if local_60 == 'local_2':
                            for pessoa_60 in lista_pessoa_60:
                                mac_60 = pessoa_60['MAC']
                                if mac == mac_60:
                                   total_a11 -= 1
                                   total_a12 += 1

            elif local == 'local_2':
                for pessoa in lista_pessoa:
                    mac = pessoa['MAC']
                    for local_60, lista_pessoa_60 in localizacao_pessoa_60_min.items():
                        if local_60 == 'local_1':
                            for pessoa_60 in lista_pessoa_60:
                                mac_60 = pessoa_60['MAC']
                                if mac == mac_60:
                                    total_a22 -= 1
                                    total_a21 += 1


        a11 = total_a11/total_de_pessoas_local_1

        a12 = total_a12/total_de_pessoas_local_1

        a21 = total_a21/total_de_pessoas_local_2

        a22 = total_a22/total_de_pessoas_local_2

        matriz = np.matrix([
            [a11, a12],
            [a21, a22],
        ])

        return matriz