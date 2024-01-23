from snake import Snake
from turtle import Turtle,Screen
from food import Food
import time


screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.screensize(600,500)
food = Food()
screen.tracer(0)
snake = Snake()
game_on = True


screen.listen()
screen.onkey(snake.turn_left,"Left")
screen.onkey(snake.turn_right,"Right")
screen.onkey(snake.turn_up,"Up")
screen.onkey(snake.turn_down,"Down")


while game_on:
	snake.move()
	if snake.head.distance(food) <= 8:
		snake.add_segment()
		food.refresh()
		food.score()
	
	if snake.head.xcor() >= 325 or snake.head.ycor() >= 270 or snake.head.ycor() <= -270 or snake.head.xcor() <= -325:
		game_on = False
		food.gameover()
		
	if snake.collusion():
		game_on = False
		food.gameover()
	time.sleep(0.1)
	screen.update()
screen.exitonclick()

