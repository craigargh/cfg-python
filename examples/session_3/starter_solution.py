my_routine = ['wake up', 'shower', 'get the train', 'work', 'go home', 'eat', 'sleep']

days = ['mon', 'tues', 'wed', 'thurs', 'fri']

for day in days:
    print('Today is {}'.format(day))
    print('I need to')

    for item in my_routine:
        print(item)

    print('')