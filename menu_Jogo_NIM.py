<<<<<<< HEAD
import partida


class cabecalho_e_coleta_dados:

    def cabecalho(self):
        print('Bem-vindo ao jogo do NIM!\n')
        print('Opções de jogo:\n')
        print('1- Partida Única\n2- Campeonato\n')

        escolha = int(input('Digite uma opção para iniciarmos o jogo: '))
        caminho = partida.Partida()
        
        if escolha == 1:
            print('\nVocê escolheu partida única!\n')
            vencedor = caminho.jogar()

            if vencedor == 1:
                print('Fim do jogo! Você ganhou!\n')
            else:
                print('Fim do jogo! O computador ganhou!\n')
                    
        else:
            print('\nVocê escolheu campeonato!')
            pontuacao_usuario = 0
            pontuacao_maquina = 0
            for i in range(3):
                print(str(i + 1) + 'º Disputa\n')
                vencedor = caminho.jogar()
                if vencedor == 1:
                    pontuacao_usuario += 1
                    print('Você ganhou a ' + str(i + 1) + 'º disputa\n')
                else:
                    pontuacao_maquina += 1
                    print('O computador ganhou a ' + str(i + 1) + 'º disputa\n')
            print('Placar: Você', pontuacao_usuario, 'X', pontuacao_maquina, 'Computador')

def iniciar_programa():
    caminho = cabecalho_e_coleta_dados()
    caminho.cabecalho()

iniciar_programa()

=======
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

>>>>>>> 86c6be42e71c43c0c9b6fd8a91611fb1197aae29
