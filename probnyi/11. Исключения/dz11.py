while True:
    string = input('Введите строку: ')
    String = string.split()
    try:
        f = int(String[0]) / int(String[1])
    except ZeroDivisionError:
        print('Произошла ошибка ZeroDivisionError!')
    except ValueError:
        print("Поддерживаются только числа")
    else:
        print(f)
        break
    print(String)
