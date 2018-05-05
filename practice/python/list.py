numList1 = [1,2,3]
numList2 = [4,5,3]

print(numList1)
numList1.append("Kengo")
print(numList1)
del numList1[3]
print(numList1)

numList1.extend(numList2)
print(numList1)
print(numList1[::-1])

print(numList1.index(3))
print(numList1.count(3))

numList1.pop()
print(numList1)
