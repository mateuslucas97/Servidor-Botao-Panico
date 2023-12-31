import socket
import pyaudio
import wave
from threading import Thread
from tkinter import *


IP_SERVIDOR = '10.16.90.122'
stream = None

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
        # cria a janela
        self.root.title('Servidor de Emergencias')
        self.root.configure(background='white')

        # cria a tela para exibir o texto "Consultorio1"

    def tela(self):
        self.tela_consultorio = Label(self.root, text='Consultorio1')
        self.tela_consultorio.place(x=5, y=5, width=100, height=85)
        self.tela_consultorio.config(font=('Arial', 13))

        # define o tamanho da tela para o padrao full HD 1920 x 1080
        largura = 800
        altura = 800
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.root.geometry(f'{largura}x{altura}+{x}+{y}')

        self.root.resizable(False, False)

        # cria o botao "Stop"

    def botao(self):
        self.botao_stop = Button(self.root, text='Parar')
        self.botao_stop.config(font=('Arial', 20))
        self.botao_stop.place(x=5, y=100, width=100, height=50)

        self.botao_stop.bind('<Button-1>', lambda event: self.receber_requisicao(event))

    def start_server(self):
        # Cria um socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Associa o socket a uma porta
        sock.bind((IP_SERVIDOR, 8080))

        # coloca o socket em modo de escuta
        sock.listen(1)

        while self.servidor:
            try:
                # Aceita a conexao de um cliente
                connection, address = sock.accept()

                # Recebe a requisicao do cliente
                request = connection.recv(1024).decode()

                # verifica o tipo de requisicao
                if request == 'alerta':

                    self.tela_consultorio.config(foreground=self.cor_alerta)

                    # Cria um objeto pyaudio
                    p = pyaudio.PyAudio()

                    # Abre o arquivo de audio
                    global stream  # Refere-se à variável global stream
                    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)

                    # Le o arquivo de audio
                    with wave.open('Servidor-Botao-Panico-main\Alerta.wav', 'rb') as wavfile:
                        (nchannels, sampwidth, framerate, nframes, comptype, compname) = wavfile.getparams()
                        audio_data = wavfile.readframes(nframes)

                    # Envia os dados do audio para o cliente
                    stream.write(audio_data)

                     # Envia uma resposta ao cliente
                    connection.sendall('Chamado recebido!'.encode())

                    # Altera o estado do botao para 'disabled'
                    self.botao_stop['state'] = 'disabled'

                else:
                    # Envia uma resposta ao cliente
                    connection.sendall('ERRO'.encode())

                # fecha a conexao com o cliente
                connection.close()
            except Exception as e:
                print('Erro no servidor:', e)


    def parar_servidor(self):
        self.servidor = False

        # Verifica a cor da tela
        cor_tela = self.tela_consultorio.cget('foreground')

        # Altera a cor da tela para a cor padrão
        if cor_tela == self.cor_alerta:
            self.tela_consultorio.config(foreground=self.cor_padrao)

        # Continua o servidor em execução
        self.server_thread.start()

    def receber_requisicao(self, event):
        # Declara a variavel global stream
        global stream
        #altera a cor da tela pra vermelho
        self.tela_consultorio.config(foreground=self.cor_alerta)
        
        # Altera o estado do botao para 'disabled'
        self.botao_stop['state'] = 'disabled'
        self.servidor = False

        # Declara a variavel stream
        stream = None

        # Tenta criar o stream de audio
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)
        except Exception as e:
            print('Erro ao criar o stream:', e)

        # Verifica se o stream já está em execução
        if stream and stream.is_active():
            # Fecha o stream de audio
            stream.close()

        # Altera o estado do botao para 'normal'
        self.botao_stop['state'] = 'normal'

    def mainloop(self):
        #self.root.bind('<Button-1>', self.receber_requisicao)
        self.root.mainloop()

    def parar_piscar(self):
        self.tela_consultorio.config


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    #app.tela()
    root.mainloop()

