from random import randint

for t in range(10):
    from random import randint


    def generate_list(target_sum, length):
        # Начинаем с генерации списка из случайных чисел
        answer = [randint(0, 10) for _ in range(length)]

        # Вычисляем текущую сумму
        current_sum = sum(answer)

        # Если сумма больше целевой, уменьшаем случайные элементы
        while current_sum != target_sum:
            if current_sum > target_sum:
                # Находим индекс элемента, который можно уменьшить
                index = randint(0, length - 1)
                # Уменьшаем элемент, если это возможно
                if answer[index] > 0:
                    answer[index] -= 1
            else:
                # Если сумма меньше, увеличиваем элемент
                index = randint(0, length - 1)
                if answer[index] < 10:
                    answer[index] += 1

            # Обновляем сумму
            current_sum = sum(answer)

        return answer


    # Генерируем список
    result = generate_list(10, 9)
    print(result)
    print("Сумма элементов:", sum(result))
