import CLI
import GUI


def menu():
    while True:
        try:
            user_in = int(input('Which would you like to use(CLI has less functions)\n1. CLI\n2. GUI\n'))
            if user_in == 1 or user_in == 2:
                return user_in
        except ValueError:
            print('Wrong input')


def run():
    num = menu()
    if num == 1:
        CLI.run()
    else:
        GUI.run()


run()
