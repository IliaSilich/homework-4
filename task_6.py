def sum_even_numbers(numbers):
    match numbers:
        case []:
            print("0")
        case [*num_list]:
            even_sum = 0
            for num in num_list:
                if num % 2 == 0:
                    even_sum += num
            print(even_sum)


input_numbers = input("Введите список чисел в формате [число1, число2, ...]: ")
sum_even_numbers(eval(input_numbers))
