class Roboter(object):
    def start_conversation(self):
        user_name = self.ask_user_name()
        self.user_name = user_name

        self.say_good_bye()

    def ask_user_name(self):
        return input("こんにちは！私はRobokoです。あなたの名前は何ですか？\n")

    def say_good_bye(self):
        print(self.user_name + "さん。ありがとうございました。\n良い一日を！さようなら。")


def run():
    roboter = Roboter()
    roboter.start_conversation()
