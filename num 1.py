print("Задача 1")
time = int(input("Duration :"))
if (time < 60):
    print(time, "сек")
elif (time >= 60) and (time < 3600):
    sec = time % 60
    min = time // 60
    print(min, "мин", sec, "сек")
elif (time >= 3600) and (time < 86400):
    sec=(time % 3600) % 60;
    min= (time % 3600)//60
    hours=time // 3600
    print(hours, "час", min, "мин", sec, "сек")
elif (time >= 86400) and (time < 2592000): #Я предпоположил, что в месяце 30 дней
    sec=((time % 86400) % 3600) % 60
    min=((time % 86400) % 3600) // 60
    hours=(time % 86400) // 3600
    days=time // 86400
    print(days, "дн", hours, "час", min, "мин", sec, "сек")
elif (time >= 2592000) and (time < 31536000):
    sec = (((time%2592000) % 86400) % 3600) % 60
    min = (((time%2592000) % 86400) % 3600) // 60
    hours = ((time % 2592000) % 86400) // 3600
    days = (time % 2592000) // 86400
    months = time // 2592000
    print(months, "мес", days, "дн", hours, "час", min, "мин", sec, "сек")
else :
    sec = ((((time % 31536000) % 2592000) % 86400) % 3600) % 60
    min = (((time % 31536000) % 2592000) % 86400) % 3600 // 60
    hours = ((time % 31536000) % 2592000) % 86400 // 3600
    days = (time % 31536000) % 2592000 // 86400
    months = time % 31536000 // 2592000
    years = time//31536000
    print(years, "год",months, "месяц", days, "дн", hours, "час", min, "мин", sec, "сек")
