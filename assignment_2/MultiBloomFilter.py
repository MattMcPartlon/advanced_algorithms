
from random import randint

from assignment_2.BloomFilterABC import BloomFilterABC
from assignment_2.BloomFilter import BloomFilter

"""
Implement a "MultiBloomFilter", which extends the BloomFilterABC class.

This class will consist of k bloom filters, all with the same capacity,
and will answer membership queries by searching for the element in each
of the k bloom filters
We will add an element by adding it to each of the k Bloom Filters as well.

In addition to the parameters of the BloomFilterABC class, you must also
support a parameter 'hash_fs' denoting the hash function to use for each
of the k filters.

You can add any parameters you'd like to the __init__ funciton
and any helper methods you'd like, but you must extend the abstract
base class.

"""


class MultiBloomFilter(BloomFilterABC):
    def __init__(self, capacity, k, hash_funcs = None, filter_ty="Integer MultiBloomFilter"):
        super().__init__(capacity, item_ty=int, filter_ty=filter_ty)
        hash_funcs = hash_funcs or [None]*k
        assert len(hash_funcs) == k
        self.filters = [BloomFilter(capacity//k, h) for h in hash_funcs]
        #TODO: add any other instance variables that you need


    @property
    def num_filled(self):
        """
        Number of slots filled summed over all filters
        """
        return sum([f.num_filled for f in self.filters])


    """Implement ABC"""
    def _add(self, item):
        pass #TODO

    def _hash(self, item):
        pass #TODO

    def __contains__(self, item):
        pass #TODO

#Simple test code
if __name__ == "__main__":
    n = 50
    items = [randint(0, 2**31-1) for _ in range(n)]
    bf = MultiBloomFilter(n, 2)
    bf.add_all(*items)
    tests = [randint(0, 2**31-1) for _ in range(10)]
    print("All items included: ", all([i in bf for i in items]))
    for t in tests:
        print(f"{t} in bf:", t in bf)

