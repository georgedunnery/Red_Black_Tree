# George Dunnery - CS 5800

from RBTree import *


def main():
    array = [10, 5, 7, 3, 15, 12, 17, 29, 100, 500]
    demo = RBTree()
    demo.insert_list(array)
    print(demo.rb_inorder_walk())
    demo.interactive()


main()
