while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
    except ValueError:
        print('Введите число.')
        continue

    try:
        operation = input('Введите операцию: (/, +, -, *): ')

        if operation == '/':
            print(a / b)
        elif operation == '+':
            print(a + b)
        elif operation == '-':
            print(a - b)
        elif operation == '*':
            print(a * b)
        else:
            print('Неизвестная операция.')

    except ZeroDivisionError:
        print('Деление на ноль')

    print('Если хотите выйти, напишите: stop, чтобы продолжить: go')
    user = input('Введите действие: ')

    if user == 'stop':
        break






