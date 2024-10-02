class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right

def main():
    tree_input = input("Enter tree nodes in level order (use 'None' for null nodes, separated by commas): ")
    tree_input = tree_input.split(',')
    tree_input = [int(x) if x != 'None' else None for x in tree_input]
    
    root = build_tree(tree_input)
    
    p_val = int(input("Enter the value of node p: "))
    q_val = int(input("Enter the value of node q: "))
    
    p_node = find_node(root, p_val)
    q_node = find_node(root, q_val)
    
    if not p_node or not q_node:
        print("One or both of the nodes are not found in the tree.")
        return
    
    lca = lowestCommonAncestor(root, p_node, q_node)
    
    print(f"The Lowest Common Ancestor of nodes {p_val} and {q_val} is: {lca.val}")

if __name__ == "__main__":
    main()
