from abc import ABC, abstractmethod

class BloomFilterABC(ABC):

    def __init__(self, capacity: int, filter_ty: str = ''):
        """
        Abstract base class for Bloom Filters
        :param capacity: The capacity of the filter
        :param filter_ty: Name for the implementing class
        """
        self._num_added = 0
        self._num_filled = 0
        self._capacity = capacity
        self.filter_ty = filter_ty

    @abstractmethod
    def __contains__(self, item):
        #TODO
        pass

    @abstractmethod
    def _add(self, item):
        """
        adds the item to the bloom filter and returns true if
        hash of the item is not already in the filter
        :param item:  item to add
        :return: true iff hash of item is not in this filter
        """
        pass

    def add(self, item):
        self._num_added += 1
        collision = item in self
        added = self._add(item)
        assert item in self
        if added:
            assert not collision
            self._num_filled += 1

    def add_all(self, *items):
        for item in items:
            self.add(item)

    @abstractmethod
    def _hash(self, item):
        pass

    def hash(self, item):
        return self._hash(item) % self.capacity

    def __str__(self):
        s = 'bloom filter of type : ' + self.filter_ty
        s += ', capacity : ' + str(self.capacity)
        s += ', num filled : ' + str(self.num_filled)
        s += ', num added : ' + str(self.num_added)
        return s

    @property
    def capacity(self):
        return self._capacity

    @property
    def num_filled(self):
        return self._num_filled

    @property
    def average_filled(self):
        if self.capacity>0:
            return self.num_filled/self.capacity
        return -1

    @property
    def num_empty(self):
        return self.capacity - self.num_filled

    @property
    def num_added(self):
        return self._num_added

    @property
    def num_collisions(self):
        return self._num_added - self._num_filled

