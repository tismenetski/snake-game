from turtle import  Turtle
import random
class Food(Turtle):  # Inheritance
    
    def __init__(self):
        super().__init__()  # Super
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10 * 10 circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))