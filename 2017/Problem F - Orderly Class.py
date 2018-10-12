x = list(input())
y = list(input())

diffs = []

for i in range(0, len(x)):
    if x[i] != y[i]:
        diffs.append(i)
if len(diffs) == 1:
    print("0")
else:
    count = 0
    i = diffs[-1]
    j = diffs[0]
    x = x[0:j] + x[i:j-1:-1] + x[i+1:len(x)]
    if x == y:
        count = 1
        i += 1
        j -= 1
        while i < len(x) and j > -1:
            if x[i] == y[j] and x[j] == y[i]:
                count += 1
            i += 1
            j -= 1
        print(str(count))
    else:
        print("0")
        
