# To delete the kth elem from the last
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def defLL(LL):
    last = Node(LL[0])
    first = last
    for val in LL[1:]:
        newNode = Node(val, None)
        last.next = newNode
        last = newNode
    return first


def delkth(k, startNode):
    currNode = startNode
    lastKNode = None
    kNode = None
    initial = True
    counter = 1
    if (k <= 0):
        return startNode
    while (currNode != None):
        if (counter == k and initial == True):
            kNode = startNode
            initial = False
        elif counter == k:
            lastKNode = kNode
            kNode = kNode.next
        else:
            counter += 1
        currNode = currNode.next
    if lastKNode != None:
        if kNode.next != None:
            lastKNode.next = kNode.next
        else:
            lastKNode.next = None
    else:
        startNode = kNode.next
    return startNode


start = delkth(6, defLL([1, 2, 3, 4, 5, 6]))
while (start != None):
    print(str(start.val) + "->", end="")
    start = start.next
