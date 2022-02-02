def double_index(first, index):
  if index >=  len(first):
    return first
  new_list = first[0:index]
  new_list.append(first[index] * 2)
  new_list = new_list + first[index+1:]
  return new_list

print(double_index([3, 8, -10, 12], 2))

#Удваивает элемент заданного индекса в листе