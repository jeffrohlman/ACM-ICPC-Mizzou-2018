num = 4
names = ["DEREK", "CHAD", "CHAE", "ADAM"]
status = ""
for i in range(1, num):
    if names[i] < names[i-1]:
        if status == "":
            status = "DECREASING"
        elif status == "INCREASING":
            status = "NEITHER"
            break
    else:
        if status == "":
            status = "INCREASING"
        elif status == "DECREASING":
            status = "NEITHER"
            break

print(status)
    
