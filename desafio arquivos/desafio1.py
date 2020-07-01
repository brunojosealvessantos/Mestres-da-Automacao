#Desafio 1 - Módulo_4
import os

class Bot:
    def __init__(self):
        self.listaArquivos=[]
        self.listaEnderecos=[]

    def exibirArquivos(self):
        self.listaArquivos = os.listdir()
        for lista in self.listaArquivos:
            print(lista)

    def montarExibirCaminho(self):
        for nome in  self.listaArquivos:
            self.listaEnderecos = os.path.join(os.getcwd() + os.sep + nome)
            print(self.listaEnderecos)

    def acessarSubPasta(self, nome):
        os.chdir(nome)
        self.listaArquivos=[]
        self.listaEnderecos=[]
        print(os.getcwd())
        
    def sairSubPasta(self):
        os.chdir('..')
        self.listaArquivos=[]
        self.listaEnderecos=[]
        print(os.getcwd())
        
nivel = Bot()

#Exibindo Arquivos do Diretório 'desafio arquivos'
nivel.exibirArquivos()

#Montando e Exibindo o Caminho dos arquivos da pasta 'desafio arquivos'
nivel.montarExibirCaminho()
nivel.exibirArquivos()

#Acessando a subpasta 'desafios textos'
nivel.acessarSubPasta('desafios textos')

#Montando e Exibindo o Caminho dos arquivos da pasta 'desafio textos'
nivel.exibirArquivos()
nivel.montarExibirCaminho()

#Saindo da subpasta 'desafio textos'
nivel.sairSubPasta()

#Entrando novamente na pasta 'desafio textos'
nivel.acessarSubPasta('desafios textos')

#Saindo da subpasta 'desafio textos'
nivel.sairSubPasta()

#Saindo da subpasta 'desafio arquivos'
nivel.sairSubPasta()

