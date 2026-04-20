# Pre-order traversal
def pre_order(node):
    result = []
    def traverse(current_node):
        if current_node is not None:
            result.append(current_node.data)
            traverse(current_node.left)
            traverse(current_node.right)

    traverse(node)
    return result


# In-order traversal
def in_order(node):
    result = []
    def traverse(current_node):
        if current_node is not None:
            traverse(current_node.left)
            result.append(current_node.data)
            traverse(current_node.right)

    traverse(node)
    return result


# Post-order traversal
def post_order(node):
    result = []
    def traverse(current_node):
        if current_node is not None:
            traverse(current_node.left)
            traverse(current_node.right)
            result.append(current_node.data)


    traverse(node)
    return result
