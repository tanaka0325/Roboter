import collections
import csv
import os
import pathlib

DEFAULT_CSV_FILE_PATH = 'data.csv'

RESTAURANT_COLUMN_NAME = 'NAME'
RESTAURANT_COLUMN_COUNT = 'COUNT'


class Restaurant(object):
    def __init__(self, csv_file=DEFAULT_CSV_FILE_PATH):
        self.csv_file = os.path.join(os.getcwd(), csv_file)
        self.columns = [RESTAURANT_COLUMN_NAME, RESTAURANT_COLUMN_COUNT]
        self.data = collections.defaultdict(int)

        if not os.path.exists(self.csv_file):
            pathlib.Path(self.csv_file).touch()

        self.load_data()

    def load_data(self):
        with open(self.csv_file, 'r') as cf:
            reader = csv.DictReader(cf)
            for row in reader:
                self.data[row[RESTAURANT_COLUMN_NAME]] = int(
                    row[RESTAURANT_COLUMN_COUNT])
        return self.data

    def save(self):
        with open(self.csv_file, 'w') as cf:
            writer = csv.DictWriter(cf, fieldnames=self.columns)
            writer.writeheader()
            for k, v in self.data.items():
                writer.writerow({
                    RESTAURANT_COLUMN_NAME: k,
                    RESTAURANT_COLUMN_COUNT: v
                })

    def increment(self, name):
        self.data[name.capitalize()] = self.data[name.capitalize()] + 1
        self.save()

    def get_most_popular(self, exclude_list=None):
        if exclude_list is None:
            exclude_list = []

        sorted_data_list = sorted(self.data, key=self.data.get, reverse=True)
        for name in sorted_data_list:
            if name in exclude_list:
                continue
            return name
