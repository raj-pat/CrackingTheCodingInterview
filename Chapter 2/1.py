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


# To remove the duplicates from the linked list
def removeDup(startNode):
    currNode = startNode
    last = startNode
    buffer = []
    buffer.append(currNode.val)
    while (currNode != None):
        currDeleted = False
        if currNode.val in buffer:  # check if the value exist in the set. If it does, remove it
            last.next = currNode.next
            currDeleted = True
        else:
            buffer.append(currNode.val)
        if currDeleted is False:
            last = currNode
        currNode = currNode.next

    while (startNode != None):
        print(str(startNode.val) + "-> ", end="")
        startNode = startNode.next


removeDup(defLL([3, 3, 3, 3, 3, 3, 3, 3]))
