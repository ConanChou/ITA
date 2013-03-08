class Max_Heap(object):
    """docstring for heap"""
    def __init__(self, array):
        self.array = array
        self.build()

    def left(self, i):
        """return left node index"""
        return 2*i+1

    def right(self, i):
        """return right node index"""
        return 2*i+2

    def parent(self, i):
        """return parent node index"""
        return i/2

    def max_heapify(self, i):
        """max heapify the array"""
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.array[l] > self.array[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.array[r] > self.array[largest]:
            largest = r
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.max_heapify(largest)

    def build(self):
        """docstring for build"""
        self.heap_size = len(self.array)
        for i in xrange(len(self.array)/2-1, -1, -1):
            self.max_heapify(i)

    def sort(self):
        """docstring for sort"""
        for i in xrange(len(self.array)-1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heap_size -= 1
            self.max_heapify(0)


if __name__ == '__main__':
    from random import shuffle

    array = range(20)
    shuffle(array)
    print "Origin:\t", array
    max_heap = Max_Heap(array)
    print "Build:\t", max_heap.array
    max_heap.sort()
    print "Sorted:\t", max_heap.array
