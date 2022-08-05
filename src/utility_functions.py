def get_counts(ls):
    """
    For a given list, return a dictionary with the counts of all the elements in the list.
    """
    counts = {}
    for element in ls:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts