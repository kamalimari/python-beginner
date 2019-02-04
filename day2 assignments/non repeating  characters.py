a = str(input("enter the sequence"))
size = len(a)
b = []
if a[0] != a[1]:
    print(a[0])
if a[size - 2] != a[size - 1]:
    print(a[size - 1])
for i in range(1, size-3):
    if a[i-1] != a[i] and a[i] != a[i+1]:
        b.append(a[i])
print(b)
size2_ = len(b)
print(size2_)
for i in range(0, size2_-1):
    if b[i] == b[i+1]:
        k = b[i]
print(k)




