import datetime
import pathlib
import socket
import pygame
import os

from pygame import mixer
from pathlib import Path
from datetime import datetime
from threading import Thread
from tkinter import *

IP_SERVIDOR = '10.16.90.208'
PORTA = '8080'

class Application:
    def __init__(self, root):
        self.root = root
        self.janela()
        self.tela()
        self.tela2()
        self.tela3()
        self.tela4()
        self.tela5()
        self.tela6()
        self.tela7()
        self.tela8()
        self.tela9()
        self.tela10()
        self.tela11()
        self.tela12()
        self.tela13()
        self.tela14()
        self.tela15()
        self.tela16()
        self.tela17()
        self.tela18()
        self.tela19()
        self.botao()
        self.botao2()
        self.botao3()
        self.botao4()
        self.botao5()
        self.botao6()
        self.botao7()
        self.botao8()
        self.botao9()
        self.botao10()
        self.botao11()
        self.botao12()
        self.botao13()
        self.botao14()
        self.botao15()
        self.botao16()
        self.botao17()
        self.botao18()
        self.botao19()
        self.cor_padrao = 'black'
        self.cor_alerta = 'red'
        self.servidor = True

        self.server_thread = Thread(target=self.start_server)
        self.server_thread.start()
        
    # cria a janela
    def janela(self):    
        self.root.title('Servidor de Emergencias')
        self.root.configure(background='white')

        # define o tamanho da tela 
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        proporcao = 0.90

        largura = int(largura_tela * proporcao)
        altura = int(altura_tela * proporcao)

        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        self.root.geometry(f'{largura}x{altura}+{x}+{y}')

        self.root.resizable(True, True)

    #Cria a tela para exibir o texto "Consultorio1"
    def tela(self):
        self.tela_consultorio1 = Label(self.root, text='Consultorio1')
        self.tela_consultorio1.place(x=5, y=5, width=100, height=85)
        self.tela_consultorio1.config(font=('Arial', 13))

    # cria o botao "Stop"
    def botao(self):
        self.botao_stop = Button(self.root, text='Parar')
        self.botao_stop.config(font=('Arial', 20))
        self.botao_stop.place(x=5, y=100, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela2(self):
        self.tela_consultorio2 = Label(self.root, text='Consultorio2')
        self.tela_consultorio2.place(x=110, y=5, width=100, height=85)
        self.tela_consultorio2.config(font=('Arial', 13))

    def botao2(self):
        self.botao_stop2 = Button(self.root, text='Parar')
        self.botao_stop2.config(font=('Arial', 20))
        self.botao_stop2.place(x=110, y=100, width=100, height=50)

        self.botao_stop2.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela3(self):
        self.tela_consultorio3 = Label(self.root, text='Consultorio3')
        self.tela_consultorio3.place(x=215, y=5, width=100, height=85)
        self.tela_consultorio3.config(font=('Arial', 13))

    def botao3(self):
        self.botao_stop3 = Button(self.root, text='Parar')
        self.botao_stop3.config(font=('Arial', 20))
        self.botao_stop3.place(x=215, y=100, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop3.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela4(self):
        self.tela_consultorio4 = Label(self.root, text='Consultorio4')
        self.tela_consultorio4.place(x=320, y=5, width=100, height=85)
        self.tela_consultorio4.config(font=('Arial', 13))

    def botao4(self):
        self.botao_stop4 = Button(self.root, text='Parar')
        self.botao_stop4.config(font=('Arial', 20))
        self.botao_stop4.place(x=320, y=100, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop4.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela5(self):
        self.tela_consultorio5 = Label(self.root, text='Consultorio5')
        self.tela_consultorio5.place(x=425, y=5, width=100, height=85)
        self.tela_consultorio5.config(font=('Arial', 13))

    def botao5(self):
        self.botao_stop5 = Button(self.root, text='Parar')
        self.botao_stop5.config(font=('Arial', 20))
        self.botao_stop5.place(x=425, y=100, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop5.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela6(self):
        self.tela_consultorio6 = Label(self.root, text='Consultorio6')
        self.tela_consultorio6.place(x=5, y=160, width=100, height=85)
        self.tela_consultorio6.config(font=('Arial', 13))

    def botao6(self):
        self.botao_stop6 = Button(self.root, text='Parar')
        self.botao_stop6.config(font=('Arial', 20))
        self.botao_stop6.place(x=5, y=255, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop6.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela7(self):
        self.tela_consultorio7 = Label(self.root, text='Consultorio7')
        self.tela_consultorio7.place(x=110, y=160, width=100, height=85)
        self.tela_consultorio7.config(font=('Arial', 13))

    def botao7(self):
        self.botao_stop7 = Button(self.root, text='Parar')
        self.botao_stop7.config(font=('Arial', 20))
        self.botao_stop7.place(x=110, y=255, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop7.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela8(self):
        self.tela_consultorio8 = Label(self.root, text='Consultorio8')
        self.tela_consultorio8.place(x=215, y=160, width=100, height=85)
        self.tela_consultorio8.config(font=('Arial', 13))

    def botao8(self):
        self.botao_stop8 = Button(self.root, text='Parar')
        self.botao_stop8.config(font=('Arial', 20))
        self.botao_stop8.place(x=215, y=255, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop8.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela9(self):
        self.tela_consultorio9 = Label(self.root, text='Consultorio9')
        self.tela_consultorio9.place(x=320, y=160, width=100, height=85)
        self.tela_consultorio9.config(font=('Arial', 13))

    def botao9(self):
        self.botao_stop9 = Button(self.root, text='Parar')
        self.botao_stop9.config(font=('Arial', 20))
        self.botao_stop9.place(x=320, y=255, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop9.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela10(self):
        self.tela_consultorio10 = Label(self.root, text='Consultorio10')
        self.tela_consultorio10.place(x=425, y=160, width=100, height=85)
        self.tela_consultorio10.config(font=('Arial', 11))

    def botao10(self):
        self.botao_stop10 = Button(self.root, text='Parar')
        self.botao_stop10.config(font=('Arial', 20))
        self.botao_stop10.place(x=425, y=255, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop10.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela11(self):
        self.tela_consultorio11 = Label(self.root, text='Consultorio11')
        self.tela_consultorio11.place(x=5, y=315, width=100, height=85)
        self.tela_consultorio11.config(font=('Arial', 11))

    def botao11(self):
        self.botao_stop11 = Button(self.root, text='Parar')
        self.botao_stop11.config(font=('Arial', 20))
        self.botao_stop11.place(x=5, y=410, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop11.bind('<Button-1>', lambda event: self.receber_requisicao(event))
    
    def tela12(self):
        self.tela_consultorio12 = Label(self.root, text='Consultorio12')
        self.tela_consultorio12.place(x=110, y=315, width=100, height=85)
        self.tela_consultorio12.config(font=('Arial', 11))

    def botao12(self):
        self.botao_stop12 = Button(self.root, text='Parar')
        self.botao_stop12.config(font=('Arial', 20))
        self.botao_stop12.place(x=110, y=410, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop12.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela13(self):
        self.tela_consultorio13 = Label(self.root, text='Consultorio13')
        self.tela_consultorio13.place(x=215, y=315, width=100, height=85)
        self.tela_consultorio13.config(font=('Arial', 11))

    def botao13(self):
        self.botao_stop13 = Button(self.root, text='Parar')
        self.botao_stop13.config(font=('Arial', 20))
        self.botao_stop13.place(x=215, y=410, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop13.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela14(self):
        self.tela_consultorio14 = Label(self.root, text='Consultorio14')
        self.tela_consultorio14.place(x=320, y=315, width=100, height=85)
        self.tela_consultorio14.config(font=('Arial', 11))

    def botao14(self):
        self.botao_stop14 = Button(self.root, text='Parar')
        self.botao_stop14.config(font=('Arial', 20))
        self.botao_stop14.place(x=320, y=410, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop14.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela15(self):
        self.tela_consultorio15 = Label(self.root, text='Consultorio15')
        self.tela_consultorio15.place(x=425, y=315, width=100, height=85)
        self.tela_consultorio15.config(font=('Arial', 11))

    def botao15(self):
        self.botao_stop15 = Button(self.root, text='Parar')
        self.botao_stop15.config(font=('Arial', 20))
        self.botao_stop15.place(x=425, y=410, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop15.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela16(self):
        self.tela_consultorio16 = Label(self.root, text='Consultorio16')
        self.tela_consultorio16.place(x=5, y=468, width=100, height=85)
        self.tela_consultorio16.config(font=('Arial', 11))

    def botao16(self):
        self.botao_stop16 = Button(self.root, text='Parar')
        self.botao_stop16.config(font=('Arial', 20))
        self.botao_stop16.place(x=5, y=563, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop16.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela17(self):
        self.tela_consultorio17 = Label(self.root, text='Consultorio17')
        self.tela_consultorio17.place(x=110, y=468, width=100, height=85)
        self.tela_consultorio17.config(font=('Arial', 11))

    def botao17(self):
        self.botao_stop17 = Button(self.root, text='Parar')
        self.botao_stop17.config(font=('Arial', 20))
        self.botao_stop17.place(x=110, y=563, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop17.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela18(self):
        self.tela_consultorio18 = Label(self.root, text='Consultorio18')
        self.tela_consultorio18.place(x=215, y=468, width=100, height=85)
        self.tela_consultorio18.config(font=('Arial', 11))

    def botao18(self):
        self.botao_stop18 = Button(self.root, text='Parar')
        self.botao_stop18.config(font=('Arial', 20))
        self.botao_stop18.place(x=215, y=563, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop18.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def tela19(self):
        self.tela_consultorio19 = Label(self.root, text='Consultorio19')
        self.tela_consultorio19.place(x=320, y=468, width=100, height=85)
        self.tela_consultorio19.config(font=('Arial', 11))

    def botao19(self):
        self.botao_stop19 = Button(self.root, text='Parar')
        self.botao_stop19.config(font=('Arial', 20))
        self.botao_stop19.place(x=320, y=563, width=100, height=50)
        
        # Liga o clique com o botão esquerdo do mouse aos dois métodos
        self.botao_stop19.bind('<Button-1>', lambda event: self.receber_requisicao(event))


    def start_server(self):

        desktop_path = Path.home() / 'Desktop'
        log_file = desktop_path / 'Registro.txt'
       
        #inicia o audio
        pygame.mixer.init() 
        
        #path_audio = pathlib.Path(r"C:\Users\Usuário\Desktop\Servidor-Botao-Panico-main\Servidor-Botao-Panico-main\Alerta.mp3")
        #path_audio = pathlib.Path("Alerta.mp3")
        
        # Obter o diretório onde o executável está localizado
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construir o caminho para o arquivo de áudio relativo ao executável
        audio_path = os.path.join(base_dir, 'Alerta.mp3')
        
        sound = pygame.mixer.Sound(audio_path)
        #sound = pygame.mixer.Sound(str(path_audio))

        # Cria um socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Associa o socket a uma porta
        sock.bind((IP_SERVIDOR, 8090))


        # coloca o socket em modo de escuta
        sock.listen(1)
        
        
   
        while self.servidor:
            try:
                # Aceita a conexao de um cliente
                connection, address = sock.accept()

                # Recebe a requisicao do cliente
                request = connection.recv(1024).decode()

                # Converte a string em um objeto bytes
                request_bytes = request.encode()

                # Escreve a requisicao no arquivo de log
                with log_file.open('a') as f:
                    log_entry = datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ' - ' + request + '\n'
                    f.write(log_entry)
                    f.flush()
       
                # Verifica de qual consultório veio a requisição de alerta
                match request:
                    case 'alerta,Consultorio1':
                        self.tela_consultorio1.config(foreground=self.cor_alerta)
                        # Play alert sound using Pygame (assuming sound object is created)
                        #sound = pygame.mixer.Sound(str(path_audio))  # Convert path to string for Pygame
                        sound.play()
                    case 'alerta,Consultorio2':
                        self.tela_consultorio2.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio3':
                        self.tela_consultorio3.config(foreground=self.cor_alerta)
                        #sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio4':
                        self.tela_consultorio4.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio5':
                        self.tela_consultorio5.config(foreground=self.cor_alerta)
                        #sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio6':
                        self.tela_consultorio6.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio7':
                        self.tela_consultorio7.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio8':
                        self.tela_consultorio8.config(foreground=self.cor_alerta)
                        #sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio9':
                        self.tela_consultorio9.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio10':
                        self.tela_consultorio10.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio11':
                        self.tela_consultorio11.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio12':
                        self.tela_consultorio12.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio13':
                        self.tela_consultorio13.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio14':
                        self.tela_consultorio14.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio15':
                        self.tela_consultorio15.config(foreground=self.cor_alerta)
                        #sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio16':
                        self.tela_consultorio16.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio17':
                        self.tela_consultorio17.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio18':
                        self.tela_consultorio18.config(foreground=self.cor_alerta)
                       # sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                    case 'alerta,Consultorio19':
                        self.tela_consultorio19.config(foreground=self.cor_alerta)
                        #sound = pygame.mixer.Sound(str(path_audio))
                        sound.play()
                        
                                        
                     # Envia uma resposta ao cliente
                connection.sendall('Chamado recebido!'.encode())             

                    # Envia uma resposta ao cliente
                connection.sendall('ERRO'.encode())

                # fecha a conexao com o cliente
                connection.close()

            except Exception as e:
                print('Erro no servidor:', e)

            

    #Altera a cor da tela "ConsultorioX" para preto e para de tocar o audio
    def receber_requisicao(self, sound):   

        # Algum som está tocando, pare-o
        pygame.mixer.stop()  # Pare o som específico
   
        # Muda a cor da tela para preto
        self.tela_consultorio1.config(foreground=self.cor_padrao)
        self.tela_consultorio2.config(foreground=self.cor_padrao)
        self.tela_consultorio3.config(foreground=self.cor_padrao)
        self.tela_consultorio4.config(foreground=self.cor_padrao)
        self.tela_consultorio5.config(foreground=self.cor_padrao)
        self.tela_consultorio6.config(foreground=self.cor_padrao)
        self.tela_consultorio7.config(foreground=self.cor_padrao)
        self.tela_consultorio8.config(foreground=self.cor_padrao)
        self.tela_consultorio9.config(foreground=self.cor_padrao)
        self.tela_consultorio10.config(foreground=self.cor_padrao)
        self.tela_consultorio11.config(foreground=self.cor_padrao)
        self.tela_consultorio12.config(foreground=self.cor_padrao)
        self.tela_consultorio13.config(foreground=self.cor_padrao)
        self.tela_consultorio14.config(foreground=self.cor_padrao)
        self.tela_consultorio15.config(foreground=self.cor_padrao)
        self.tela_consultorio16.config(foreground=self.cor_padrao)
        self.tela_consultorio17.config(foreground=self.cor_padrao)
        self.tela_consultorio18.config(foreground=self.cor_padrao)
        self.tela_consultorio19.config(foreground=self.cor_padrao)


def mainloop(self):
    self.root.mainloop()

if __name__ == '__main__':
    root = Tk()
    Application(root)
    root.mainloop()
