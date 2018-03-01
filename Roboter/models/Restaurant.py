import csv
import os


class Restaurant(object):

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
        if self.find_by_restaurant_name(restaurant_name):
            self.increment_count(restaurant_name)
        else:
            with open(self.csv_file_name, 'a') as cf:
                writer = csv.DictWriter(cf, fieldnames=self.fieldnames)
                writer.writerow({
                    self.fieldnames[0]: restaurant_name,
                    self.fieldnames[1]: 1
                })

    def find_by_restaurant_name(self, restaurant_name):
        with open(self.csv_file_name, 'r') as cf:
            reader = csv.DictReader(cf)
            for row in reader:
                if row[self.fieldnames[0]] == restaurant_name:
                    return True
                    break

    def increment_count(self, restaurant_name):
        update_list = []
        with open(self.csv_file_name, 'r+') as cf:
            reader = csv.DictReader(cf)
            for row in reader:
                if row[self.fieldnames[0]] == restaurant_name:
                    d = {
                        self.fieldnames[0]: row[self.fieldnames[0]],
                        self.fieldnames[1]: int(row[self.fieldnames[1]]) + 1
                    }
                    update_list.append(d)
                else:
                    update_list.append(row)
            cf.seek(0)
            writer = csv.DictWriter(cf, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(update_list)

    def get_top_restaurant_name(self):
        top_restaurant = {}
        with open(self.csv_file_name, 'r') as cf:
            reader = csv.DictReader(cf)
            for row in reader:
                if top_restaurant:
                    if top_restaurant[self.fieldnames[1]] < row[self.
                                                                fieldnames[1]]:
                        top_restaurant = dict(row)
                else:
                    top_restaurant = dict(row)

        if top_restaurant:
            return top_restaurant[self.fieldnames[0]]
        else:
            return None
