answer = 0

while True:
    input1 = input("Enter the First Number: ")
    if not input1:
        answer = 0
    else:
       input1 = float(input1)
    input2 = float(input("Enter the Second Number: "))
    operation = input("Enter the Operation: ")
    
    answer = 0
    
    if operation == "+":
        answer = input1+input2
    elif operation == "-":
        answer =input1-input2
    elif operation == "*":
        answer =input1*input2
    elif operation == "/":
        answer =input1/input2
    elif operation == "//":
        answer =input1//input2
    elif operation == "%":
        answer =input1%input2
    elif operation == "**":
        answer =input1**input2
    
    print(str(input1)+" "+str(operation)+" "+str(input2)+" = "+str(answer))
    
