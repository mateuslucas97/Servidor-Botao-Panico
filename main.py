import os
import shutil
import socket
import playsound
import tempfile
from threading import Thread
from tkinter import *
from playsound import playsound


IP_SERVIDOR = '10.16.90.122'

class Application:
    def __init__(self, root):
        self.root = root
        self.janela()
        self.tela()
        self.botao()
        self.cor_padrao = 'black'
        self.cor_alerta = 'red'
        self.servidor = True

        self.server_thread = Thread(target=self.start_server)
        self.server_thread.start()

    def janela(self):
        self.root.title('Servidor de Emergencias')
        self.root.configure(background='white')

    def tela(self):
        self.tela_consultorio = Label(self.root, text='Consultorio1')
        self.tela_consultorio.place(x=5, y=5, width=100, height=85)
        self.tela_consultorio.config(font=('Arial', 13))

        largura = 600
        altura = 600
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.root.geometry(f'{largura}x{altura}+{x}+{y}')

        self.root.resizable(False, False)

    def botao(self):
        self.botao_stop = Button(self.root, text='Parar')
        self.botao_stop.config(font=('Arial', 20))
        self.botao_stop.place(x=5, y=100, width=100, height=50)

        self.botao_stop.bind('<Button-1>', self.receber_requisicao)

    def start_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((IP_SERVIDOR, 8080))
        sock.listen(1)

        while self.servidor:
            try:
                connection, address = sock.accept()

                request = connection.recv(1024).decode()

                if request == 'alerta':
                    self.tela_consultorio.config(foreground=self.cor_alerta)

                    # Reproduzir o áudio
                    playsound('Servidor-Botao-Panico-main\Alerta.wav')

                else:
                    connection.sendall('ERRO'.encode())

                connection.close()
            except Exception as e:
                print('Erro no servidor:', e)

    def receber_requisicao(self, event):
        self.tela_consultorio.config(foreground=self.cor_alerta)

        temp_dir = tempfile.mkdtemp()
        try:
            with open('Servidor-Botao-Panico-main\Alerta.wav', 'rb') as arquivo:
                if os.path.exists(arquivo.name):
                    stream = playsound(arquivo, block=True, tempdir=temp_dir)
                else:
                    raise FileNotFoundError
        finally:
            # Limpar o diretório temporário
            shutil.rmtree(temp_dir)

        # Muda a cor da tela para preto
        self.tela_consultorio.config(foreground=self.cor_padrao)

    def mainloop(self):
        self.root.mainloop()

