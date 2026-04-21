# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(root: Node):
    # base
    rnode, lnode = 0, 0
    if root.left_child is None and root.right_child is None:
        return root.value 
    
    if root.right_child is not None:
        rnode = greatest_node(root.right_child)
        rnode = rnode if rnode > root.right_child.value else root.right_child.value 

    if root.left_child is not None:
        lnode = greatest_node(root.left_child)
        lnode = lnode if lnode > root.left_child.value else root.left_child.value

    return lnode if lnode > rnode else rnode
if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)
    tree.left_child.left_child.left_child = Node(3)
    tree.left_child.left_child.right_child = Node(1)

    tree.right_child = Node(4)
    tree.right_child.left_child = Node(6)
    tree.right_child.right_child = Node(11)
    tree.right_child.right_child.left_child = Node(13)
    tree.right_child.right_child.right_child = Node(12)
    

    print(greatest_node(tree))

# if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)
    print(greatest_node(tree))