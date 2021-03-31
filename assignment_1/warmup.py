import time
from math import factorial

"""
Fill in all #TODO's
Note : you may not use global variables anywhere in your implementations.
If global variables are used, no credit will be given.
"""


def binomial(n: int, r: int) -> int:
    """
    Binomial coefficient, nCr, aka the "choose" function
    n! / (r! * (n - r)!)
    """
    if 0 > r or n < r:
        return 0
    p = 1
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p


def permutations(S: list) -> list:
    """
    Generates all permutations of the input list S
    @input : a list of elements S
    @output : a list of all permutations of the list S
    """
    P = permutation_helper(S)
    assert len(P) == factorial(len(S))
    return P


# 4 points
def permutation_helper(S: list) -> list:
    pass  # TODO


def powerset(S: list) -> list:
    """
    Returns the powerset of the input list S
    @input : a list of elements S
    @output : the powerset of S
    """
    P_S = powerset_helper(S)
    assert len(P_S) == 2 ** len(S)
    return P_S


# 4 points
def powerset_helper(S: list) -> list:
    pass  # TODO


def subsets(S: list, k: int) -> list:
    """
    Generates all subsets T of the list S that have
    cardinality k.

    @input : a list of elements S
    @output : a list of all subsets of S with cardinality k
    """
    if k > len(S) or k < 0:
        raise Exception('must have 0<=k<=|S|, got k : ', k, 'and |S|', len(S))
    T = subset_helper(S, k)
    assert len(T) == binomial(len(S), k)
    return T


# 4 points
def subset_helper(S: list, k: int) -> list:
    pass  # TODO


def timed(message="", verbose=True):
    def time_decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter_ns()
            value = func(*args, **kwargs)
            stop = time.perf_counter_ns()
            if verbose:
                print(message, "in", (stop - start) / 10 ** 9, "seconds.")
            return value

        return wrapper

    return time_decorator


if __name__ == "__main__":
    A = list(range(5))
    # A = np.random.randint(2**31-1, size=4).tolist()
    perms = timed("Permutations")(permutations)(A)
    print(perms)
    pset = timed("Powerset")(powerset)(A)
    print(pset)
    subsets = timed("Subsets")(subsets)(A, 3)
    print(subsets)
