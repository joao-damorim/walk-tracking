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

class Markov:

    def qtd_de_pessoas(self, lista_pessoa):
        total = len(lista_pessoa)
        return total

    def localizacao_pessoa(self, lista_pessoa):
        localizacao = {}
        localizacao['local_1'] = []
        localizacao['local_2'] = []
        localizacao['local_3'] = []
        for pessoa in lista_pessoa:
            if pessoa['local'] == 'local_1':
                localizacao['local_1'].append(pessoa)
            elif pessoa['local'] == 'local_2':
                localizacao['local_1'].append(pessoa)
            elif pessoa['local'] == 'local_3':
                localizacao['local_1'].append(pessoa)
        return localizacao


