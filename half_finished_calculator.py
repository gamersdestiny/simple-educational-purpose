def calx():
    input1 = int(input(
'''
1 2 3
4 5 6
7 8 9
'''))
    operator = input('+ - * / \n')
    input2 = int(input(
'''
1 2 3
4 5 6
7 8 9
'''))
    print(input1, operator, input2, '=')
    if operator == '+':
        result = input1+input2
        print(result)
    elif operator == '-':
        result = input1-input2
        print(result)
    elif operator == '*':
        result = input1*input2
        print(result)
    elif operator == '/':
        result = input1/input2
        print(result)
    else:
        print('invalid input try again')
        calx()
calx()