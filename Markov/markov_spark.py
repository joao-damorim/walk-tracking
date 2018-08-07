# ADVICE: With PyDev, take care about unused imports (and also unused variables),
# please comment them all, otherwise you will get any errors at the execution.
# Note that even the trick like the directives @PydevCodeAnalysisIgnore and
# @UnusedImport will never solve that issue.

# Imports the PySpark libraries
from pyspark import SparkConf, SparkContext

# The 'os' library allows us to read the environment variable SPARK_HOME defined in the IDE environment
import os
import numpy as np
import json

# Configure the Spark context to give a name to the application
sparkConf = SparkConf().setAppName("WordCount")
sc = SparkContext(conf=sparkConf)

# The text file containing the words to count (this is the Spark README file)
textFile = sc.textFile(os.environ["SPARK_HOME"] + "/README.md")

# The code for counting the words (note that the execution mode is lazy)
# Uses the same paradigm Map and Reduce of Hadoop, but fully in memory
wordCounts = textFile.flatMap(lambda line: line.split()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)


# Executes the DAG (Directed Acyclic Graph) for counting and collecting the result
# for wc in wordCounts.collect(): print wc


class Markov():

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
                localizacao['local_2'].append(pessoa)
            elif pessoa['local'] == 'local_3':
                localizacao['local_3'].append(pessoa)

        return localizacao

    def qtd_de_pessoas_em_cada_local(self, dicionario_locais_pessoas):

        qtd_pessoas_local = {}
        local_1 = len(dicionario_locais_pessoas['local_1'])
        qtd_pessoas_local['local_1'] = local_1
        local_2 = len(dicionario_locais_pessoas['local_2'])
        qtd_pessoas_local['local_2'] = local_2
        local_3 = len(dicionario_locais_pessoas['local_3'])
        qtd_pessoas_local['local_3'] = local_3

        return qtd_pessoas_local

    def calcular_total_de_pessoas_por_lugar_porcentagem(self, total_de_pessoas, qtd_pessoas_local):

        a11 = (qtd_pessoas_local['local_1'] / float(total_de_pessoas)) * 100
        a12 = (qtd_pessoas_local['local_2'] / float(total_de_pessoas)) * 100
        a13 = (qtd_pessoas_local['local_3'] / float(total_de_pessoas)) * 100

        matriz = np.matrix([
            [a11, a12, a13],
        ])

        return matriz


arq = open('imagem.txt', 'r')
x = arq.read()
listaImagem = json.loads(x)

print(listaImagem)

m = Markov()

total_de_pessoas_3_locais = m.qtd_de_pessoas(listaImagem)
print(total_de_pessoas_3_locais)

localizacao_pessoas_3_locais = m.localizacao_pessoa(listaImagem)
print(localizacao_pessoas_3_locais)

total_de_pessoas_em_cada_local = m.qtd_de_pessoas_em_cada_local(localizacao_pessoas_3_locais)
print(total_de_pessoas_em_cada_local)

array_atual = m.calcular_total_de_pessoas_por_lugar_porcentagem(total_de_pessoas_3_locais,
                                                                total_de_pessoas_em_cada_local)
print(array_atual)
