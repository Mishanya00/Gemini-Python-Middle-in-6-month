def change1(x):
  print("x: ", x, " id: ", id(x))
  x = x + x
  print("x: ", x, " id: ", id(x))
  return x


def change2(a):
  print("ID: ", id(a), " a: ", a)
  a.append(1)
  print("ID: ", id(a), " a: ", a)

def change3(a):
  print("ID: ", id(a), " a: ", a)
  a = [2]
  print("ID: ", id(a), " a: ", a)


def change4(sequence):
  print("ID: ", id(sequence), "sequence: ", sequence)
  sequence.append(4)
  print("ID: ", id(sequence), "sequence: ", sequence)
  sequence = [0]
  print("ID: ", id(sequence), "sequence: ", sequence)
  print(" ")


var1 = 5
print("var1: ", var1, " id: ", id(var1))
var2 = change1(var1)
print("var1: ", var1, " id: ", id(var1))
print("var2: ", var2, " id: ", id(var2))

print('\n-------------------------------\n')

listA = [0]
print("Before change")
print("ID: ", id(listA), " listA: ", listA)

print("\nchange2()")
change2(listA)
print("ID: ", id(listA), " listA: ", listA)

print("\nchange3()")
change3(listA)
print("ID: ", id(listA), " listA: ", listA)

print("\nchange4()")
numberList = [1, 2, 3]
print("ID: ", id(numberList), "numberList: ", numberList)
print(" ")

change4(numberList)
print("ID: ", id(numberList), "numberList: ", numberList)