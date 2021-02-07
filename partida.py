class Partidas:

    def __init__(self, numero_pecas, limite_pecas_por_jogada):
        self.limite_pecas_por_jogada = limite_pecas_por_jogada
        self.numero_pecas = numero_pecas

    def usuario_comeca(self):
        print('Você começa!\n')
        while (self.numero_pecas > 0):
            usuario_pecas = self.usuario_escolhe_jogada()
            print('Você tirou', usuario_pecas, 'peças.')
            self.numero_pecas -= usuario_pecas
            numUsuario = self.numero_pecas
            if numUsuario == 0:
                return 1
            print('Agora restam', self.numero_pecas, 'peças no tabuleiro.')
            computador_pecas = self.computador_escolhe_jogada()
            print('O computador tirou', computador_pecas, 'peças.')
            self.numero_pecas -= computador_pecas
            numComputador = self.numero_pecas
            if numComputador == 0:
                return 0
            print('Agora restam', self.numero_pecas, 'peças no tabuleiro.')
            pass

    def computador_comeca(self):
        print('Computador começa!\n')
        while self.numero_pecas > 0:
            computador_pecas = self.computador_escolhe_jogada()
            print('O computador tirou', computador_pecas, 'peças.')
            self.numero_pecas -= computador_pecas
            numComputador = self.numero_pecas
            if numComputador == 0:
                return 0
            print('Agora restam', self.numero_pecas, 'peças no tabuleiro.')
            usuario_pecas = self.usuario_escolhe_jogada()
            print('Você tirou', usuario_pecas, 'peças.')
            self.numero_pecas -= usuario_pecas
            numUsuario = self.numero_pecas
            if numUsuario == 0:
                return 1
            print('Agora restam', self.numero_pecas, 'peças no tabuleiro.')
            pass

    def usuario_escolhe_jogada(self):
        while True:
            quant_pecas = int(input('Quantas peças você vai retirar? '))
            if (quant_pecas > 0 and quant_pecas <= self.limite_de_jogadas):
                return quant_pecas
                pass
            else:
                print('Oops! Jogada inválida! Tente de novo.')
                pass
            pass

    def computador_escolhe_jogada(self):
        if self.numero_pecas <= self.limite_de_jogadas:
            return self.numero_pecas
            pass
        else:
            if self.numero_pecas % (self.limite_de_jogadas + 1) > 0:
                return self.numero_pecas % (self.limite_de_jogadas + 1)
                pass
            return self.limite_de_jogadas
            pass