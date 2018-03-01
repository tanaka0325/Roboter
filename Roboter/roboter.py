from .models.Restaurant import Restaurant
from .models.Robot import Robot


def start_conversation():
    robot = Robot()
    robot.say_hello()
    robot.recommend_restaurant()
    robot.ask_favorite_restaurant()
    robot.say_good_bye()
