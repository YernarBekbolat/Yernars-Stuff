def always_false(num):
  if num > 0 and num < 0:
    return True
  else:
    return False

print(always_false(0))

print(always_false(-1))

print(always_false(1))

#В этой функции результат всегда будет False, ибо мы создали невозможное условие, где цифра и больше, и меньше нуля