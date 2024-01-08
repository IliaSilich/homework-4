def greeting(name):
    first_name, last_name = name.split()

    match last_name[-1]:
        case "я" | "а":
            print(f"Здравствуйте, госпожа {last_name}")
        case _:
            print(f"Здравствуйте, господин {last_name}")


full_name = input("Введите имя и фамилию: ")
greeting(full_name)
