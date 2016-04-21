a = int(input('Please, enter the year:'))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('Високосный')
        else:
            print('Обычный')
    else:
        print('Високосный')
else:
    print('Обычный')
