# The previous implementation produced the wrong result. Let's fix the implementation by adjusting the way we create the tree.
import sys
sys.setrecursionlimit(10**6)
class TreeNode:
    def __init__(self, id=0, x=0, y=0, left=None, right=None):
        self.id = id
        self.x = x
        self.y = y
        self.left = left
        self.right = right

# Function to add a node to the tree
def add_node(parent, child):
    if child.x < parent.x:  # Go left
        if parent.left is None:
            parent.left = child
        else:
            add_node(parent.left, child)
    else:  # Go right
        if parent.right is None:
            parent.right = child
        else:
            add_node(parent.right, child)

# Function to build the tree
def build_tree(nodes):
    # Sort the nodes based on y descending and x ascending
    nodes.sort(key=lambda x: (-x[2], x[1]))
    root = TreeNode(id=nodes[0][0], x=nodes[0][1], y=nodes[0][2])

    for id, x, y in nodes[1:]:
        add_node(root, TreeNode(id=id, x=x, y=y))

    return root

# Preorder traversal of the tree
def preorder(node, traversal):
    if node:
        traversal.append(node.id)
        preorder(node.left, traversal)
        preorder(node.right, traversal)

# Postorder traversal of the tree
def postorder(node, traversal):
    if node:
        postorder(node.left, traversal)
        postorder(node.right, traversal)
        traversal.append(node.id)

# Main function to solve the problem
def solution(nodeinfo):
    # Enumerate the nodes with ids and sort based on y then x
    nodes = [(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    tree = build_tree(nodes)

    preorder_result = []
    postorder_result = []

    preorder(tree, preorder_result)
    postorder(tree, postorder_result)

    return [preorder_result, postorder_result]
