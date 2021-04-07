from random import randint

from .BloomFilterABC import BloomFilterABC


class BloomFilter(BloomFilterABC):
    """
    Bloom filter for integers
    """

    def __init__(self, capacity: int, hash_function=None):
        super().__init__(capacity, filter_ty="Integer BloomFilter")
        # TODO: add any instance variables needed

    def _add(self, item):
        pass  # TODO (see abc)

    def _hash(self, item):
        """
        Implement a standard hash function (see Utils.py)
        """
        pass  # TODO

    def __contains__(self, item):
        pass  # TODO


# Code below can be used for running a simple test
if __name__ == "__main__":
    n = 50
    items = [randint(0, 2 ** 31 - 1) for _ in range(n)]
    bf = BloomFilter(capacity=n)
    bf.add_all(*items)
    tests = [randint(0, 2 ** 31 - 1) for _ in range(10)]
    print("All items included: ", all([i in bf for i in items]))
    for t in tests:
        print(f"{t} in bf:", t in bf)
