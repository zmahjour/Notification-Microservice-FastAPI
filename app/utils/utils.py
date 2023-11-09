import random


def create_otp():
    random_code = random.randint(1000, 9999)
    return random_code
