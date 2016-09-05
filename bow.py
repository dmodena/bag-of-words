# Importações
import operator
import codecs
import re

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
words = [re.sub('\W', '', block) for block in text.lower().split(" ")]

# Criando dicionário de palavras
indices = {}

# Adicionando valores de acordo com quantidade de vezes
#  em que a palavra aparece
for word in words:
    if word in indices:
        indices[word] += 1
    else:
        indices[word] = 1

# Recalculando valores de acordo com total de palavras
total_words = len(words)
for word in indices:
    indices[word] /= total_words

# Ordenando resultados
sorted_indices = sorted(indices.items(), key=operator.itemgetter(1), reverse=True)

# Imprimindo resultados
print()
imprimir(sorted_indices)
print()
print(str(total_words) + " palavras distintas.")
