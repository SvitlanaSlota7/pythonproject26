def fibonacci_search(arr, x):
    n = len(arr)

    # Найменше число Фібоначчі, яке >= n
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m2 + fib_m1

    while (fib_m < n):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    # Поки є елементи для перевірки
    while (fib_m > 1):
        i = min(offset + fib_m2, n - 1)

        if (arr[i] < x):
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif (arr[i] > x):
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i  # Знайдено!

    if (fib_m1 and offset + 1 < n and arr[offset + 1] == x):
        return offset + 1

    return -1

data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_fib = 72

result_fib = fibonacci_search(data, target_fib)

if result_fib != -1:
    print(f"Елемент {target_fib} знайдено за індексом {result_fib}")
else:
    print("Елемент не знайдено")