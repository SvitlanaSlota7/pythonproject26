def binary_search_recursive(arr, low, high, x):
    # діапазон пошуку вичерпано
    if high >= low:
        mid = (high + low) // 2

        # Якщо елемент посередині
        if arr[mid] == x:
            return mid

        # Якщо елемент менший за середній, шукаємо в лівій частині
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)

        # Інакше шукаємо в правій частині
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        # Елемент не знайдено
        return -1

data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search_recursive(data, 0, len(data) - 1, target)

print(f"Binary Search: Елемент {target} знайдено за індексом {result}")