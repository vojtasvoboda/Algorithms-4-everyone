class TreeNode:
    """
    The node of a tree consists of the data which can be any object
    and its left and right children (if any)
    """
    def __init__(self, data, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild
