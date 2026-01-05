import copy

original = [1, 2, [3, [3,4,5,6], 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

print(original)
print(shallow)
print(deep)

for item in original:
    print(id(item), end=' ')

# Though print is the same, ids are different in shallow and deep and in shallow this id is the same as in the original
print()
for item in shallow:
    print(id(item), end=' ')

print()
for item in deep:
    print(id(item), end=' ')
