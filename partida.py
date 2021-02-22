class coleta_dados:

    def coletar_dados(self):
        numero_pecas = int(input('Digite a quantidade de peças que terá no tabuleiro: '))
        limite_de_retirada_de_pecas = int(input('Digite o limite de peças que podem ser retiradas do tabuleiro: '))

        '''numero_pecas = 5
        limite_de_retirada_de_pecas = 2 # campo para testes'''

        if numero_pecas % (limite_de_retirada_de_pecas + 1) == 0:
            print('Você começa!\n')
            quem_comeca = [[1,0],[-1,-1]] # Linha 1: 1º posição: Usuário; 2º posição: Máquina
        else:
            print('Computador começa!\n')
            quem_comeca = [[0,1],[-1,-1]] # Linha 1: 1º posição: Máquina; 2º posição: Usuário 

        return numero_pecas, limite_de_retirada_de_pecas, quem_comeca


class Partida:

    def jogar(self):

        caminho_coleta_dados = coleta_dados()

        dados_necessarios = caminho_coleta_dados.coletar_dados()
        numero_pecas_tabuleiro = dados_necessarios[0]
        numero_pecas_jogadores = dados_necessarios[2]
        limite_de_retirada_de_pecas = dados_necessarios[1] 

        while numero_pecas_tabuleiro > 0:

            for j in range(len(numero_pecas_jogadores)):

                if numero_pecas_jogadores[0][j] == 1:
                    numero_peca_usuario = self.usuario_escolhe_jogada(limite_de_retirada_de_pecas)
                    print('Você tirou', numero_peca_usuario, 'peças do tabuleiro')
                    auxiliar = numero_peca_usuario

                else:
                    numero_peca_computador = self.computador_escolhe_jogada(numero_pecas_tabuleiro, limite_de_retirada_de_pecas)
                    print('O computador tirou', numero_peca_computador, 'peças do tabuleiro')
                    auxiliar = numero_peca_computador
                    
                numero_pecas_jogadores[1][j] = numero_pecas_tabuleiro - auxiliar
                numero_pecas_tabuleiro = numero_pecas_jogadores[1][j]

                print('Agora restam', numero_pecas_tabuleiro, 'peças no tabuleiro\n')

                if numero_pecas_jogadores[1][j] == 0:
                    if numero_pecas_jogadores[0][j] == 1:
                        return 1
                    else:
                        return 0
                        
                
    def usuario_escolhe_jogada(self, limite_pecas_por_jogada):
        while True:
            quant_pecas = int(input('Quantas peças você vai retirar? '))
            if (quant_pecas > 0 and quant_pecas <= limite_pecas_por_jogada):
                return quant_pecas
                pass
            else:
                print('Oops, jogada inválida! O valor de retirada de peças, precisa ser igual ou menor que o limite estabelecido\n')
                pass
            pass

        '''return limite_pecas_por_jogada - 1 # Campo usado apenas para testes'''

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