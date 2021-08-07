#Вывод определённого количества четных чисел из последовательности Фибоначчи
def Fibonachi(x):
    if (x > 0) and type(x) == int:
        print("0")
        x-= 1
        num1 = 1
        num2 = 1
        while x != 0:
            x -= 1
            while num1 % 2 !=0:
                num1,num2 =num1+num2,num1
            print(num1)
            num1,num2 =num1+num2,num1
    else:
        print(" Неправильный ввод исходных данных. Попробуйте другое число")

Fibonachi(4)

