import partida


class cabecalho_e_coleta_dados:

    def cabecalho(self):
        print('Bem-vindo ao jogo do NIM!\n')
        print('\nOpções de jogo:\n')
        print('1- Para jogar uma partida isolada\n2- Para jogar um campeonato\n')
        escolha = int(input('Digite uma opção para iniciarmos o jogo: '))
        caminho = tipos_de_partida()
        
        if escolha == 1:
            print('Você escolheu partida única!\n')
            caminho.partida_unica()
        else:
            print('Você escolheu campeonato!\n')
            caminho.campeonato()

def iniciar_programa():
    caminho = cabecalho_e_coleta_dados()
    caminho.cabecalho()

iniciar_programa()

