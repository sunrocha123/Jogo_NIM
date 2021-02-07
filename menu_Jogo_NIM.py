import partida

class Menu:

    def caminho(self, numero_pecas, limite_pecas_por_jogada):
        return partida.Partidas(numero_pecas, limite_pecas_por_jogada)

    def cabecalho(self):
        print('Bem-vindo ao jogo do NIM!\n')
        numero_pecas = int(input('Digite a quantidade de peças no tabuleiro:  '))
        limite_pecas_por_jogada = int(input('Digite o limite de retirada de peça por jogada: '))
        print('\nOpções de jogo:\n')
        print('1- Para jogar uma partida isolada\n2- Para jogar um campeonato\n')
        escolha = int(input('Digite uma opção para iniciarmos o jogo: '))
        self.caminho(numero_pecas, limite_pecas_por_jogada)
        if escolha == 1:
            self.partida_unica()
        else:
            self.campeonato()

    def partida_unica(self):
        print('Você escolheu uma partida isolada!\n')
        print('******PARTIDA******\n')
        if partida_isolada == 1:
            print('Fim do jogo! Você ganhou!\n')
        else:
            print('Fim do jogo! O computador ganhou!\n')
        pass

    def campeonato(self):
        print('Você escolheu um campeonato!\n')
        vencedor_usuario = 0
        vencedor_maquina = 0

        for i in range(3):
            print(str(i + 1) + 'º Disputa\n')
            partida_campeonato = caminho.partida()
            if partida_campeonato == 1:
                vencedor_usuario += 1
                print('Você ganhou a ' + str(i + 1) + 'º disputa\n')
            else:
                vencedor_maquina += 1
                print('O computador ganhou a ' + str(i + 1) + 'º disputa\n')
        print('Placar: Você', vencedor_usuario, 'X', vencedor_maquina, 'Computador')