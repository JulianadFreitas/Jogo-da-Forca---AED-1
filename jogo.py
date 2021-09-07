from tkinter import Widget
from tkinter.constants import W
from graphics import *
import random

def main():
 a = random.randrange(1,10)
 b = random.randrange(1,10)
 c = random.randrange(1,10)
 d = random.randrange(0,10)
 x = random.choice(["+","-","*","/"])
 y = random.choice(["+","-","*","/"])
 z = random.choice(["+","-","*"])
 
 operadores = [x, y, z]
 operacao = str(str(a) + str(x) + str(b) + str(y) + str(c) + str(z ) + str(d))
 resultado = round(eval(operacao))
 operacaoNaTela = (str(str(a) + "__" + str(b) + "__"+ str(c) +"__"+ str(d) + " = ") + str(resultado))
 print(a,b, round(resultado), operacao, operacaoNaTela) 
 
 win = GraphWin( "Jogo da Forca" , 500, 340)
 area = Rectangle(Point( 10,10),Point(290,330))
 retanguloBase = Rectangle(Point(65,115),Point(135,130))
 area.draw(win)
 label = Text(Point(150, 180), 'Descrubra os operadores')
 label.draw(win) 
 label = Text(Point(150, 205), operacaoNaTela)
 label.draw(win) 
 retanguloBase.draw(win)
 cabeca = Circle(Point( 119.5,45), 5)
 cabeca.draw(win)
 
 linhaReta=Line(Point(100,115),Point(100,20))
 linhaReta.draw(win)
 linhaHorizontal=Line(Point(100,20),Point(120,20))
 linhaHorizontal.draw(win)
 linhaApoio=Line(Point(120,20),Point(120,40))
 linhaApoio.draw(win)
 
 corpo=Line(Point(120,50),Point(120,90))
 corpo.draw(win)
 
 bracoDireito=Line(Point(120,60),Point(130,70))
 bracoDireito.draw(win)
 bracoEsquerdo=Line(Point(120,60),Point(110,70))
 bracoEsquerdo.draw(win)
 
 peDireito=Line(Point(120,90),Point(130,100))
 peDireito.draw(win)
 peEsquerdo=Line(Point(120,90),Point(110,100))
 peEsquerdo.draw(win)

 # Expessura de linha
 retanguloBase.setWidth(2)
 linhaReta.setWidth(2)
 linhaHorizontal.setWidth(2)
 linhaApoio.setWidth(2)
 corpo.setWidth(2)
 bracoDireito.setWidth(2)
 bracoEsquerdo.setWidth(2)
 peDireito.setWidth(2)
 peEsquerdo.setWidth(2)
 
 # Cor da borda
 retanguloBase.setOutline("brown") 
 area.setOutline("brown") 
 cabeca.setOutline( "purple")

 # preenchimento
 win.setBackground('white')
 area.setFill("pink")
 retanguloBase.setFill("brown")
 cabeca.setFill( "purple")
 bracoDireito.setFill( "purple")
 bracoEsquerdo.setFill( "purple")
 corpo.setFill( "purple")
 peDireito.setFill( "purple")
 peEsquerdo.setFill( "purple")
 linhaReta.setFill( "brown")
 linhaHorizontal.setFill( "brown")
 linhaApoio.setFill( "brown")

 entrada= Entry(Point(200,150),1)
 entrada.draw(win)
 txt = Text(Point(200,180),1)
 txt.draw(win)
 txt.setText(entrada.getText())
 print(txt)
 mensagem = ""
 aviso = Text(Point(200,180),mensagem)
 aviso.draw(win)
 
 for i in range(0,3):
     if i ==3:
         mensagem="Você perdeu"
         txt.setText("")
     elif(txt == x):
         mensagem="Parabéns, você acertou. Agora digite o próximo operador"
         win.getMouse()
         txt.setText(mensagem.getText())
         win.getMouse()
 win.getMouse() # Espera o click do mouse
 win.close() # Fecha a janela
     
main()