def string_reverse(string):
    reversed_str = string[::-1]
    return reversed_str


fruits = ["apple", "banana", "cherry"]
rev_fruits = map(string_reverse, fruits)
print(*list(rev_fruits), sep='\n')
