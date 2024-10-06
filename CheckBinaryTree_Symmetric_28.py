class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True

    def isMirror(left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

    return isMirror(root.left, root.right)

def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if 2 * i + 1 < len(nodes):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def check_symmetric_tree():
    user_input = input("Enter the binary tree as an array (use 'null' for None): ")
    values = user_input.strip().split(",")
    values = [int(val) if val != 'null' else None for val in values]
    root = build_tree(values)
    result = isSymmetric(root)
    print("Output:", result)

check_symmetric_tree()
