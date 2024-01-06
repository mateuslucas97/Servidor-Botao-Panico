
import socket
from threading import Thread
import time

from tkinter import *

IP_SERVIDOR = "192.168.0.51"

class Application():
    def __init__(self, root):
        self.root = root
        self.janela()
        self.tela()
        self.botao()
        self.cor_padrao = "black"
        self.cor_alerta = "red"
        self.servidor = True

        self.server_thread = Thread(target=self.start_server)
        self.server_thread.start()

    def janela(self):
        #cria a janela
        self.root.title("Servidor de Emergencias")
        self.root.configure(background = 'white')

        #cria a tela para exibir o texto "Consultorio1"
    def tela(self):
        self.tela_consultorio = Label(self.root, text="Consultorio1")
        self.tela_consultorio.place(x=5, y=5, width=100, height=85)
        self.tela_consultorio.config (font=("Arial", 13))

        #define o tamanho da tela para o padrao full HD 1920 x 1080
        largura = 800
        altura = 800
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura)  //2
        y = (altura_tela - altura) // 2
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

        self.root.resizable(False, False)

        #cria o botao "Stop"
    def botao(self):
        self.botao_stop = Button(self.root, text="Parar")
        self.botao_stop.config(font=("Arial", 20))
        self.botao_stop.place(x=5, y=100, width=100, height=50)


    def start_server(self):
        #Cria um socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #Associa o socket a uma porta
        sock.bind((IP_SERVIDOR, 8080))

        #coloca o socket em modo de escuta
        sock.listen(1)

        while self.servidor:
            try:
                #Aceita a conexao de um cliente
                connection, address = sock.accept()

                #Recebe a requisicao do cliente
                request = connection.recv(1024).decode()

                #verifica o tipo de requisicao
                if request == "alerta":

                    for i in range(10):
                    #altera a cor da tela para vermelho
                        self.tela_consultorio.config(foreground=self.cor_alerta)
                        time.sleep(0.1)
                        self.tela_consultorio.config(foreground=self.cor_padrao)
                else:
                    #altera a cor da tela para a cor padrao
                    self.tela_consultorio.config(foreground=self.cor_padrao)

                #envia uma resposta ao cliente
                connection.sendall("Chamado enviado!".encode())

                #fecha a conexao com o cliente
                connection.close()
            except Exception as e:
                print("Erro no servidor:", e)

    def parar_servidor(self):
        self.servidor = False

        # Verifica a cor da tela
        cor_tela = self.tela_consultorio.cget("foreground")

        # Altera a cor da tela para a cor padrão
        if cor_tela == self.cor_alerta:
            self.tela_consultorio.config(foreground=self.cor_padrao)

        # Continua o servidor em execução
        self.server_thread.start()

    

    def receber_requisicao(self, evento):
        if evento.data == "alerta":
            self.tela_consultorio.config(foreground=self.cor_alerta)
        else:
            self.tela_consultorio.config(foreground=self.cor_padrao)

    def mainloop(self):
        self.root.bind("<Button-1>", self.receber_requisicao)
        self.root.mainloop()

    def parar_piscar(self):
        self.tela_consultorio.config

if __name__ =="__main__":
    root = Tk()
    app = Application(root)
    app.tela()
    root.mainloop()