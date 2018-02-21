cats_string = raw_input('How many cats do you need to feed? ')

cats = int(cats_string)
cans = 2

total_cans = cats * cans

output = "{} cats eat {} cans".format(cats, total_cans)
print(output)
