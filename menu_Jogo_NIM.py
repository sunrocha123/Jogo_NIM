import partida
import PySimpleGUI as sg


class cabecalho_e_coleta_dados:

    def cabecalho(self):

        informacoes_tela_inicial = [[sg.Text('Bem-vindo ao Jogo DONIM!!!\n')],
                            [sg.Button('Jogar')],
                            [sg.Button('Sair')]]

        janela_tela_inicial = sg.Window('Tela inicial', informacoes_tela_inicial)

        event, values = janela_tela_inicial.read()
        if event == 'Sair' or event == sg.WINDOW_CLOSED:
            return janela_tela_inicial.close()
        else:
            janela_tela_inicial.close()
            informacoes_opcao = [[sg.Text('Escolha uma opção de partida:')],
                            [sg.Button('Única')],
                            [sg.Button('Campeonato')]]
            
            janela_opcao = sg.Window('Opções de partida', informacoes_opcao)

            event, values = janela_opcao.read()
            janela_opcao.close()
            if event == 'Campeonato':
                self.campeonato()
            else:
                self.partida_unica()

    def caminho(self):
        return partida.Partida()
    
    def partida_unica(self):

        vencedor = self.caminho().jogar()

        if vencedor == 1:
            quem_venceu = [[sg.Text('Fim do jogo! Você ganhou!')]]
        else:
            quem_venceu = [[sg.Text('Fim do jogo! O computador ganhou!')]]

        janela_vencedor = sg.Window('Vencedor', quem_venceu)
        
        while True:
            event, values = janela_vencedor.read()
            if event == sg.WINDOW_CLOSED:
                break

    '''def campeonato(self):
            pontuacao_usuario = 0
            pontuacao_maquina = 0

            pontuacao = [[sg.Text('Usuário:', str(pontuacao_usuario))],
                         [sg.Text('Máquina:', str(pontuacao_maquina))]]

            janela_pontuacao = sg.Window('Placar', pontuacao)

            while True:
                event, values = janela_pontuacao.read()
                if event == sg.WINDOW_CLOSED:
                    break
                else:
                    for i in range(3):
                        print(str(i + 1) + 'º Disputa\n')
                        vencedor = self.caminho().jogar()
                        if vencedor == 1:
                            pontuacao_usuario += 1
                            print('Você ganhou a ' + str(i + 1) + 'º disputa\n')
                        else:
                            pontuacao_maquina += 1
                            print('O computador ganhou a ' + str(i + 1) + 'º disputa\n')
                    print('Placar: Você', pontuacao_usuario, 'X', pontuacao_maquina, 'Computador')'''

def iniciar_programa():
    caminho = cabecalho_e_coleta_dados()
    caminho.cabecalho()

iniciar_programa()