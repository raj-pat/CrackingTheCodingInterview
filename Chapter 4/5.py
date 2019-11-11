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

def isBST(node, min, max):
    if node == None:
        return True
    if min != None:
        if node.val <= min:
            return False
    if max != None:
        if node.val >= max:
            return False
    return isBST(node.left, min, node.val) and isBST(node.right, node.val, max)


print(isBST(root, None, None))
