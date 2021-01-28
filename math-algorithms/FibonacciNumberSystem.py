"""
    Считываем две строки.
    1. Количество цифр n (не учавствует в программе)
    2. Последовательность 0 и 1 равное n
"""
N = input('Введите N:\n') # 0 (или 5) (или 10) (...)
fibonacciNumberSystem = input('Введите последовательность 0 и 1:\n').split(' ') # 0 1 0 0 1 (или 1 0 1 0 1 0 0 1 0 0 0 1)

"""
    1. Действие первое:
    
    Если первый элемент массива 0, то меняем на 1
    Если первый элемент массива 1, а за ним 0, (то есть 10), то меняем на 01

    Исходя из выше сказаного, если элементов массива всего 1, всегда будет 1.
"""

if (len(fibonacciNumberSystem) == 1):
    print(1)
    exit()

if (fibonacciNumberSystem[0] == '0'):
    fibonacciNumberSystem[0] = '1'

if (fibonacciNumberSystem[0] == '1' and fibonacciNumberSystem[1] == '0'):
    fibonacciNumberSystem[0] = '0'
    fibonacciNumberSystem[1] = '1'

fibonacciNumberSystem = ''.join(fibonacciNumberSystem) # объеденям массив в одну строку (01001)
"""
    2. Действие второе:
    Заменяем последовательность 110 на 001, в каждой итерации цикла, до тех пор пока она есть.
"""
print()
while (True):
    fibonacciNumberSystem = fibonacciNumberSystem.replace('110', '001', 1) # меняем только 1 раз (третий аргумент)
    if not '110' in fibonacciNumberSystem: # Если 110 нет в строке, заканчиваем цикл
        break

print('Итоговая строка: ', ' '.join(fibonacciNumberSystem.split())) # Превращаем строку в формат 1 0 1 0 1 0 0 1 0 0 0 1 (символ через пробел)
