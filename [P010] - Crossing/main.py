import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
score = Scoreboard()


screen.listen()



screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_car()
    

    # Collision with the cars
    for cars in car.all_cars:
        if cars.distance(turtle) < 20:
            game_is_on = False
            score.game_over()
            
    # Finished 
    if turtle.is_at_finish_line():
        turtle.restart()
        car.level_up()
        score.level_up()

screen.exitonclick()