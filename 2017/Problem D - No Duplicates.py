x = input().split()
x = sorted(x)
y = "yes"
for i in range(1,len(x)):
    if(x[i] == x[i - 1]):
        y = "no"
        break

print(y)
