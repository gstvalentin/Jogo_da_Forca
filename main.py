import re
from secrets import choice
from words import lista_palavras
from erros import desenha_forca

#? Procura palavras válidas para jogo
def get_valid_words(lista_palavras):
    word = choice(lista_palavras)
    while '-' in word or ' ' in word:
        word = choice(lista_palavras)
    
    return word

#print(get_valid_words(lista_palavras))



def forca():
    letras_usadas = []
    letras_erradas = []
    word = get_valid_words(lista_palavras).upper()
    erros = 0
    palavara_secreta = '_ ' * len(word)
    desenha_forca(erros)
    print(palavara_secreta)
    while True:
        letra = input('\nTentativa: ').upper()
        letras_usadas.append(letra)
        secreto_temporario = ''
        if erros >= 6:
            desenha_forca(7)
            print(f'Você perdeu! A palavra era "{word}"')
            break
        if len(letra) > 1:
            print('Tente novamente, só é possível digitar uma letra por vez')
            continue
        
        for letra_secreta in word: #? Loop para user visualizar as tentativas
            if letra_secreta in letras_usadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '_ '
        
        if letra not in word:
            erros += 1
        if letra not in word:
            letras_erradas.append(letras_usadas.pop())
            
        
        if secreto_temporario == word:
            print(f'Parabéns, você ganhou! A palavra era {secreto_temporario}')
        else:
            desenha_forca(erros)
            print()
            print(f'A palavra secreta está assim: {secreto_temporario}')
            print(f'Você já tentou as seguintes letras {letras_erradas}')

if __name__ == "__main__":
    forca()

# palavra = get_valid_words(lista_palavras)
# print(palavra)
# palavara_secreta = '_ ' * len(palavra)
# 