# to remove the duplicates in the list
number = [1, 2, 5, 9, 6, 4, 1, 7, 3, 6]
uniques = []
for numbers in number:
    if numbers not in uniques:
        uniques.append(numbers)
print(uniques)

