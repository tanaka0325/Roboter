from .models.Restaurant import Restaurant


class Roboter(object):

    csv_file_name = 'data.csv'

    def __init__(self):
        self.model = Restaurant(self.csv_file_name)

    def start_conversation(self):
        user_name = self.ask_user_name()
        self.user_name = user_name

        if self.is_exists_top_restrant():
            self.ask_to_like_recommended_restaurant()

        favorite_restaurant = self.ask_favorite_restaurant()
        self.save_favorite_restaurant(favorite_restaurant)

        self.say_good_bye()

    def ask_user_name(self):
        return input("こんにちは！私はRobokoです。あなたの名前は何ですか？\n")

    def ask_favorite_restaurant(self):
        return input(self.user_name + "さん。どこのレストランが好きですか？\n")

    def save_favorite_restaurant(self, favorite_restaurant):
        self.model.save_restaurant(favorite_restaurant.capitalize())

    def is_exists_top_restrant(self):
        return bool(self.model.get_top_restaurant_name())

    def ask_to_like_recommended_restaurant(self):
        top_restaurant_name = self.model.get_top_restaurant_name()
        while True:
            answer = input("私のオススメのレストランは、" + top_restaurant_name +
                           'です。\nこのレストランは好きですか？ [Yes/No]').lower()
            if answer in ('yes', 'y'):
                self.save_favorite_restaurant(top_restaurant_name)
                break
            elif answer in ('no', 'n'):
                break
            else:
                print("YesかNoで答えてください\n")

    def say_good_bye(self):
        print(self.user_name + "さん。ありがとうございました。\n良い一日を！さようなら。")


def run():
    roboter = Roboter()
    roboter.start_conversation()
