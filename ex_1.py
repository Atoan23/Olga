# Задача - преобразовать число в строку, содержащую звуки капель дождя, соответствующие определенным потенциальным факторам, т. е число, должно делится на другое число, не оставляя остатка. 
# Если заданное число делится без остатка на:
# 3 - добавляем "Pling" к результату.
# 5 - добавляем "Plang" к результату.
# 7 - добавляем "Plong" к результату.
# 3 и 5 – добавляем "Plingplang"
# 5 и 7 – добавляем "Plangplong"
# 7 и 3 – добавляем "Plongplang"
# не подходит ни одного из чисел, в качестве, результата выводится значение этого числа.

import random
raindrops = random.randint(0, 100)
if  raindrops % 3 == 0:
    if raindrops % 3 == 0 and raindrops % 5 == 0:
        print('plingplang')
        if raindrops % 3 == 0 and raindrops % 7 == 0:
            print ('plingplong')
    else:
        print('pling')
if  raindrops % 5 == 0:
    if raindrops % 5 == 0 and raindrops % 7 == 0:
        print('plangplong')
        if raindrops % 5 == 0 and raindrops % 3 == 0:
            print ('plangpling')
    else:
        print('plang')
if raindrops % 7 == 0:
    if raindrops % 7 == 0 and raindrops % 3 == 0:
        print ('plongpling')
        if raindrops % 7 == 0 and raindrops % 5 == 0:
            print ('plongplang')
    print ('plong')
else:
    print(raindrops)
        

