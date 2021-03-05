print("Задача 3")
arr = []
i = int(input("Введите количество процентов, чтобы я выдал вам склонение : "))
if (i == 0) or (i >= 4):
    print(i, "Процентов")
elif i == 1:
    print(i, 'Процент')
else:
    print(i, "Процента")
k=0
print("Проверка:")
for k in range(21):
    if (k == 0) or (k >= 4):
        print(k, "Процентов")
    elif k == 1:
        print(k, 'Процент')
    else:
        print(k, "Процента")
