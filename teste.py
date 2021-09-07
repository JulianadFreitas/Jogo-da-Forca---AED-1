from graphics import *
def main():
    chao=200
    raioBala=10
    
    win=GraphWin("Cannon Ball",500,230,autoflush=False)   
    linhaChao = Line(Point(0,chao),Point(500,chao))
    linhaChao.draw(win)
    cannonBall=Circle(Point(50,chao-raioBala),raioBala)
    cannonBall.setFill("black")
    cannonBall.draw(win)
    
    gravidade=[0,-0.2]
    vento=[0.01,0]
    vIni=[5,-5]
    
    dx=vIni[0]
    dy=vIni[1]
    while(cannonBall.getCenter().getY()+raioBala<=chao):
        cannonBall.move(dx,dy)
        dx=dx-gravidade[0]-vento[0]
        dy=dy-gravidade[1]-vento[1]
        update(30)
    
    win.getMouse()
    win.close()

if __name__=="__main__":
    main()