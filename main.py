from menu import menu
from jogar import jogar2, ler_ranking

reset_cor = '\033[0m'
letra_inexiste = '\033[0m'     # -> fundo preto
letra_errada = '\033[43m'   # -> fundo amarelo
letra_correta = '\033[42m'  # -> fundo verde
print('---------------------------------- GAME OF NAMES ------------------------------------')
print('------------------------------------ INSTRUÇÕES ------------------------------------')
print('Você deve escolher um nome com até 05 letras')
print('Você tem 20 tentativas para adivinhar o nome escolhido pelo sistema')
print('Abaixo deixamos um exemplo do funcionamento do sistema')
print(letra_correta ,'B', reset_cor ,'RUNO -> a letra B faz parte do nome e está na posição correta')
print('PE', letra_errada ,'D', reset_cor ,'RO -> a letra D faz parte do nome mas em outra posição')
print('EST', letra_inexiste,'E',reset_cor,'R -> a letra E não faz parte do nome ')
print('Boa sorte!')
print('------------------------------------------------------------------------------------')
while True:
    opcao = menu()
    if opcao == 'i':
        print('')
        print('')
        print('INICIAR JOGO')
        print('')
        jogar2()

    elif opcao == 'r':
        print('\033[35m'+'RANKING DOS JOGADORES'+'\033[0m')
        ranking = ler_ranking()
        if ranking == False:
            print('Sem ranking')
          
        else:
            primeiro_colocado = '\033[33m'   # -> fundo amarelo
            nickname = 0
            ranking = sorted(ranking, key=lambda r: r['chances'])
            msg=''
            for i in ranking:
                if msg == "":
                    msg += primeiro_colocado+i['nome'].upper()+"\t\t\t" +reset_cor+" "+i['chances']+" jogadas\n" 
                else:
                    msg += i['nome'] .upper()+" \t\t\t "+i['chances']+" jogadas\n" 
     
            print("NOME\t\t\tTENTATIVAS\n"+msg)
       
    elif opcao == 's':
        print('Obrigado por jogar o jogo dos nomes!')
        break