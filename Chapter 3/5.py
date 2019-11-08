# sort stack using one more stack
stack1 = [9, 8, 4, 1, 6, 3, 5]
stack2 = []  # tempStack

temp = None
pushPopCount = 0
# print(len(stack1))
while (len(stack1) != 0):
    ins = stack1.pop()
    print(ins)
    while (len(stack2) != 0):
        peek = stack2.pop(-1)
        print(peek)
        if peek < ins:
            stack1.append(peek)
            pushPopCount += 1
        else:
            stack2.append(peek)
            stack2.append(ins)
            break
    if len(stack2) == 0:
        stack2.append(ins)
    while (pushPopCount != 0):
        pushPopCount -= 1
        stack2.append(stack1.pop())
    print(stack1)
    print(stack2)
for elem in stack2:
    print(elem)
