import csv
import sys
import os


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        if '' in (brand, photo_file_name, carrying):
            raise ValueError

        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except ValueError as ex:
            raise ex
        self.ext = self.get_photo_file_ext()

    def get_photo_file_ext(self):
        _, extension = os.path.splitext(self.photo_file_name)
        if extension not in (".jpg", ".jpeg", ".png", ".gif"):
            raise ValueError
        return extension


class Car(CarBase):

    car_type = "car"

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            length, width, height = map(float, body_whl.split("x"))
            #print(length, width, height)
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        if extra == '':
            raise ValueError
        self.extra = extra


def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        car_list = []
        car_types = {
            'car': lambda x: Car(x[1], x[3], x[5], x[2]),
            'truck': lambda x: Truck(x[1], x[3], x[5], x[4]),
            'spec_machine': lambda x: SpecMachine(x[1], x[3], x[5], x[6])}

        for row in reader:
            #print(row)
            try:
                car_type = row[0]
                if car_type in car_types:
                    car_list.append(car_types[car_type](row))
            except Exception as ex:
                pass

    return car_list


if __name__ == '__main__':
    print(get_car_list(sys.argv[1]))

