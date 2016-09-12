# Importações
import operator
import codecs
import re
from collections import Counter

# Retorna a quantidade de pontos para formatação
def pts(number):
    return "." * number

# Método para imprimir dicionários
def imprimir(dicionario):
    for (word, value) in dicionario:
        if len(word) < 25:
            print(word + pts(25 - len(word)) + ": " + str(value))
        else:
            print(word + ": " + str(value))

# Lendo texto
fd = codecs.open('text.txt', 'r', 'utf-8')
text = fd.read()
fd.close()

# Criando lista a partir do texto, ignorando capitalização
#  e caracteres especiais
all_words = re.findall(r'\w+', text.lower())

# Stopwords
stopwords = ['a', 'ante', 'as', 'até', 'após', 'com', 'contra', 'de', 'desde', 'o', 'os', 'para', 'perante', 'por', 'sem', 'sob', 'sobre', 'trás', 'um', 'uma', 'uns', 'umas']

# Removendo stopwords
words = [w for w in all_words if w not in stopwords]

# Contador de palavras
word_count = Counter(words)
total_words = len(words)

# Criando dicionário de palavras
indices = {}
for w in word_count:
    indices[w] = word_count[w] / total_words

# Ordenando resultados
sorted_indices = sorted(indices.items(), key=operator.itemgetter(1), reverse=True)

# Removendo palavras menos usadas
sorted_indices_size = len(sorted_indices)
limit_size = sorted_indices_size - int(round(sorted_indices_size / 10))

# Limitando tamanho da list
filtered_list = sorted_indices[0:1000] if limit_size > 1000 else sorted_indices[0:limit_size]

# Imprimindo resultados
print()
imprimir(filtered_list)
print()
print(str(len(filtered_list)) + " palavras distintas.")
