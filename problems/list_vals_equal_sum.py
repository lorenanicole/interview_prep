def find_pairs_equal_sum_iterative(list, sum):
    """
    :param list: an unsorted list of vals to find pairs in
    :param sum: numerical sum pairs must equal

    :return list of pairs that equal sum

    Ref: This is a classic NP-Complete problem which is called subset-sum.

    In computer science, the subset sum problem is an important problem in
    complexity theory and cryptography. The problem is this: given a set
    (or multiset) of integers, is there a non-empty subset whose sum is zero?
    For example, given the set {−7, −3, −2, 5, 8}, the answer is yes because
    the subset {−3, −2, 5} sums to zero. The problem is NP-complete, meaning
    roughly that while it is easy to confirm whether a proposed solution is
    valid, it may inherently be prohibitively difficult to determine in the
    first place whether any solution exists.

    https://stackoverflow.com/questions/9656789/find-2-numbers-in-an-unsorted-array-equal-to-a-given-sum
    """
    freq_map = {}
    for val in list:
        if val not in freq_map:
            freq_map[val] = 1
        else:
            freq_map[val] += 1

    pairs = {}
    for val in freq_map.keys():
        possible_pair = sum - val

        if possible_pair in freq_map:
            if possible_pair == val and freq_map[val] < 1:
                next
            pairs[val] = possible_pair

    return pairs

if __name__ == '__main__':
    print(find_pairs_equal_sum_iterative([6, 4, 5, 7, 9, 1, 2], 10))