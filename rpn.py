
truth = 1
Stack = list()
operands = ["+", "-", "/", "*"]
while(truth == 1):
    try:
        currentInput = input()
    except EOFError:
        break
    if (currentInput.isnumeric() == True):
        Stack.append(int(currentInput))
        print(int(currentInput))
    elif (currentInput == "+" and len(Stack) >= 2):
        num1 = Stack.pop()
        num2 = Stack.pop()
        Stack.append(num1 + num2)
        print(int(num1 + num2))
    elif (currentInput == "-"  and len(Stack) >= 2):
        num1 = Stack.pop()
        num2 = Stack.pop()
        Stack.append(num2 - num1)
        print(int(num2 - num1))
    elif (currentInput == "*"  and len(Stack) >= 2):
        num1 = Stack.pop()
        num2 = Stack.pop()
        Stack.append(num1 * num2)
        print(int(num1 * num2))
    elif (currentInput == "/" and len(Stack) >= 2):
        num1 = Stack.pop()
        num2 = Stack.pop()
        if (num1 == 0):
            print("invalid operation")
            Stack.append(num2)
            Stack.append(num1)
            continue
        else:
            Stack.append(num2 / num1)
        print(int(num2 / num1))
    elif (currentInput == "~" and len(Stack) >= 1):
        num1 = Stack.pop()
        Stack.append(num1 * -1)
        print(int(num1 * -1))
    else:
        print("invalid operation")
                
                                                

