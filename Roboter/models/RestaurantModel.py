import csv
import os


class RestaurantModel(object):

    fieldnames = ['NAME', 'COUNT']

    def __init__(self, csv_file_name):
        self.csv_file_name = os.path.join(os.getcwd(), csv_file_name)

        if not self.is_exists_csv_file():
            self.create_csv_file()

    def is_exists_csv_file(self):
        return os.path.exists(self.csv_file_name)

    def create_csv_file(self):
        with open(self.csv_file_name, 'w') as cf:
            writer = csv.DictWriter(cf, fieldnames=self.fieldnames)
            writer.writeheader()

    def save_restaurant(self, restaurant_name):
        # TODO 既に登録されているレストランだったらinsertではなくincrementする
        with open(self.csv_file_name, 'a') as cf:
            writer = csv.DictWriter(cf, fieldnames=self.fieldnames)
            writer.writerow({
                self.fieldnames[0]: restaurant_name.capitalize(),
                self.fieldnames[1]: 1
            })
