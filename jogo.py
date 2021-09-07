from tkinter.constants import W
from graphics import *
def main():
 win = GraphWin( "Jogo da Forca" , 500, 340)
 area = Rectangle(Point( 10,10),Point(290,130))
 retanguloBase = Rectangle(Point(65,115),Point(135,130))
 area.draw(win)
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
 
 
 win.getMouse() # Espera o click do mouse
 win.close() # Fecha a janela
     
if __name__ == "__main__":
 main()