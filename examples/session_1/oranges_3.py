oranges_string = raw_input('How many oranges do you want? ')

oranges = int(oranges_string)
cost_per_orange = 0.3

total_cost = oranges * cost_per_orange

output = str(oranges) + " oranges costs £" + str(total_cost)

print(output)
