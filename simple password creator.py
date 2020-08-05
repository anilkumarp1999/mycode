import random
def passwordCreator():
    upper_case = ["A","B","C","D"]
    lower_case = ["a","b","c","d"]
    numbers = ["1","2","3","4"]
    special_chars = ["!","@","#","%"]
    password = random.choice(upper_case) + random.choice(lower_case) + random.choice(numbers) + random.choice(special_chars)

    password = password + password

    return password
print(passwordCreator())