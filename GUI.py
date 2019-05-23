from tkinter import *

root = Tk()
main_frame = Frame(root)
display_frame = Frame(main_frame, bg="dark grey", width=500, height=100)
sign_frame = Frame(main_frame)
button_frame = Frame(main_frame)
label = Label(display_frame, text="Enter an equation", bg="dark grey")
button_plus = Button(sign_frame, text="+", width=14, command=lambda: button_event('+'))
button_minus = Button(sign_frame, text="-", width=14, command=lambda: button_event('-'))
button_mult = Button(sign_frame, text="X", width=14, command=lambda: button_event('X'))
button_div = Button(sign_frame, text="/", width=15, command=lambda: button_event('/'))
button_sqrt = Button(sign_frame, text="sqrt|", width=15, command=lambda: button_event('sqrt| '))
button_pow = Button(sign_frame, text="^", width=15, command=lambda: button_event('^'))
button_fact = Button(sign_frame, text="!", width=15, command=lambda: button_event('!'))
button_clear = Button(sign_frame, text="Clear", width=15, command=lambda: button_event('cl'))
button1 = Button(button_frame, text="1", width=20, height=10, bg="grey", command=lambda: button_event('1'))
button2 = Button(button_frame, text="2", width=20, height=10, bg="grey", command=lambda: button_event('2'))
button3 = Button(button_frame, text="3", width=20, height=10, bg="grey", command=lambda: button_event('3'))
button4 = Button(button_frame, text="4", width=20, height=10, bg="grey", command=lambda: button_event('4'))
button5 = Button(button_frame, text="5", width=20, height=10, bg="grey", command=lambda: button_event('5'))
button6 = Button(button_frame, text="6", width=20, height=10, bg="grey", command=lambda: button_event('6'))
button7 = Button(button_frame, text="7", width=20, height=10, bg="grey", command=lambda: button_event('7'))
button8 = Button(button_frame, text="8", width=20, height=10, bg="grey", command=lambda: button_event('8'))
button9 = Button(button_frame, text="9", width=20, height=10, bg="grey", command=lambda: button_event('9'))
button_point = Button(button_frame, text=".", width=20, height=10, bg="gray", command=lambda: button_event('.'))
button_equal = Button(button_frame, text="=", width=20, height=10, bg="gray", command=lambda: button_event('='))
button0 = Button(button_frame, text="0", width=20, height=10, bg="grey", command=lambda: button_event('0'))


def run():
    label.place(relx=.1, rely=.1, relheight=0.8, relwidth=0.8)
    button_plus.grid(row=0, padx=5, pady=5)
    button_minus.grid(row=0, column=1, padx=5, pady=5)
    button_mult.grid(row=0, column=2, padx=5, pady=5)
    button_div.grid(row=0, column=3, padx=5, pady=5)
    button_sqrt.grid(row=1, padx=5, pady=5)
    button_pow.grid(row=1, column=1, padx=5, pady=5)
    button_fact.grid(row=1, column=2, padx=5, pady=5)
    button_clear.grid(row=1, column=3, padx=5, pady=5)
    button1.grid(row=0, padx=5, pady=5)
    button2.grid(row=0, column=1, padx=5, pady=5)
    button3.grid(row=0, column=2, padx=5, pady=5)
    button4.grid(row=1, padx=5, pady=5)
    button5.grid(row=1, column=1, padx=5, pady=5)
    button6.grid(row=1, column=2, padx=5, pady=5)
    button7.grid(row=2, padx=5, pady=5)
    button8.grid(row=2, column=1, padx=5, pady=5)
    button9.grid(row=2, column=2, padx=5, pady=5)
    button_point.grid(row=3, padx=5, pady=5)
    button_equal.grid(row=3, column=2, padx=5, pady=5)
    button0.grid(row=3, column=1, padx=5, pady=5)
    main_frame.pack()
    display_frame.pack(padx=20, pady=20)
    sign_frame.pack()
    button_frame.pack(pady=20)

    root.mainloop()


def button_event(event):
    if event != '=' and event != "cl" and not is_sign(event):
        if label.cget('text').startswith('Enter'):
            label['text'] = event
        else:
            label['text'] = label.cget('text') + event
    elif is_sign(event):
        label['text'] = label.cget('text') + ' ' + event + ' '
    elif event == "cl":
        label['text'] = ''
    elif event == '=':
        ans = get_answer(label.cget('text'))
        label['text'] = label.cget('text') + '\n' + ('__' * len(label.cget('text')))
        label['text'] = label.cget('text') + '\n' + ans


def is_sign(input_txt):
    if input_txt == '+' or input_txt == '-' or input_txt == '/' or \
       input_txt == 'X' or input_txt == '^' or input_txt == '!':
        return True
    return False


def get_answer(equation):
    ting = equation.split()
    try:
        if len(ting) == 2:
            if ting[1] == '!':
                return str(fact(int(ting[0])))
            else:
                return str(sq_rt(int(ting[1])))
        elif len(ting) == 3:
            num1 = int(ting[0])
            sign = ting[1]
            num2 = int(ting[2])
            if sign == '+':
                return str(add(num1, num2))
            elif sign == '-':
                return str(sub(num1, num2))
            elif sign == '/':
                return str(div(num1, num2))
            elif sign == '^':
                return str(power(num1, num2))
            else:
                return str(mlt(num1, num2))
        else:
            return 'Invalid input'
    except ValueError:
        return 'Invalid input'


def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    return x/y


def mlt(x, y):
    return x*y


def sq_rt(num):
    return num ** .5


def power(num, exp):
    if exp == 0:
        return 1
    return num * power(num, exp-1)
