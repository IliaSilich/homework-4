import random


def generate_password(length):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password_generator = (random.choice(chars) for _ in range(length))
    return ''.join(password_generator)


generated_password = generate_password(8)
print(f"Сгенерированный пароль: {generated_password}")
