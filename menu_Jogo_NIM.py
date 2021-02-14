import partida
import pygame


class cabecalho_e_coleta_dados:

    def cabecalho(self):
        print('Bem-vindo ao jogo DoNIM!\n')
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

# Criando interface gráfica do jogo

'''class tela_inicio:

    def exibir_tela_inicio(self):

        pygame.init()
        pygame.font.init()
        tela = pygame.display.set_mode([800,450])
        pygame.display.set_caption("Jogo DoNIM")
        fonte_padrao = pygame.font.get_default_font()
        tamanhos_fonte = [45,30]

        cabecalho = pygame.Surface([500, 80])
        cabecalho.fill((139,0,0)) # cor do cabeçalho
        fonte_cabecalho = pygame.font.SysFont(fonte_padrao, tamanhos_fonte[0])
        texto_cabecalho = fonte_cabecalho.render('BEM-VINDO AO JOGO DONIM!', 1, (250,250,250))

        instrucoes_jogo = pygame.Surface([250,80])
        instrucoes_jogo.fill((255,69,0)) # cor da opção "instruções do jogo"
        fonte_instrucoes_jogo = pygame.font.SysFont(fonte_padrao, tamanhos_fonte[1])
        texto_instrucoes_jogo = fonte_instrucoes_jogo.render('INSTRUÇÕES DO JOGO',1,(250,250,250))

        jogar = pygame.Surface([250,80])
        jogar.fill((255,69,0)) # cor da opção "jogar"
        fonte_jogar = fonte_instrucoes_jogo
        texto_jogar = fonte_jogar.render('JOGAR',1,(250,250,250))

        pygame.mixer.music.load('Músicas/tela_inicio.ogg')
        pygame.mixer.music.play()


        relogio = pygame.time.Clock()
        sair_jogo = False

        while sair_jogo != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair_jogo = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    instrucoes_jogo.move_ip(10,10)
            relogio.tick(30)
            tela.blit(cabecalho,[150,45])
            tela.blit(instrucoes_jogo,[275,180])
            tela.blit(jogar,[275, 300])
            cabecalho.blit(texto_cabecalho,[30,25])
            instrucoes_jogo.blit(texto_instrucoes_jogo,[10,27])
            jogar.blit(texto_jogar,[87,30])
            pygame.display.update()       
        pygame.quit()

def iniciar():
    caminho = tela_inicio()
    caminho.exibir_tela_inicio()

iniciar()'''
