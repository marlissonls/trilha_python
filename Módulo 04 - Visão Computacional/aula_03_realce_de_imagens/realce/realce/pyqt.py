import sys
from os.path import dirname
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100  # margem superior
        self.esquerda = 100 # margem esquerda
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(25, 25)
        self.caixa_texto.resize(220, 40)

        botao1 = QPushButton('Botão 1', self)
        botao1.move(100, 200)
        botao1.resize(150, 50)
        botao1.setStyleSheet('QPushButton {background-color: blue; font: bold; font-size: 20px}')
        botao1.clicked.connect(self.botao1_click)
        
        botao2 = QPushButton('Botão 2', self)
        botao2.move(300, 200)
        botao2.resize(150, 50)
        botao2.setStyleSheet('QPushButton {background-color: red; font: bold; font-size: 20px}')
        botao2.clicked.connect(self.botao2_click)

        botao_caixa = QPushButton('Botão Texto', self)
        botao_caixa.move(500, 200)
        botao_caixa.resize(150, 50)
        botao_caixa.setStyleSheet('QPushButton {background-color: green; font: bold; font-size: 20px}')
        botao_caixa.clicked.connect(self.mostra_texto)

        self.label_1 = QLabel(self)
        self.label_1.setText("Aperte algum botão")
        self.label_1.move(270, 100)
        self.label_1.resize(300, 35)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 25px; color: blue}')

        self.label_caixa = QLabel(self)
        self.label_caixa.setText("Digitou: ")
        self.label_caixa.move(270, 150)
        self.label_caixa.resize(400, 35)
        self.label_caixa.setStyleSheet('QLabel {font: bold; font-size: 25px; color: blue}')

        self.carro = QLabel(self)
        self.carro.move(20, 300)
        self.carro.resize(505, 260)
        self.carro.setPixmap(QPixmap(f'{dirname(__file__)}/images/azul.png'))
        # tudo que vai aparecer na tela tem que ser colocado antes de carregar a janela
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def botao1_click(self):
        self.label_1.setText("O carro 1 foi selecionado!")
        self.carro.setPixmap(QPixmap(f'{dirname(__file__)}/images/azul.png'))
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 25px; color: blue}')
    
    def botao2_click(self):
        self.label_1.setText("O carro 2 foi selecionado!")
        self.carro.setPixmap(QPixmap(f'{dirname(__file__)}/images/vermelho.png'))
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 25px; color: red}')

    def mostra_texto(self):
        conteudo = self.caixa_texto.text()
        self.label_caixa.setText("Digitou: " + conteudo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())