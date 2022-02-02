def remove_middle(first, start, end):
  return first[:start] + first[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Удаляет элементы листа в заданном промежутке 