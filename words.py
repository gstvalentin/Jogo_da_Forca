from unidecode import unidecode

dicionario = open('brutf8.txt', 'r', encoding='utf-8').readlines()
lista_palavras = []
for d in dicionario:
    words = unidecode(d.replace('\n', '')) #? Sem acentos e ç
    #words = d.replace('\n', '')  #? Com acentos e ç
    lista_palavras.append(words)
