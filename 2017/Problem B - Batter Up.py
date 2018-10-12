n = int(input())
n2 = n
ls = []
tot = 0

ls = list(map(int, input().split()))

for i in range(0, n):
    if ls[i] < 0:
        n2 = n2 - 1
    else:
        tot = tot + ls[i]

print((1.0 * tot)/n2)
