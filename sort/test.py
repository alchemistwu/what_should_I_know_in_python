from sort.bubble_sort import *
from sort.seletion_sort import *
import numpy

def test():
    random_list = numpy.random.permutation(10).tolist()
    print(random_list)
    print(bubble_sort(random_list))
    print(selection_sort(random_list))
if __name__ == '__main__':
    test()