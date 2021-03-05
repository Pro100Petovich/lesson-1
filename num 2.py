print("Задача 2")
arr = []
i = 3
kub = 1
while i < 1000:
    arr.append(kub)
    kub = i ** 3
    i += 2
print(arr)

print("Пункт а: ")
summ = 0
r = 0
arr_2 = arr
for i in range(len(arr)):
    sum_2 = 0
    while arr[i] > 0:
        sum_2 += arr[i] % 10
        arr[i] // 10
    if sum_2 % 7 == 0:
        summ += arr_2[i]
    i +=1

print(summ)

print("Пункт b: ")
k = 0
r = 0
summ_2 = 0
arr_3 = arr_2
for k in range(len(arr_3)):
    arr_3[k] += 17
for r in range(len(arr_3)):
    sum_3 = 0
    while arr_3[r] > 0:
        sum_3 += arr_3[r] % 10
        arr_3[r] // 10
    if sum_3 % 7 == 0:
        summ_2 += arr_2[r]
    r += 1

print(summ_2)
