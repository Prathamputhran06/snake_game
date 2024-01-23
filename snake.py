from turtle import Turtle,Screen


class Snake(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.segment = []
		self.segments()
		self.head = self.segment[0]
		self.penup()
		self.head.color("red")
		self.direction = 0
				
	def segments(self):
		y_cor = 0
		for i in range(3):
			new_segment = Turtle()
			new_segment.shape("turtle")
			new_segment.color("green")
			new_segment.speed(1)
			new_segment.shapesize(0.5,0.5)
			new_segment.penup()
			y_cor=y_cor - 10
			new_segment.goto(y_cor,0)
			self.segment.append(new_segment)
	
	def add_segment(self):
		new_segment = Turtle()
		new_segment.shape("turtle")
		new_segment.color("green")
		new_segment.speed(1)
		new_segment.shapesize(0.5,0.5)
		new_segment.penup()
		self.segment.append(new_segment)
	
	def move(self):
		for i in range(len(self.segment)-1,0,-1):
			x_cor = self.segment[i-1].xcor()
			y_cor = self.segment[i-1].ycor()
			self.segment[i].goto(x_cor,y_cor)
		self.head.forward(10)
					
	def turn_left(self):
		if self.direction == 270:
			self.direction = 180
		else:
			self.direction = (self.direction + 90) % 360
		self.head.setheading(self.direction)
		
	def turn_right(self):
		if self.direction == 270:
			self.direction = 0
		else:
			self.direction = (self.direction + 270) % 360
		self.head.setheading(self.direction)
		
	def turn_up(self):
		if self.direction == 180 or self.direction==0:
			self.direction = 90
			self.head.setheading(self.direction)
		
	def turn_down(self):
		if self.direction == 180 or self.direction==0:
			self.direction = 270
			self.head.setheading(self.direction)
			
	def collusion(self):
		for seg in self.segment:
			if seg == self.head :
				pass
			elif self.head.distance(seg) < 8:
				return True
			
			
		

