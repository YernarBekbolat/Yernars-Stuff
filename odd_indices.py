def odd_indices(first):
  new_list = []
  for index in range(0, len(first)):
    if index % 2 != 0:
      new_list.append(first[index])
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

#Выводит новый лист, где только элементы с нечётным индексом из прошлого листа