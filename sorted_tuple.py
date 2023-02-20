a =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
n = len(a)

for i in range(n):
  for j in range(0, n - i - 1):
    if a[j][-1] > a[j + 1][-1]:
      a[j], a[j + 1] = a[j + 1], a[j]

print(a)