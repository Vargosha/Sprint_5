import random
import string


def generate_email():
    username = 'raguzin_egor_25_'
    domain = 'yandex.ru'
    numbers = random.randint(100, 999)
    return f'{username}{numbers}@{domain}'

def generate_password():
    characters = string.ascii_letters + string.digits
    length = random.randint(6,8)
    return ''.join(random.choice(characters) for _ in range(length))
