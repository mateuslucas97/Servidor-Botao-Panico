import datetime
import socket
import pygame

from threading import Thread
from tkinter import *


IP_SERVIDOR = '10.16.90.122'
stream = None

class Application:
    def __init__(self, root):
        self.root = root
        self.janela()
        self.tela()
        self.tela2()
        self.tela3()
        self.botao()
        self.botao2()
        self.botao3()
        self.cor_padrao = 'black'
        self.cor_alerta = 'red'
        self.servidor = True

        self.server_thread = Thread(target=self.start_server)
        self.server_thread.start()
        
    # cria a janela
    def janela(self):    
        self.root.title('Servidor de Emergencias')
        self.root.configure(background='white')

        # define o tamanho da tela para o padrao full HD 1920 x 1080
        largura = 600
        altura = 600
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.root.geometry(f'{largura}x{altura}+{x}+{y}')

        self.root.resizable(False, False)

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

    def start_server(self):
        log_file = open('log.txt', 'a')

        # Cria um socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Associa o socket a uma porta
        sock.bind((IP_SERVIDOR, 8080))

        # coloca o socket em modo de escuta
        sock.listen(1)

        #inicia o audio
        pygame.mixer.init()

        while self.servidor:
            try:
                # Aceita a conexao de um cliente
                connection, address = sock.accept()

                # Recebe a requisicao do cliente
                request = connection.recv(1024).decode()

                # Converte a string em um objeto bytes
                request_bytes = request.encode()

                # Escreve a requisicao no arquivo de log
                log_file.write(f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - {request}\n')
       
                # Verifica de qual consultório veio a requisição de alerta
                match request:
                    case 'alerta,Consultorio1':
                        self.tela_consultorio1.config(foreground=self.cor_alerta)
                    case 'alerta,Consultorio2':
                        self.tela_consultorio2.config(foreground=self.cor_alerta)
                    case 'alerta,Consultorio3':
                        self.tela_consultorio3.config(foreground=self.cor_alerta)
                        
                    # Cria um objeto pygame
                sound = pygame.mixer.Sound('Servidor-Botao-Panico-main\Alerta.wav')

                    # Toca o audio
                sound.play()
                
                     # Envia uma resposta ao cliente
                connection.sendall('Chamado recebido!'.encode())             

                #else:
                    # Envia uma resposta ao cliente
                connection.sendall('ERRO'.encode())

                # fecha a conexao com o cliente
                connection.close()

            except Exception as e:
                print('Erro no servidor:', e)

            # Não fecha o arquivo de log
            log_file.flush()
            

    #Altera a cor da tela "ConsultorioX" para preto e para de tocar o audio
    def receber_requisicao(self, sound):   
       
        # Algum som está tocando, pare-o
        pygame.mixer.stop()  # Pare o som específico

        # Muda a cor da tela para preto
        self.tela_consultorio1.config(foreground=self.cor_padrao)
        self.tela_consultorio2.config(foreground=self.cor_padrao)
        self.tela_consultorio3.config(foreground=self.cor_padrao)


def mainloop(self):
    self.root.mainloop()

if __name__ == '__main__':
    root = Tk()
    Application(root)
    root.mainloop()
