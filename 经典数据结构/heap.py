class Heap(object):
    def __init__(self, elist):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise ValueError('The heap is empty!')
        return self._elems[0]

    def push(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def pop(self):
        if self.is_empty():
            raise ValueError('The heap is empty!')
        elems = self._elems
        e0 = elems[0]
        e =elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0


    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1) >> 1
        while i>0 and e<elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1) >> 1
        elems[i] = e

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin << 1 + 1
        while j < end:
            if j+1 < end and elems[j+1]<elems[j]:
                j += 1
            if e<elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j << 1 + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end>>1, -1, -1):
            self.siftdown(self.elems[i], i, end)
            