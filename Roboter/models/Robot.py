from .Restaurant import Restaurant

DEFAULT_ROBOT_NAME = 'Roboko'


class Robot(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        self.name = name
        self.user_name = user_name
        self.restaurant_model = Restaurant()

    def say_hello(self):
        user_name = input("こんにちは！私は" + self.name + "です。あなたの名前は何ですか？\n")
        self.user_name = user_name

    def recommend_restaurant(self):
        top_restaurant_name = self.restaurant_model.get_top_restaurant_name()
        if top_restaurant_name:
            while True:
                answer = input("私のオススメのレストランは、" + top_restaurant_name +
                               'です。\nこのレストランは好きですか？ [Yes/No]').lower()
                if answer in ('yes', 'y'):
                    self.restaurant_model.save_restaurant(top_restaurant_name)
                    break
                elif answer in ('no', 'n'):
                    break
                else:
                    print("YesかNoで答えてください\n")

    def ask_favorite_restaurant(self):
        favorite_restaurant = input(self.user_name + "さん。どこのレストランが好きですか？\n")
        self.restaurant_model.save_restaurant(favorite_restaurant.capitalize())

    def say_good_bye(self):
        print(self.user_name + "さん。ありがとうございました。\n良い一日を！さようなら。")
