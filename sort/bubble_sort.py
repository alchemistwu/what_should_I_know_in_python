'''
Bubble sort.

Reference: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
Written by Junzheng
1/13/2020
'''

def bubble_sort(list_to_sort):
    swapped = True

    while swapped:
        length = len(list_to_sort)
        swapped = False
        for i in range(length - 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swapped = True
    return list_to_sort
