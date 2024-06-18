# Поиск мин и макс длины имени строки из трех строк
s1 = input()
s2 = input()
s3 = input()
l1 = len(s1)
l2 = len(s2)
l3 = len(s3)
a = max(l1,l2,l3)
b = min(l1,l2,l3)
a2 = str(a)
b2 = str(b)
if min(l1,l2,l3)==l1:
    print(s1)
elif min(l1, l2, l3)==l2:
    print(s2)
elif min(l1,l2,l3)==l3:
    print(s3)
if max(l1,l2,l3)==l1:
    print(s1)
elif max(l1, l2, l3)==l2:
    print(s2)
elif max(l1,l2,l3)==l3:
    print(s3)


# a1 = 'MAX = ' + a2
# b1 = 'MIN = ' + b2
# print(a1)
# print(b1)