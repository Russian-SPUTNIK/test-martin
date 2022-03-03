a = [5, 8, 2, 6, 1]
for i in range(0, 5):
    if a[i] % 2 == 0:
        a[i] = 1
    else:
        a[i] = 0
print(a)
z = 0
h=5
for n in range(0,5):
        z = a[n] * 2 ** (h-1) + z
        h=h-1
print(z)
print("proba")