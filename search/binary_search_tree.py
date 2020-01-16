'''
This file contains algorithm of a binary  search tree and basic operations in it.

Reference: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
Written by Junzheng
1/13/2020
'''
class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if value > self.value:
            if self.right_child:
                self.right_child.insert(value)
            else:
                self.right_child = BinarySearchTree(value)
        else:
            if self.left_child:
                self.left_child.insert(value)
            else:
                self.left_child = BinarySearchTree(value)

    def in_order(self):

        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()



if __name__ == '__main__':
    b = BinarySearchTree(10)
    for i in range(10):
        b.insert(i)
    b.in_order()