from avl_tree import AVLNode, root


def get_total_sum_iter(tree:AVLNode):
    stack = [tree]
    sum = tree.key
    while stack:
        node = stack.pop()
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
        sum += node.key
    return sum
print(get_total_sum_iter(root))

def get_total_sum_rec(tree:AVLNode, sum) -> int:
    if not tree:
        return sum
    get_total_sum_rec(tree.right, sum=sum+tree.key)
    get_total_sum_rec(tree.left, sum=sum+tree.key)
    return sum



print(get_total_sum_rec(root, root.key))


