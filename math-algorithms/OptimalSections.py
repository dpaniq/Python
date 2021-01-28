"""
Число N принадлежит диапазону от 1 до 2000000. 
Границы отрезков – целые числа в диапазоне от -2^63 до 2^63.
Гарантируется, что левая граница каждого отрезка не превышает правую границу.

!!! Отрезки во входных данных перечислены в порядке возрастания их левой границы.
"""

# 1. Набор отрезков
# N = int(input('Введите N:\n'))
# print('Пример отрезка 1 5 или -20000 50000')
# sections = []
# while N:
#     sections.append(list(map(int, input('Введите отрезок: \n').split())))
#     N -= 1
# print(sections)

# Testing
sections = [[20, 30], [6, 10], [1, 5]]                               # Ответ 1 10 (new line) 20 30
sections = [[-40000000000, 20000000000], [10000000000, 30000000000]] # Ответ -40000000000 30000000000
sections = [[1,4], [3,5], [10, 14], [11, 13], [15, 16]]              # Ответ 1 5 (new line) 10 16

# 2. Сортировка элементов массива
sections.sort(key = lambda key: key[0])
print(sections)

# 3. Определение места отрезка [a,b], [c,d] для всех отрезков
# a = (_A_), b = (_B_), c = (_C_), d = (_D_)

result = []
while len(sections) > 1:
    _A_ = sections[0][0]
    _B_ = sections[0][1]
    _C_ = sections[1][0]
    _D_ = sections[1][1]
    print(f'::: SECTIONS: [{_A_},{_B_}] - [{_C_},{_D_}]:::')

    # 3.1. Промежуток a < c < b < d -> [a, d]
    if (
        _A_ < _C_ and
        _C_ < _B_ and
        _B_ < _D_
    ):
        sections = sections[2::]       # Удаляем первых два элемента массива
        sections.insert(0, [_A_, _D_]) # Вставляем в качестве первого элемента массива
        continue

    # 3.2. Промежуток a < c < d < b -> [a, b]
    if (
        _A_ < _C_ and
        _C_ < _D_ and
        _D_ < _B_
    ):
        sections = sections[2::]
        sections.insert(0, [_A_, _D_])
        continue

    # 3.3. Промежуток b == c-1 -> [a, d]
    if (
        _B_ == _C_ - 1
    ):
        sections = sections[2::]
        sections.insert(0, [_A_, _D_])
        continue

    # Если отрезки не могут быть объеденены
    result.append([_A_, _B_])
    sections.remove([_A_, _B_])

print("\n\n\nОтвет:")
result.extend(sections) # Складываем оба массива в один (или просто result + sections)
print(result)