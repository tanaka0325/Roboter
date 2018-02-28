from .models.RestaurantModel import RestaurantModel


class Roboter(object):

    csv_file_name = 'data.csv'

    def __init__(self):
        self.model = RestaurantModel(self.csv_file_name)

    def start_conversation(self):
        user_name = self.ask_user_name()
        self.user_name = user_name

        favorite_restaurant = self.ask_favorite_restaurant()
        self.save_favorite_restaurant(favorite_restaurant)

        self.say_good_bye()

    def ask_user_name(self):
        return input("こんにちは！私はRobokoです。あなたの名前は何ですか？\n")

    def ask_favorite_restaurant(self):
        return input(self.user_name + "さん。どこのレストランが好きですか？\n")

    def save_favorite_restaurant(self, favorite_restaurant):
        self.model.save_restaurant(favorite_restaurant)

    def say_good_bye(self):
        print(self.user_name + "さん。ありがとうございました。\n良い一日を！さようなら。")


def run():
    roboter = Roboter()
    roboter.start_conversation()
