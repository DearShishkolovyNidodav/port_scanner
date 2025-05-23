from random import randint
# Итоговый список с ответами
answer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Сумма всех ответов (не должна быть больше 10)
total_answer = sum(answer)
# Счётчик
counter = 0
print(f"Длина списка равна {len(answer)}")
# Работает пока сумма всех ответов меньше десяти и число итераций меньше длины списка
while sum(answer) < 10 and counter < len(answer):
    # Генерируем ответ
    current_answer = randint(0, 10)
    print(f"Получен ответ: {current_answer}")
    # Заносим ответ в список
    answer[counter] = current_answer
    # Проверяем, что сумма ответов меньше 10
    if sum(answer) >= 10:
        print(f"Общая сумма ответов равна: {sum(answer)}")
        answer[counter] = 0
        break
    # Увеличиваем счётчик
    counter += 1
    #print(total_answer)
print(answer)
print(sum(answer))
print(f"Счётчик: {counter}")
# Вычитаем из 10 сумму ответов и получившееся число заносим в список (чтобы итоговая сумма ответов равнялась десяти)
add_answer = 10 - sum(answer)
answer[counter] = add_answer
print("\n" * 10)
print(f"Итоговый ответ: {answer}")
print(f"Сумма итогового ответа: {sum(answer)}")