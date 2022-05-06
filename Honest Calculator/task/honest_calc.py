# write your code here
msg = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):", " ... lazy", " ... very lazy", " ... very, very lazy",
       "You are", "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0
store_res = 'n'  # store results
cont_calc = 'y'  # continue calculations
x = 0
y = 0
oper = '0'


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


def check(v1, v2, v3):
    message = ''
    if is_one_digit(v1) and is_one_digit(v2):
        message = message + msg[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        message = message + msg[7]
    if (v1 == 0 or v2 == 0) and (v3 in '+-*'):
        message = message + msg[8]
    if message != '':
        message = msg[9] + message
        print(message)


while cont_calc == 'y':
    if x == "M":
        x = memory
    if y == 'M':
        y = memory

    while oper not in '+-*/' or type(x) is not float or type(y) is not float:
        x, oper, y = input(f'{msg[0]}').split()
        error = 0
        if x == "M":
            x = memory
        if y == 'M':
            y = memory
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg[1])
        if oper not in '+-*/':
            print(msg[2])
            error += 1
        elif oper == '/' and y == 0:
            check(x, y, oper)
            print(msg[3])
            y = '0'
            error += 1


    # print result and go for another loop
    x = float(x)
    y = float(y)
    check(x, y, oper)
    if oper == "+":
        result = float(x + y)
    elif oper == "-":
        result = float(x - y)
    elif oper == "*":
        result = float(x * y)
    elif oper == "/":
        result = float(x / y)

    print(result)
    store_res = input(msg[4])

    while store_res not in 'ny' or store_res == '':
        store_res = input(msg[4])
    really = True
    if store_res == 'y':
        msg_index = 10
        while is_one_digit(result):
            store_res = input(msg[msg_index])
            if store_res == 'y':
                if msg_index < 12:
                    msg_index += 1
                    really = True
                else:
                    really = True
                    break
            elif store_res == 'n':
                really = False
                break

    if really:
        memory = result



    cont_calc = input(msg[5])
    while cont_calc not in 'ny' or cont_calc =='':
        cont_calc = input(msg[5])
    x = '0'
    y = '0'


# print(x, oper, y)
