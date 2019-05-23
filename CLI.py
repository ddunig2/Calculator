def get_input(format_n):
    if format_n == 1:
        while True:
            user_in = input('please enter an expression in this format(num + num)\nOr "End" to end\n')
            if user_in.lower() == 'end':
                print('goodbye :)')
                break
            split = user_in.split()
            try:
                num1 = int(split[0])
                num2 = int(split[2])
                if split[1] == '-':
                    print(num1 - num2)
                elif split[1] == '+':
                    print(num1 + num2)
                else:
                    print('expression not supported  please try a different one')
            except ValueError:
                print('re-enter expression')

    elif format_n == 2:
        while True:
            try:
                num1 = int(input('Enter the first number: '))
                sign = input('Enter the sign: ')
                num2 = int(input('Enter the second number: '))
                if sign == '-':
                    print(num1 - num2)
                elif sign == '+':
                    print(num1 + num2)
            except ValueError:
                print('please enter numbers')


def main_menu():
    while True:
        try:
            user_in = int(input('Please pick a format\n1. num + num\n2. enter num, enter operation, enter num\n'))
            if user_in == 1 or user_in == 2:
                return user_in
        except ValueError:
            print('Wrong input')


def run():
    get_input(main_menu())