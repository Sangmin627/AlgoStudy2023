import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def postOrder(self):
        if self.left != None:
            self.left.postOrder()
        if self.right != None:
            self.right.postOrder()
        print(self.data)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

binaryTree = Node(preorder[0])
for i in range(1, len(preorder)):
    binaryTree.insert(preorder[i])

binaryTree.postOrder()