from typing import List
from collections import Counter


def unique_occurrences(arr: List[int]) -> bool:
    d = {}

    for item in arr:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    set_occurrences = set(d.values())

    return len(d) == len(set_occurrences)



def unique_occurrences_2(arr: List[int]) -> bool:
    d = {}

    for item in arr:
        d[item] = d.get(item, 0) + 1

    return len(d) == len(set(d.values()))


def unique_occurrences_3(arr: List[int]) -> bool:
    counter = Counter(arr)

    return len(counter.values()) == len(set(counter.values()))
