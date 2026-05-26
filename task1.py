from avl_tree import root, AVLNode


def find_min_recursive(tree:AVLNode) -> int:
    if not tree.left:
        return tree.key
    return find_min_recursive(tree.left)
print(find_min_recursive(root))


def find_min_iterative(tree:AVLNode):
    curr_node = tree
    while tree.left:
        curr_node = tree.left
        tree = tree.left
    return curr_node.key

print(find_min_iterative(root))
