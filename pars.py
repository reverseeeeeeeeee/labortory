data={}
flag = True 
file = open('conf.txt', 'r')
for line in file:
    if line[0] not in ['#', ';', '\n']:
        list0 = line.split(' ', 1)
            
                
                
        x=len(list0)
        if x>1:
            key = list0[0]
            value = list0[1]
            data[key]= value
        elif x == 1:
            key = list0[0].rstrip('\n')
            value = "Значение не задано"
            data[key]= value                
while flag:
    try:
        key = input("Введите ключ: ")
        print ("Ключ:", key," \nЗначение:", data[key])   
    except:
        print("Ключ:", key," \nЗначение: Такого ключа не существует")
    
    for i in range(3):
        command = input("Продолжите?(y/n)")
        if command == 'y':
            flag = True
            break
        elif command == 'n':
            flag = False
            break
        if i == 2:
            flag = False
        print("Введена неправильная команда!Скоро программа закроется!")
print("Выход!")
