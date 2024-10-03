class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_level_order(arr, root, i, n):
    if i < n:
        if arr[i] is None:
            return None
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

def is_valid_bst(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)

def check_bst_from_input():
    arr = list(map(lambda x: int(x) if x != "None" else None, input("Enter the tree as a list (use 'None' for null nodes): ").split()))
    if not arr:
        return False
    root = insert_level_order(arr, None, 0, len(arr))
    return is_valid_bst(root)

result = check_bst_from_input()
print(result)
