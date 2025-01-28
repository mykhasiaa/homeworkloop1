print("Введіть 0 для завершення")
total = 0

while True:
    a = int(input("Введіть число: "))
    if a != 0:
        total += a
    else:
        break

print(f"Сума введених чисел: {total}")