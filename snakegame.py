import turtle
import time
import random
delay=0.1
#setup screen
wn=turtle.Screen()
wn.title("game by shabab")
wn.setup(width=600,height=600)
wn.bgcolor("green")
wn.tracer(0)

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,200)

segments=[]

def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"
def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    if head.direction=="down":
        head.sety(head.ycor()-20)
    if head.direction=="left":
        head.setx(head.xcor()-20)
    if head.direction=="right":
        head.setx(head.xcor()+20)

#key assignment
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#main loop
while True:
    wn.update()
   #when snake touch food
    if head.distance(food)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        food.goto(x,y)
        # add new segments(snake body)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    #join last segment in reverse order
    for i in range(len(segments)-1,0,-1):
        x1=segments[i-1].xcor()
        y1=segments[i-1].ycor()
        segments[i].goto(x1,y1)
    #join oth segment to head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
    #check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    #check collisions for head with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(delay)

