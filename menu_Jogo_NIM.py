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
            if event == 'Campeonato':
                self.campeonato()
            elif event == sg.WINDOW_CLOSED:
                janela_opcao.close()
            else:
                self.partida_unica()
    
    def partida_unica(self):

            '''caminho = partida.Partida()
            
            if escolha == 1:
                print('\nVocê escolheu partida única!\n')
                vencedor = caminho.jogar()

                if vencedor == 1:
                    print('Fim do jogo! Você ganhou!\n')
                else:
                    print('Fim do jogo! O computador ganhou!\n')'''

    def campeonato(self):

            '''else:
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
                print('Placar: Você', pontuacao_usuario, 'X', pontuacao_maquina, 'Computador')'''

def iniciar_programa():
    caminho = cabecalho_e_coleta_dados()
    caminho.cabecalho()

iniciar_programa()