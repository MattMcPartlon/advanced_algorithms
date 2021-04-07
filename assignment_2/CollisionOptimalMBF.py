"""
Implement a MultiBloomFilter that is optimized to minimize collision probability

This class takes a capacity as a parameter and returns a multi-bloom-filter with
k sub-filters, where k is chosen to minimize the likelihood of collisions

You must only implement code to find the optimal such k (given an overall capacity)

Please list the rationale for your choice of k as a comment. Your choice must only be
within +-c for some constant c>0 of the optimal k (so that floor's and ceils can
be ignored in the analysis)
"""
from random import randint
from typing import Iterable, Any
from assignment_2.MultiBloomFilter import MultiBloomFilter as MBF


class CollisionOptimalMBF(MBF):
    def __init__(self, capacity: int):
        k = self.get_optimal_k(capacity)
        hash_fns = self.get_hash_fns(k)
        super().__init__(capacity, k, hash_fns, filter_ty="Integer MultiBloomFilter")

    def get_optimal_k(self, capacity: int) -> int:
        pass  # TODO: leave a comment explaining your approach below

    def get_hash_fns(self, k: int) -> Iterable[Any]:
        pass  # TODO: get k hash functions to use for the multi bloom filter


# Simple test code
if __name__ == "__main__":
    n = 50
    items = [randint(0, 2 ** 31 - 1) for _ in range(n)]
    bf = CollisionOptimalMBF(n, 2)
    bf.add_all(*items)
    tests = [randint(0, 2 ** 31 - 1) for _ in range(10)]
    print("All items included: ", all([i in bf for i in items]))
    for t in tests:
        print(f"{t} in bf:", t in bf)
