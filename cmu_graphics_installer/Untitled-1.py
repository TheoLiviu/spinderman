

from cmu_graphics import*
import math
app.stepsPerSecond=100
plfrm=Group(Rect(60,80,60,10,fill='brown'),
            Rect(270,190,60,10,fill='brown'),
            Rect(110,320,60,10,fill='brown'))

healthbar= Group(Oval(315,10,14,20, rotateAngle=-30, fill='red'),Oval(325,10,14,20, rotateAngle=30, fill='red'),Polygon(320,25, 306,10, 334, 10, fill='red'))


app.step=0 
ball=Rect(200,270,60,10,fill='brown')
ball2=Rect(300,350,60,10,fill='brown')
plfrm.add(ball)
plfrm.add(ball2)
ball.dx=-1
app.step=0
app.x=0
app.y=0

rope=Line(0,0, 200,300, fill='red')
player= Circle(200,200,30,fill='black')
app.speed=0
app.angle=0
app.z=0
app.g=2
def onStep():
   
    app.speed= (app.step)**(1/2)
    app.step+=1
    timer=app.step/10
    app.z=timer*app.g
    if player.hitsShape(plfrm):
        player.centerY+=10
    
    rope.x1=player.centerX
    rope.y1=player.centerY
    length=((rope.y2-rope.y1)**2+(rope.x2-rope.x1)**2)**(1/2)
    cosAngle=((rope.x2-player.centerX)**2)**(1/2)/length
    app.angle=math.asin(cosAngle)*(180/math.pi)
    print(app.z)
    
    
    
    
    
    for i in plfrm:
        if i.centerX==-30:
           i.centerX=randrange(430,470)
           i.centerY=randrange(50,350)
def onMouseMove(mouseX,mouseY):
    app.y=mouseY
    app.x=mouseX
    rope.x2=mouseX
    rope.y2=mouseY
    
def onKeyHold(keys):
    if'a'in keys:
        player.centerX-=4
        
    elif'd'in keys:
       player.centerX+=4
    elif'w'in keys and rope.y1>rope.y2:
       player.centerY-=4
       app.step=0
    if 'space' in keys and player.centerX!=rope.x2:
       app.z=0
       player.centerX+= app.speed*math.cos((player.rotateAngle)*math.pi/180)
       player.centerY+= app.speed*math.sin((player.rotateAngle)*math.pi/180)
       player.rotateAngle= app.angle
    if 'r' in keys:
       player.centerX=200
       player.centerY=200

plfrm.clear()

cmu_graphics.run()