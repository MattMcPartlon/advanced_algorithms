import numpy as np
import matplotlib.pyplot as plt
from assignment_2.BloomFilter import BloomFilter as BF
from assignment_2.CollisionOptimalMBF import CollisionOptimalMBF as CO_MBF
from assignment_2.MultiBloomFilter import MultiBloomFilter as MBF

"""
Test the performance of your Bloom Filters.

  - Add r elements uniformly at random from
   [1..N] to your filter.
  - return the bloom filter
"""


def bf_performance_helper(N: int, r: int, capacity: int, hash_func=None):
    S = np.random.choice(np.arange(N), size=r, replace=False)
    bf = BF(capacity=capacity, hash_function=hash_func)
    bf.add_all(*S)
    return bf


def mbf_performance_helper(N: int, r: int, capacity: int, k: int, hash_funcs=None):
    S = np.random.choice(np.arange(N), size=r, replace=False)
    bf = MBF(capacity=capacity, k=k, hash_funcs=hash_funcs)
    bf.add_all(*S)
    return bf


def co_mbf_performance_helper(N: int, r: int, capacity: int):
    S = np.random.choice(np.arange(N), size=r, replace=False)
    bf = CO_MBF(capacity=capacity)
    bf.add_all(*S)
    return bf


"""
Compare the collision probabilities for each type of filter over
different ranges of r. Each bloom filter should have (approximately) 
the same total capacity.
"""

capacity = 10000
N = 20000
step = 1000
rs = list(range(1000, N + 1, step))
# compute the (empirical) collision probability for each type
# of bloom filter, and plot the results (you may use matplotlib.pyplot for this)
# Use r for the x axis and collision probability for y.
# For the MultiBloomFilter, you may want to experiment with a few different values of k
# and include the results for each k value in your plot.

#example code for plot and save:
#for each type of filter:
#   ... get collision prob. data for the filter ...
#   plt.plot(rs, collision_prob_data, label = filter.filter_ty)
#plt.legend()
#plt.show()
#plt.save_fig(<path>)


pass  # TODO: Save the plot in ./collision_comparison.jpeg

# Leave a comment explaining your findings below


"""
Repeat the experiment plotting the number of slots filled for each type of filter
"""
capacity = 10000
N = 20000
step = 1000
rs = list(range(1000, N + 1, step))
# TODO: Save the plot in ./fill_comparison.jpeg

# Leave a comment explaining your findings below -
# Is this what you expect after seeing the results from the first plot?
