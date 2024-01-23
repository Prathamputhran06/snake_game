from turtle import Turtle
from random import randint

class Food(Turtle):
	
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.shapesize(0.5,0.5)
		self.color("red")
		self.penup()
		self.count = 0
		self.refresh()
		self.score_count = Turtle()
		self.score_count.hideturtle()
		self.score_count.penup()
		self.score_count.goto(0,265)
		self.score_count.color("white")
		self.score_count.pensize(100)
		self.score_count.write(f"score: {self.count}" , move=False, align='center', font=('Arial', 14, 'normal'))
		
	def refresh(self):
		x_cor = randint(0,248)
		y_cor = randint(0,248)
		self.goto(x_cor,y_cor)
	
	def score(self):
		self.count += 1
		self.score_count.clear()
		self.score_count.write(f"score: {self.count}" , move=False, align='center', font=('Arial', 14, 'normal'))
		
	def gameover(self):
		self.score_count.goto(0,0)
		self.score_count.write(f"GAME OVER!!!" , move=False, align='center', font=('Arial', 14, 'normal'))
		

