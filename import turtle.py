import turtle
import math
import random

wn=turtle.Screen()
wn.bgcolor("yellow")
wn.title("A MAZE GAME")
wn.setup(700,700)
wn.tracer(0)

#create pen
class Pen(turtle.Turtle):
    def _init_(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
class Player(turtle.Turtle) :
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)  
        self.gold=0 

    def go_up(self):
        move_to_x=self.xcor()
        move_to_y=self.ycor()+24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    

    def go_down(self):
        move_to_x=self.xcor()
        move_to_y=self.ycor()-24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        


    def go_left(self):
        move_to_x=self.xcor()-24
        move_to_y=self.ycor()
        self.shape("square")

        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_right(self):
        move_to_x=self.xcor()+24
        move_to_y=self.ycor()
        self.shape("square")
        
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def is_collison(self,other):
        a=self.xor()-other.xcor()
        b=self.yor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance <5:
            return True
        else:
            return False
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self) 
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=100 
        self.goto(x,y) 
    def destroy(self) :
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def _init_(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold=25
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])
    
    def move(self):
        if self.direction=="up":
            dx=0
            dy=24
        elif self.direction=="down":
            dx=0
            dy=-24
              
        elif self.direction=="left":
            dx=-24
            dy=0
            self.shape("triangle") 
        elif self.direction=="right":
            dx=24
            dy=0
            self.shape("triangle")
        else:
            dx=0  
            dy=0 


        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"
            elif player.xcor()>self.xcor():
                self.direction="right"
            elif player.ycor()<self.ycor():
                self.direction="down"
            elif player.xcor()>self.ycor():
                self.direction="up"              


        move_to_x=self.xcor()+dx
        move_to_y=self.ycor()+dy  

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)  
        else:
            self.direction=random.choice(["up","down","left","right"])
          
        turtle.ontimer(self.move,t=random.randint(100,300))

def is_close(self,other):
    a=self.xcor()-other.xcor()
    b=self.ycor()-other.ycor()
    distance=math.sqrt((a**2)+(b**2))

    if distance <75:
        return True
    else:
        return False
    


def destroy(self):
    self.goto(2000,2000)
    self.hideturtle()

#create level list
levels=[""]
#define first list
level_1=[
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXE         XXXXX",
"X  XXXXXX  XXXXXX  XXXXX",
"X      XX  XXXXXX  XXXXX",
"X      XX  XXX       EXX",
"XXXXXX XX  XXX        XX",
"XXXXXX XX  XXXXXX  XXXXX",
"XXXXXX XX    XXXX  XXXXX",
"X  XXX       XXXXT XXXXX",
"X  XXX XXXXXXXXXXXXXXXXX",
"X        XXXXXXXXXXXXXXX",
"X               XXXXXXXX",
"XXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXX   XXXXX  X",
"XXX  XXXXXXXXXX        X",
"XXXE                   X",
"XXX         XXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXX             X",
"XX    XXXX             X",
"XX    XXXXXXXXXX   XXXXX",
"XX      YXXXXXXX     XXXXX",
] 



treasures=[]  
enemies=[]     
#ADD MAZE TO MAZE LIST
levels.append(level_1)
#create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x=-288+(x*24)
            screen_y=288-(y*24)
            if character =="X":
                pen.goto(screen_x,screen_y)
                pen.shape("square")
                pen.stamp()
                walls.append((screen_x,screen_y))  
            if character=="P":
                player.goto(screen_x,screen_y)
            if character=="T":
                Treasure.append(Treasure(screen_x,screen_y))
            if character=="E":
                enemies.append(Treasure(screen_x,screen_y))  
pen=Pen() 
player=Player()
walls=[]
setup_maze(levels[1])
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

while True:
    for treasure in treasures :
        if player.is_collison(treasure):
            player.gold += treasure.gold
            print("Player Gold:{}".format(player.gold))   
        treasure.destroy()
        treasures.remove(treasure)
    for enemy in enemies:
        if player.is_collison(enemy):
            print("player dies")   
    wn.update()         






        
            

