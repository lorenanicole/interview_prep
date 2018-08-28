## Binary Tree
class BinaryTree(object):
    """
    Ref: https://pythonschool.net/data-structures-algorithms/binary-tree/
    Ref: http://interactivepython.org/courselib/static/pythonds/Trees/TreeTraversals.html
    Ref: https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/
    """
    def __init__(self, val):
        self.root = val
        self.left_child = None
        self.right_child = None

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root(self):
        return self.root

    def set_root(self, val):
        self.root = val

    def add_right_child(self, val):
        if not self.get_right_child():
            self.right_child = BinaryTree(val)
        else:
            tree = BinaryTree(val)
            tree.right = self.get_right_child()
            self.right_child = tree

    def add_left_child(self, val):
        if not self.get_left_child():
            self.left_child = BinaryTree(val)
        else:
            tree = BinaryTree(val)
            tree.left = self.get_left_child()
            self.left_child = tree

    def preorder(self, ordered=None):
        if not ordered:
            ordered = '{}->'.format(self.get_root())
        else:
            ordered += '{}->'.format(self.get_root())
        print(ordered)
        if self.get_left_child():
            self.left_child.preorder(ordered)
        if self.get_right_child():
            self.right_child.preorder(ordered)

    def order(self, ordered=None):
        if self.get_left_child():
            self.left_child.order()
        if not ordered:
            ordered = '{}->'.format(self.get_root())
        else:
            ordered += '{}->'.format(self.get_root())
        print(ordered)
        if self.get_right_child():
            self.right_child.order()

    def postordered(self, ordered=None):
        if self.get_left_child():
            self.left_child.order()
        if self.get_right_child():
            self.right_child.order()
        if not ordered:
            ordered = '{}->'.format(self.get_root())
        else:
            ordered += '{}->'.format(self.get_root())
        print(ordered)

    def search(self, val):
        if self.get_root() == val:
            return self.root

        left_child = self.get_left_child()
        while left_child: # O(n)
            if left_child.get_root() == val:
                return left_child.root()
            left_child = left_child.get_left_child()

        right_child = self.get_right_child()
        while right_child:  # O(n)
            if right_child.get_root() == val:
                return right_child.get_root()
            right_child = right_child.get_right_child()

        return -1

tree = BinaryTree('Book')
tree.add_left_child('Chapter 1')
tree.add_right_child('Chapter 2')

tree.get_left_child().add_left_child('Section 1.1')
tree.get_left_child().add_right_child('Section 1.2')

# print(tree.preorder())
# print(tree.order())
# print(tree.postordered())

print(tree.search('Chapter 2'))


