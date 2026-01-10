list1 = [1, 2, 3, 5]
list2 = [8, 9, 10]
X = 15
# Output = (5,10)


# O elevado ao quadrado porem funciona
def match_numbers(list1, list2, X):
    match = ()

    for number1 in list1:
        for number2 in list2:
            if number1 + number2 == X:
                match = (number1, number2)
    return match


print(match_numbers(list1, list2, X))