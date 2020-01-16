'''
Selection sort.

Reference: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
Written by Junzheng
1/13/2020
'''

def selection_sort(list_to_sort):
    length = len(list_to_sort)

    for i in range(length - 1):
        min = list_to_sort[i]
        min_index = i
        for j in range(i + 1, length):
            if list_to_sort[j] < min:
                min = list_to_sort[j]
                min_index = j

        list_to_sort[min_index], list_to_sort[i] = list_to_sort[i], list_to_sort[min_index]

    return list_to_sort
