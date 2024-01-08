letters = ["a", "b", "c"]
numbers = [1, 2, 3]
symbols = ["%", "$", "@"]

merge = zip(letters, numbers, symbols)

print(*list(merge), sep='\n')
