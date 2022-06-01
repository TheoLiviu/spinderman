
from random import randrange
from tkinter import Image, Label
from turtle import clear
from cmu_graphics import*
import math
app.stepsPerSecond=20
app.background=None



boss= Star(200, -60, 50, 20, fill='darkblue', border='black',borderWidth=2,roundness=90)
bosshealthbar= Rect(170, -5, 60,6, fill='green')
endprise=Label('Choose your reward', 200,200, size=40, visible=False)

wp=Group()
healthbar= Rect(335,10, 61,6, fill='green')
heart= Group(Oval(315,10,14,20, rotateAngle=-30, fill='red'),
                 Oval(325,10,14,20, rotateAngle=30, fill='red'),
                 Polygon(320,25, 306,10, 334, 10, fill='red'))

score=Label(0, 200,20, size=20)
wd=Label('Well done',200,200,size=40, fill='red', visible=False)
cr=Label('Choose your reward', 200,200, size=40, visible=False)

stars= Group(Star(randrange(0,400), randrange(0,400), 10, 5, fill='gold', border='orange',
     borderWidth=2), 
             Star(randrange(0,400), randrange(0,400), 10, 5, fill='gold', border='orange',
     borderWidth=2), 
             Star(randrange(0,400), randrange(0,400), 10, 5, fill='gold', border='orange',
     borderWidth=2))

instr=Label('Use SPACE to swing and W to climb up the rope, shoot with E when the boss comes', 200,100, fill='white', font='orbitron')
goal=Label('Collect as many stars as you can to save the world', 200, 140, fill='white')
start = Group()
start.add(Rect(0,0,400,400,fill='black'))
start.add(instr)
start.add(goal)
startbox = Group(Rect(150, 170, 100, 60, fill='gold', border='white'), 
                 Arc(250, 200, 50, 60, 0, 180, fill='gold', border='white'),
                 Arc(150, 200, 50, 60, 0, 180, fill='gold', border='white', rotateAngle=-180), 
                 Rect(248, 172, 5, 56, fill='gold'), 
                 Rect(148, 172, 5, 56, fill='gold'))
start.add(startbox)
start_text = Label('Start', start.centerX, start.centerY, size=25, fill='white', font='orbitron', bold=True)
start.add(start_text)
start.oh = startbox.height
start.ow = startbox.width

plfrm=Group(Star(randrange(420,430), randrange(0,400), 20, 20, fill='darkblue', border='black',borderWidth=2,roundness=90),
            Star(randrange(420,430), randrange(0,400), 20, 20, fill='darkblue', border='black',borderWidth=2,roundness=90))

rope=Line(0,0, 200,300, fill='red', opacity=0)
player=Circle(200,200,30,fill='black')
player2=Circle(200,200,30,fill='black', opacity=0)
rope2=Line(0,0,200,300,fill='red', opacity=0)
playerG= Group()
playerG.add(player)
playerG.add(player2)
playerG.add(rope)
playerG.add(rope2)

app.death=False
app.color=0
app.color2=255
app.step=0
app.x=0
app.y=0
app.angle=0
app.speed=0
app.angle=0
app.dx=4
app.timer=0
speed=6
app.start=False
app.dx2=4
rewards = Group(Circle(70,320,20, fill='green'),
               Star(129,320,20,5,fill='gold'),
               Star(189, 320, 20, 5, fill='red'),
               Oval(250, 320, 20,40, fill='magenta'),
               Arc(295, 320, 40, 20, 0,180,fill='cyan'))
rewards.visible=False

app.rect = [ ]




def spawnStars():
    for i in stars:
            i.centerX-=app.dx2
            if i.centerX<-10:
                i.centerX=randrange(410,450)
                i.centerY=randrange(0,400)
            if i.hitsShape(player):
                score.value+=1
                stars.remove(i)
                stars.add(Star(randrange(410,440), 
                            randrange(0,400), 
                            10, 5, fill='gold', 
                            border='orange',
                            borderWidth=2))

def gforce():
     
    if player.hitsShape(plfrm):
       for i in plfrm:
           i.opacity=100

    else:
        player.centerY+=app.timer**1/2
        player.centerX-=app.dx

def trigonometri():

    length=((rope.y2-rope.y1)**2+(rope.x2-rope.x1)**2)**(1/2)
    cosAngle=((rope.x2-player.centerX)**2)**(1/2)/length

    if cosAngle<1: 
        app.angle=math.asin(cosAngle)*(180/math.pi)

def playerPositioning():

    rope.x1=player.centerX
    rope.y1=player.centerY
    rope2.x1=rope.x2
    rope2.y1=rope.y2
    rope2.x2= app.x+rope.x2-rope.x1
    rope2.y2= app.y+rope.y2-rope.y1
    player2.centerX=rope2.x2
    player2.centerY=rope2.y2

def restartColorCount():

    if app.color>254:
       app.color=1
       app.color2=255
    
def obsRespawn():

    for i in plfrm:
        if i.centerX<-20:
           i.centerX=randrange(430,470)
           i.centerY=randrange(50,350)

def obsMove():

    for i in plfrm:
        i.centerX-=app.dx2

