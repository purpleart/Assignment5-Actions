import math
from datetime import date

def firstrun():
    return "success"


def calculate_area(radius):
    return math.pi * radius ** 2


def get_first_last_elements(my_list):
    return my_list[0], my_list[-1]


def get_delta_days(date1, date2):
    delta = date2 - date1
    return delta.days
