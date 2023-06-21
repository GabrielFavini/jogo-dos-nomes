def carrega_nomes():
    names = []
    with open('C:/Users/gabri/OneDrive/Documentos/jogo/base_nomes.txt') as arquivo:
        for i in arquivo:
            names.append(i.replace("\n",'').upper())
    return(names)

def salva_ranking(nome, chances):
    conteudo = nome + '-' + str(chances)
    with open('C:/Users/gabri/OneDrive/Documentos/jogo/ranking.txt','a') as arquivo:
        arquivo.write(conteudo+'\n')
       
def ler_ranking():
    import os
    if os.path.exists('C:/Users/gabri/OneDrive/Documentos/jogo/ranking.txt'):
        ranking = []
        with open('ranking.txt') as arquivo:
            for i in arquivo:
                linha = i.split('-')
                ranking.append({'nome':linha[0],'chances':linha[1].replace("\n",'')})
        return ranking  
    else:
        return False

def jogar2():
    import random
    nomes = carrega_nomes()
    nome = random.choice(nomes)
    #print(nome)
    termo = nome
    termo = termo.upper()[:5]
    chances = 20
    reset_cor = '\033[0m'
    letra_inexiste = '\033[0m'  # -> fundo preto
    letra_errada = '\033[43m'   # -> fundo amarelo
    letra_correta = '\033[42m'  # -> fundo verde
    nickname = str(input('Qual será seu nickname com até 5 letras? '))[:5]  
   
    while chances > 0:  
        palavra = []
        chute = str(input(f'Oi {nickname}, tente adivinhar um nome com 5 letras: ')).upper()[:5]
        chances -= 1
        if chute == termo:
            print(letra_correta,chute,reset_cor)
            print(f'Parabéns {nickname}, voce acertou o nome!')
            salva_ranking(nickname, 20-chances)
            break
        elif chances == 0:
            print('Infelizmente suas chances acabaram :( ')
            break
        else:
            print('Errou, tente novamente:')
            i = 0
            for letra in chute:
                palavra.append(letra)
                if letra not in termo:
                    palavra[i] = letra_inexiste +' '+ palavra[i] +' '+ reset_cor
                elif palavra[i] == termo[i]:
                    palavra[i] = palavra[i] = letra_correta +' '+ palavra[i] +' '+ reset_cor
                else:
                    palavra[i] = palavra[i] = letra_errada +' '+ palavra[i] +' '+ reset_cor
                i += 1
            for c in palavra:
                    print(c, end='')
            print("\n")
            