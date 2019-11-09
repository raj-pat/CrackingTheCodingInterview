# check if the tree is BST

class node:
    def __init__(self, val):
        self.k = val
        self.left = None
        self.right = None


elems = [58, 4, 5, 7, 2, 8, 9, 1, 0]


def insert(root, nod):  # doesn't allow duplicates
    if nod.k < root.k:
        if root.left != None:
            insert(root.left, nod)
        else:
            root.left = nod
    elif nod.k > root.k:
        if root.right != None:
            insert(root.right, nod)
        else:
            root.right = nod


root = node(6)
for elem in elems:
    insert(root, node(elem))


# def inOrder(root):
#     if root == None:
#         return
#     inOrder(root.left)
#     print(root.k)
#     inOrder(root.right)
#

def isBST(root, min, max):
    if root != None:
        if min == None and max == None:  # At the root node
            if isBST(root.left, None, root.k) == -1:
                return -1
            if isBST(root.right, root.k, None) == -1:
                return -1

        if min != None:
            if root.k < min:
                return -1
        if max != None:
            if root.k > max:
                return -1
        if isBST(root.left, min, root.k) == -1:
            return -1
        elif isBST(root.right, root.k, max) == -1:
            return -1
    return 1


inOrder(root)
print("True") if isBST(root, None, None) == 1 else print("False")
