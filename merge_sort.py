# Функция для сортировки слиянием
def merge_sort(nums):
    # Функция будет работать только если длина списка больше одного (чтобы не было проблем с индексами)
    if len(nums) > 0:
        # Получаем середину списка
        middle = len(nums) // 2
        # Создаем новый список, состоящий из элементов от начала до середины nums
        left = nums[:middle]
        # То же самое, но от середины до конца nums
        right = nums[middle:]
        # ААААА!!!!! Это РЕКУРСИЯ!!!
        merge_sort(left)
        merge_sort(right)
        # i - индекс в списке left; j - индекс в списке right; k - индекс в списке nums (исходном)
        i = j = k = 0

        # Magic! (Нет, серьёзно, а как это работает?)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # На случай если в right ещё остались элементы
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        # На случай если в left ещё остались элементы
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

nums = [5, 86, 99, 1, 15, 81, 45, 12]
merge_sort(nums)
print(nums)