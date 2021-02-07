class Jogar_NIM:

    def partida(self):
        while True:
            numero_pecas = int(input('Quantas peças? '))
            limite_pecas_por_jogada = int(input('Limite de peças por jogada? '))
            print()
            if (numero_pecas > 0 and limite_pecas_por_jogada > 0):
                if numero_pecas % (limite_pecas_por_jogada + 1) == 0:
                    print('Você começa!\n')
                    while (numero_pecas > 0):
                        usuario_pecas = self.usuario_escolhe_jogada(numero_pecas, limite_pecas_por_jogada)
                        print('Você tirou', usuario_pecas, 'peças.')
                        numero_pecas -= usuario_pecas
                        numUsuario = numero_pecas
                        if numUsuario == 0:
                            return 1
                        print('Agora restam', numero_pecas, 'peças no tabuleiro.')
                        computador_pecas = self.computador_escolhe_jogada(numero_pecas, limite_pecas_por_jogada)
                        print('O computador tirou', computador_pecas, 'peças.')
                        numero_pecas -= computador_pecas
                        numComputador = numero_pecas
                        if numComputador == 0:
                            return 0
                        print('Agora restam', numero_pecas, 'peças no tabuleiro.')
                        pass
                    pass
                else:
                    print('Computador começa!\n')
                    while numero_pecas > 0:
                        computador_pecas = self.computador_escolhe_jogada(numero_pecas, limite_pecas_por_jogada)
                        print('O computador tirou', computador_pecas, 'peças.')
                        numero_pecas -= computador_pecas
                        numComputador = numero_pecas
                        if numComputador == 0:
                            return 0
                        print('Agora restam', numero_pecas, 'peças no tabuleiro.')
                        usuario_pecas = self.usuario_escolhe_jogada(numero_pecas, limite_pecas_por_jogada)
                        print('Você tirou', usuario_pecas, 'peças.')
                        numero_pecas -= usuario_pecas
                        numUsuario = numero_pecas
                        if numUsuario == 0:
                            return 1
                        print('Agora restam', numero_pecas, 'peças no tabuleiro.')
                        pass
                    pass
                pass
            else:
                print('Os valores digitados precisam ser maiores que 0')
                pass
            pass

    def usuario_escolhe_jogada(self, n, m):
        while True:
            quant_pecas = int(input('Quantas peças você vai retirar? '))
            if (quant_pecas > 0 and quant_pecas <= m):
                return quant_pecas
                pass
            else:
                print('Oops! Jogada inválida! Tente de novo.')
                pass
            pass

    def computador_escolhe_jogada(self, n, m):
        if n <= m:
            return n
            pass
        else:
            if n % (m + 1) > 0:
                return n % (m + 1)
                pass
            return m
            pass


def main():
    print('Bem-vindo ao jogo do NIM!\n\nOpções de jogo:\n')
    print('1- Para jogar uma partida isolada\n2- Para jogar um campeonato\n')
    escolha = int(input('Digite uma opção para iniciarmos o jogo: '))
    caminho = Jogar_NIM()
    if escolha == 1:
        print('Você escolheu uma partida isolada!\n')
        print('******PARTIDA******\n')
        partida_isolada = caminho.partida()
        if partida_isolada == 1:
            print('Fim do jogo! Você ganhou!\n')
        else:
            print('Fim do jogo! O computador ganhou!\n')
        pass
    else:
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
        pass

main()