marks = []

while True:
    inp = input("Enter student mark {Type exit to when you are done}: ")
    if inp != "e":
        marks.append(inp)
    else:
        break

total = 0

for x in marks:
    total += float(x)

average = total/len(marks)

print("Average = "+str(average))

