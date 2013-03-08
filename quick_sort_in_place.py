"""
    quick_sort_in_place.py

    Implementation of quick sort on a list and returns a sorted list. In-place version.

    Quick Sort Overview:
    ------------------------
    Uses partitioning to recursively divide and sort the list

    Time Complexity: O(n**2) worst case

    Space Complexity: O(log n) this version

    Stable: No

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""

def partition(seq, left, right, pivot_index):
    """docstring for partition"""
    pivot_value = seq[pivot_index]
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    store_index = left
    for i in range( left, right ):
        if seq[i] < pivot_value:
            seq[i], seq[store_index] = seq[store_index], seq[i]
            store_index += 1
    seq[store_index], seq[right] = seq[right], seq[store_index]
    return store_index

def quicksort(seq, left, right):
    """in-place version of quicksort"""
    if left < right:
        pivot = (left+right)/2
        pivot_new_index = partition(seq, left, right, pivot)
        quicksort(seq, left, pivot_new_index - 1)
        quicksort(seq, pivot_new_index + 1, right)
