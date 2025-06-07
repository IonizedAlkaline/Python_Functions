name = ("bob", "john", "steve")
roll_no = (3, 2, 1)

list3 = list(zip(name, roll_no))
print(list3)
list4 = [1, 2, 3]
# print(list4[::-1])
list5 = [100, 200, 300]
for x, y in zip(list4, list5[::-1]):
    print(x, y)
