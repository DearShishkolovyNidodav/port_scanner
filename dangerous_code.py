import sys

#sys.setrecursionlimit(2000)  # Увеличиваем лимит

num = 100

def infinite_recursion():
    global num
    print(f"Вызов функции {num}")
    a = 1234567
    b = a ** a
    num += 1
    sys.setrecursionlimit(num)
    infinite_recursion()  # Рекурсивный вызов

infinite_recursion()  # Раскомментируйте, чтобы запустить
