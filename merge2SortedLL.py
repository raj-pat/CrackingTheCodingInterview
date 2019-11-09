class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode(-1)
    root = l3
    while (l1 != None and l2 != None):
        if l1.val < l2.val:
            l3.next = ListNode(l1.val)
            l1 = l1.next
        else:
            l3.next = ListNode(l2.val)
            l2 = l2.next
        print(l3.val)
        l3 = l3.next
    if l1 == None:
        l3.next = l2
    else:
        l3.next = l1

    return root.next
