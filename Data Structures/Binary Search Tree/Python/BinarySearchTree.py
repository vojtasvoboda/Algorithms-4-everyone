from TreeNode import *

class BinarySearchTree:
    def __init__(self, root):
        """
        This constructor checks if the root is a TreeNode and if it is not
        it creates a new one with the data being the given root.
        """
        if not isinstance(root, TreeNode):
            root = TreeNode(root)
        self.root = root


    def insertNewNode(self, node, root=None):
        def _insertNewNode(root, node):
            """
            'node' is the node that is to be inserted in the tree.
            This function takes a node and a tree node and inserts it in that tree.
            it checks if the current node (the root) is None and if so it just
            returns 'node', if not it repeats the process but this time for the
            left subtree if node.data < root.data else it repeats it for the right
            subtree
            """
            if (root == None):
                return node

            elif (node.data < root.data):
                root.leftChild = _insertNewNode(root.leftChild, node)
                return root

            else:
                root.rightChild = _insertNewNode(root.rightChild, node)
                return root

        # If the root is None this means that the tree has no nodes (no root)
        if (root == None):
            root = self.root

        # If the input is not a TreeNode, Make it a TreeNode :)
        if not isinstance(node, TreeNode):
            node = TreeNode(node)

        # Call the helper method
        self.root = _insertNewNode(root, node)

    def preOrderTraversal(self, root=None):
        """
        This function traverses the tree in a way such it prints the root of the
        current tree first, repeats the process for the left subtree then the right one
        """
        def _preOrderTraversal(root):
            if (root == None):
                return

            print(root.data)
            _preOrderTraversal(root.leftChild)
            _preOrderTraversal(root.rightChild)

        # Initialize the root to pass it the helper method
        if (root == None):
            root = self.root

        # Call the helper method
        _preOrderTraversal(root)

    def inOrderTraversal(self, root=None):
        """
        Traverse the tree in a way such that it does not print a node unless it
        had printed every other node that was to the left of it. After printing
        that node it goes ot the right subtree and does the same
        """
        def _inOrderTraversal(root):
            if (root == None):
                return

            _inOrderTraversal(root.leftChild)
            print(root.data)
            _inOrderTraversal(root.rightChild)

        if (root == None):
            root = self.root
        _inOrderTraversal(root)

    def postOrderTraversal(self, root=None):
        """
        Traverses the tree in a way such that it does not print a node unless it
        had printed every other node to its right and to its left
        """
        def _postOrderTraversal(root):
            if (root == None):
                return

            _postOrderTraversal(root.leftChild)
            _postOrderTraversal(root.rightChild)
            print(root.data)

        if (root == None):
            root = self.root
        _postOrderTraversal(root)

    def getHeight(self, root=None):
        """
        Gets the height of the tree where the tree that consists of only one node
        (the root of the tree) has a height of zero.
        we mean by the height of the tree the longest branch (subtree) it has.
        The idea is simple, the height of any tree = the maximum between the height
        of the left and right subtree + 1.
        If a None value is reached then it has a length of -1, this means that the
        leaf that is before it has a height of zero
        """
        def _getHeight(root):
            if (root == None):
                return -1
            leftHeight = _getHeight(root.leftChild)
            rightHeight = _getHeight(root.rightChild)

            return 1 + max(leftHeight, rightHeight)

        if (root == None):
            root = self.root
        return _getHeight(root)


root = 5
bst = BinarySearchTree(root)
bst.insertNewNode(TreeNode(4))
bst.insertNewNode(TreeNode(8))
bst.insertNewNode(TreeNode(10))
bst.insertNewNode(TreeNode(1))
bst.insertNewNode(TreeNode('e'))
bst.insertNewNode(TreeNode(11))
bst.insertNewNode(TreeNode(9))
bst.insertNewNode(TreeNode('A'))
bst.insertNewNode(TreeNode('x'))

print("The height of the tree: " + str(bst.getHeight()))
print("-----------------------------")
print("In order traversal")
bst.inOrderTraversal()
print("------------------")
print("pre order traversal")
bst.preOrderTraversal()
print("------------------")
print("post order traversal")
bst.postOrderTraversal()
