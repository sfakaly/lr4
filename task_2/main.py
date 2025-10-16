#sfakaly
x = list(map(int, input("Введите список чисел через пробел: ").split())) # запрашивает список чисел
print(list(n**2 for n in x)) # выводит квадраты этих чисел