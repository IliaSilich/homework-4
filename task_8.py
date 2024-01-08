def check_password_strength(password):
    if len(password) < 8:
        return "Пароль не надежный"

    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    digit_chars = "0123456789"
    symbol_chars = "!%@#$^&"

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char in uppercase_chars:
            has_uppercase = True
        elif char in lowercase_chars:
            has_lowercase = True
        elif char in digit_chars:
            has_digit = True
        elif char in symbol_chars:
            has_symbol = True

    if has_uppercase or has_lowercase or has_digit or has_symbol:
        return "Надежный пароль"
    else:
        return "Пароль не надежный"


pass_input = input('Введите пароль: ')
print(check_password_strength(pass_input))
