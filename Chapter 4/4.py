# Check if the tree is balanced

class node:
    def __init__(self, val):
        self.k = val
        self.left = None
        self.right = None


def isBalanced(root):
    if root == None:
        return 0
    print(root.k, end=" ")
    lh = isBalanced(root.left)
    rh = isBalanced(root.right)
    if lh == -1 or rh == -1:
        return -1
    if lh - rh not in [-1, 0, 1]:
        print("error")
        return -1
    else:
        return max(lh, rh) + 1


nod = []
for i in range(11):
    nod.append(node(i))
nod[0].left = nod[1]
nod[0].right = nod[2]
nod[1].left = nod[3]
nod[1].right = nod[4]
nod[2].left = nod[5]
nod[2].right = nod[6]
nod[3].left = nod[9]
nod[4].left = nod[7]
nod[5].right = nod[8]

# nod[7].left = nod[10]

print(isBalanced(nod[0]))
