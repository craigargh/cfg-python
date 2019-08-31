from itertools import count


def run():
    has_key = False

    print('Try to escape the room')

    for turn in count(1):
        print('TURN {}'.format(turn))

        command = input('What do you want to do? ')
        info = split_command(command)

        action = info['action']
        item = info['item']

        if action == 'look' and item == 'room':
            print('You are in a room with a key and a door')

        elif action == 'look' and item == 'key':
            print('It is a key that opens a door')

        elif action == 'pickup' and item == 'key':
            print('You picked up the key')
            has_key = True

        elif not has_key and action == 'open' and item == 'door':
            print('The door is locked')

        elif has_key and action == 'open' and item == 'door':
            print('You leave the room. You win!')
            break

        else:
            print("I don't understand '{}'".format(command))

        print()

    print('You exited the room in {} turns'.format(turn))


def split_command(command):
    command = command.lower()
    separated_command = command.split(' ')
    action = separated_command[0]
    item = separated_command[1]

    return {
        'action': action,
        'item': item,
    }


run()
