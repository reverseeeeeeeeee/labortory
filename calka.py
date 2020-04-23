print("Калькулятор!\nФункции:умножение,деление,сложение,вычитание.")
flag = 1
while flag:
    x = float(input("Введите первое значение:"))
    y = float(input("Введите второе значение:"))

    command = input("Выберите действие:")

    if command == '+' :
        result = x + y
    elif command == '-' :
        result = x - y
    elif command == '*' : 
        result = x * y
    elif command == '/' : 
        if y == 0 :
            result = "Деление на ноль!"
        else :
            result = x / y 
    else:
        print("Ведено неправильная команда!Попробуйте еще!")
        continue
    print (result)

    for i in range(3):
        command = input("Продолжите?(Да/Нет)")
        if command == 'Да':
            flag = 1
            break
        elif command == 'Нет':
            flag = 0
            break
        if i == 2:
            flag = 0
        print("Введена неправильная команда!Скоро программа закроется)")
print("Выход!")