while True:
    user_inputA = input('Введите значение стороны 1: ')
    if float(user_inputA)>0:
        user_inputB = input ('Введите значение стороны 2: ')
        if float(user_inputB)>0:
            s=float(user_inputA)*float(user_inputB)
        print ('Результат:',s)
        break
    else:
        print ('Вы ввели неверное значение.Повторите попытку!')
        continue