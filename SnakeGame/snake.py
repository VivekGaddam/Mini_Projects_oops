from turtle import *
position=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.create()
    def create(self):
        for i in position:
            self.add_segment(i)
    def add_segment(self,i):
            v=Turtle()
            v.shape("square")
            v.color("red")
            v.penup()
            v.goto(i)
            self.segments.append(v)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for j in range(len(self.segments)-1,0,-1):
            new_x=self.segments[j-1].xcor()
            new_y=self.segments[j-1].ycor()
            self.segments[j].goto(new_x,new_y)
        self.segments[0].forward(20)
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    