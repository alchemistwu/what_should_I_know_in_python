'''
This file contains data structure of a binary tree and basic operations in it.

Reference: https://www.codementor.io/@leandrotk100/everything-you-need-to-know-about-tree-data-structures-pynnlkyud
Written by Junzheng
1/13/2020
'''

import random
from queue import Queue

class BinaryTree:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        '''
        Insert a child at the left of current node.
        :param value: The value of inserted node.
        :return: Nothing
        '''
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        '''
        Insert a child at the right of current node.
        :param value: The value of inserted node.
        :return: Nothing
        '''
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    # Depth first traverse

    def pre_order_traverse(self):
        print(self.value)
        if self.left_child:
            self.left_child.pre_order_traverse()
        if self.right_child:
            self.right_child.pre_order_traverse()

    def in_order_traverse(self):
        if self.left_child:
            self.left_child.in_order_traverse()
        print(self.value)
        if self.right_child:
            self.right_child.in_order_traverse()

    def post_order_traverse(self):
        if self.left_child:
            self.left_child.post_order_traverse()
        if self.right_child:
            self.right_child.post_order_traverse()
        print(self.value)

    # Width first traverse

    def breadth_first_traverse(self):
        q = Queue()
        q.put(self)
        while not q.empty():
            current_node = q.get()
            print(current_node.value)
            if current_node.left_child is not None:
                q.put(current_node.left_child)
            if current_node.right_child is not None:
                q.put(current_node.right_child)


class BinaryTreeTest:

    def __init__(self):
        self.binaryTree = self.create_tree()

    def create_tree(self, min=0, max=10, size=8):
        '''
        Function to create a random binary tree
        :return: A random binary tree
        '''
        nodes = []
        root = None

        for _ in range(size):
            nodes.append(random.randint(min, max))

        for node in nodes:
            if root is None:
                root = BinaryTree(node)
            else:
                place_to_insert = self.wandar(root)
                if random.random() > 0.5:
                    place_to_insert.insert_left(node)
                    print("=========================")
                    print("Place to insert: %d, left inserted value: %d" % (place_to_insert.value, node))
                    print("=========================")
                else:
                    place_to_insert.insert_right(node)
                    print("=========================")
                    print("Place to insert: %d, right inserted value: %d" % (place_to_insert.value, node))
                    print("=========================")

                print("Traversing...")
                root.pre_order_traverse()
                print("Traverse Over.")
        return root

    def wandar(self, root):
        print("wandaring in the tree...")
        while(random.random() > 0.5):
            if random.random() > 0.5:
                print("Turn left")
                if root.left_child:
                    root = root.left_child
                else:
                    print("Over")
                    return root
            else:
                print("Turn right")
                if root.right_child:
                    root = root.right_child
                else:
                    print("Over")
                    return root
        print("Over")
        return root

    def traverse_test(self):
        print("Pre-order Traversing...")
        self.binaryTree.pre_order_traverse()
        print("In-order Traversing...")
        self.binaryTree.in_order_traverse()
        print("Post-order Traversing...")
        self.binaryTree.post_order_traverse()
        print("Breadth first Traversing...")
        self.binaryTree.breadth_first_traverse()



if __name__ == '__main__':
    TestCase = BinaryTreeTest()
    TestCase.traverse_test()
    print("Finished")
