def every_three_nums(start):
  if start > 100:
    return []
  else:
    return list(range(start, 101, 3))

print(every_three_nums(1))

#Создает лист, который начинается с нашего заданного значения до 100, с промежутком в 3