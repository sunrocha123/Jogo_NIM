class coleta_dados:

    def coletar_dados(self):
        numero_pecas = int(input('Digite a quantidade de peças que terá no tabuleiro: '))
        limite_de_retirada_de_pecas = int(input('Digite o limite de peças que podem ser retiradas do tabuleiro: '))

        if numero_pecas % (limite_de_retirada_de_pecas + 1) == 0:
            quem_comeca = 1
        else:
            quem_comeca = 0

        return numero_pecas, limite_de_retirada_de_pecas, quem_comeca


class Partida:

    def jogar(self, quantidade_de_partidas):

        caminho_coleta_dados = coleta_dados()

        for i in range(quantidade_de_partidas):
            dados_necessarios = caminho_coleta_dados.coletar_dados()
            numero_pecas_tabuleiro = dados_necessarios[0]
            quem_vence = dados_necessarios[2]
                
    def usuario_escolhe_jogada(self, limite_pecas_por_jogada):
        '''while True:
            quant_pecas = int(input('Quantas peças você vai retirar? '))
            if (quant_pecas > 0 and quant_pecas <= limite_pecas_por_jogada):
                return quant_pecas
                pass
            else:
                print('Oops! Jogada inválida! Tente de novo.')
                pass
            pass''' # Campo desabilitado para realização de testes
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





'''class tipos_de_partida:

    def __init__(self, numero_de_pecas, limite_pecas_por_jogada):
        self.numero_de_pecas = numero_de_pecas
        self.limite_pecas_por_jogada = limite_pecas_por_jogada

    def caminho(self):
        return partida.Partidas()

    def partida_unica(self):
        print('Você escolheu uma partida isolada!\n')
        print('******PARTIDA******\n')

        partida_isolada = self.validar_quem_comeca()

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

            partida_campeonato = self.validar_quem_comeca()

            if partida_campeonato == 1:
                vencedor_usuario += 1
                print('Você ganhou a ' + str(i + 1) + 'º disputa\n')
            else:
                vencedor_maquina += 1
                print('O computador ganhou a ' + str(i + 1) + 'º disputa\n')
        print('Placar: Você', vencedor_usuario, 'X', vencedor_maquina, 'Computador')

    def validar_quem_comeca(self):
        if self.numero_pecas % (self.limite_pecas_por_jogada + 1) == 0:
            return self.caminho().usuario_comeca(self.numero_pecas, self.limite_pecas_por_jogada)
        else:
            return self.caminho().computador_comeca(self.numero_pecas, self.limite_pecas_por_jogada)'''

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