class Partidas:

    def usuario_comeca(self, numero_pecas, limite_pecas_por_jogada):
        print('Você começa!\n')
        while (numero_pecas > 0):
            usuario_pecas = self.usuario_escolhe_jogada(limite_pecas_por_jogada)
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

    def computador_comeca(self, numero_pecas, limite_pecas_por_jogada):
        print('Computador começa!\n')
        while numero_pecas > 0:
            computador_pecas = self.computador_escolhe_jogada(numero_pecas, limite_pecas_por_jogada)
            print('O computador tirou', computador_pecas, 'peças.')
            numero_pecas -= computador_pecas
            numComputador = numero_pecas
            if numComputador == 0:
                return 0
            print('Agora restam', numero_pecas, 'peças no tabuleiro.')
            usuario_pecas = self.usuario_escolhe_jogada(limite_pecas_por_jogada)
            print('Você tirou', usuario_pecas, 'peças.')
            numero_pecas -= usuario_pecas
            numUsuario = numero_pecas
            if numUsuario == 0:
                return 1
            print('Agora restam', numero_pecas, 'peças no tabuleiro.')
            pass

    def usuario_escolhe_jogada(self, limite_pecas_por_jogada):
        '''while True:
            quant_pecas = int(input('Quantas peças você vai retirar? '))
            if (quant_pecas > 0 and quant_pecas <= limite_pecas_por_jogada):
                return quant_pecas
                pass
            else:
                print('Oops! Jogada inválida! Tente de novo.')
                pass
            pass'''
        return limite_pecas_por_jogada - 1

    def computador_escolhe_jogada(self, numero_pecas, limite_pecas_por_jogada):
        if numero_pecas <= limite_pecas_por_jogada:
            return numero_pecas
            pass
        else:
            if numero_pecas % (limite_pecas_por_jogada + 1) > 0:
                return numero_pecas % (limite_pecas_por_jogada + 1)
                pass
            return limite_pecas_por_jogada
            pass