def playerDeath():
    
    if player.hitsShape(plfrm) and healthbar.width>1:
        healthbar.width=healthbar.width-1
    if healthbar.width==1:
        Label('Game Over',200,200,size=40, fill='red')
        app.death=True

def accelerate():

    if score.value>30 and app.dx <7:
       app.dx+=1/6

def bossOSMovement():
    
    for i in plfrm:
        i.centerY+= speed*math.cos((boss.rotateAngle)*math.pi/180)
        i.centerX+= speed*math.sin((boss.rotateAngle)*math.pi/180)
        if i.bottom>450:
            plfrm.remove(i)
            plfrm.add(Star(randrange(420,430), randrange(0,400), 20, 20, fill='darkblue', border='black',borderWidth=2,roundness=90))

def deactivateBoss():
        if player.centerX<=200:
            for i in wp:
                i.centerY-= speed*math.cos((app.angSpec)*math.pi/180)
                i.centerX+= speed*math.sin((app.angSpec)*math.pi/180)  
        else:
            for i in wp:
                i.centerY-= speed*math.cos((app.angSpec)*math.pi/180)
                i.centerX-= speed*math.sin((app.angSpec)*math.pi/180)

def reward():
    
    if boss.opacity==0:

        for cx in range(45, 335, 60):
            square = Rect(cx, 295, 55, 55, fill='grey', opacity=90)
            app.rect.append(square)

        for square in app.rect:
            if (square.contains(app.x, app.y) == True):
                square.fill = 'lightgrey'
            else:
                square.fill = 'grey'
        
        wd.visible=False
        wp.clear()
        endprise.visible=True
        cr.visible=True
        rewards.visible=True
        rewards.toFront()
        for i in rewards:
            if (i.contains(app.x, app.y) == True):
                i.width = 40
                i.height= 40
            else:
                i.width = 30
                i.height= 30

def chooseReward():
    
     for i in rewards:
            if (i.contains(app.x, app.y) == True):
                Rect(0,0,400,400,fill='white')
                endprise.visible=False
                cr.visible=False
                i.width = 50
                i.height= 50
                i.centerX=200
                i.centerY=200
                i.toFront()
                rewards.clear()
                rewards.add(i)
                rewards.toFront()
                Label('Yay!', 200,150, size=50)
                app.stop() 
          
def bossFight():
    
    if score.value>39:
        stars.clear()
        
        bosshealthbar.centerX=boss.centerX
        bosshealthbar.centerY=boss.centerY+54
        boss.rotateAngle+=3
      
        if boss.centerY<50:
            boss.centerY+=1

        for i in wp:
            if wp.hitsShape(boss) and bosshealthbar.width>1:
               bosshealthbar.width-=1
               wp.remove(i)

        if bosshealthbar.width==1:
            wd.visible=True
            bosshealthbar.visible=False
            if boss.opacity>=1:
               boss.opacity-=1
            if boss.opacity==0:
               wd.visible=False
               wp.clear()
    
        bossOSMovement()
        deactivateBoss()

def onStep():
    
    if app.start==False:

        start.toFront()

    if app.start==True:
        app.color+=1/5
        
        restartColorCount()
    
        app.background=rgb(app.color, 140, app.color2)
        app.speed= (app.step)**(1/2)
        app.step+=1
        app.timer=app.step/10
        
        accelerate()
        
        spawnStars()
            
        gforce()

        trigonometri()

        playerPositioning()

        obsMove()

        obsRespawn()

        playerDeath()

        bossFight()
    
def onMouseMove(mouseX,mouseY):
    reward()
    app.y=mouseY
    app.x=mouseX
    rope.x2=mouseX
    rope.y2=mouseY
    
def onKeyHold(keys):

    if'a'in keys and app.death==False:
        player.centerX-=4
        player2.centerX+=4

    elif'd'in keys and app.death==False:
       player.centerX+=4
       player2.centerX-=4

    elif'w'in keys and player.centerX>app.x and player.centerY>app.y and app.death==False:

       player.centerY-= speed*math.cos((app.angle)*math.pi/180)
       player.centerX-= speed*math.sin((app.angle)*math.pi/180)

    elif'w' in keys and player.centerX<app.x and player.centerY>app.y and app.death==False:

       player.centerY-= speed*math.cos((app.angle)*math.pi/180)
       player.centerX+= speed*math.sin((app.angle)*math.pi/180)

    if 'space' in keys and player.centerY>app.y and app.death==False:
        
       app.dx2=4+app.step**(1/3)
       playerG.rotateAngle-=app.step**(1/3)
       rope.opacity=100
       app.timer=0
       app.dx=0
       
    if 'r' in keys and app.death==False:

       playerG.centerX=200
       playerG.centerY=200

def onKeyPress(key):

    if key=='space':

        app.step=0

    if key == "e":
        
        app.angSpec=app.angle
        wp.add(Star(player.centerX, player.centerY, 10, 5, fill='gold', border='orange', borderWidth=2))

def onKeyRelease(key):

    rope.opacity=0
    app.dx=4
    app.dx2=4

def onMousePress(mouseX,mouseY):
    chooseReward()
    if start.hits(mouseX, mouseY):

        start.clear()
        app.start = True

cmu_graphics.run()