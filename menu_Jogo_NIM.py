import partida

class tipos_de_partida:

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
            return self.caminho().computador_comeca(self.numero_pecas, self.limite_pecas_por_jogada)

class cabecalho_e_coleta_dados:

    def cabecalho(self):
        print('Bem-vindo ao jogo do NIM!\n')
        dados_necessarios = self.coletar_dados()
        tipos_de_partida(dados_necessarios[0], dados_necessarios[1])
        print('\nOpções de jogo:\n')
        print('1- Para jogar uma partida isolada\n2- Para jogar um campeonato\n')
        escolha = int(input('Digite uma opção para iniciarmos o jogo: '))
        caminho = tipos_de_partida()
        
        if escolha == 1:
            caminho.partida_unica()
        else:
            caminho.campeonato()

    def coletar_dados(self):
        numero_pecas = int(input('Digite a quantidade de peças no tabuleiro:  '))
        limite_pecas_por_jogada = int(input('Digite o limite de retirada de peça por jogada: '))
        return numero_pecas, limite_pecas_por_jogada

def iniciar_programa():
    caminho = cabecalho_e_coleta_dados()
    caminho.cabecalho()

iniciar_programa()