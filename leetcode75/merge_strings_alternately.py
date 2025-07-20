def merge_alternately(word1: str, word2: str) -> str:
    min_length = min(len(word1), len(word2))

    new_string = ""
    for i in range(min_length):
        new_string += word1[i] + word2[i]

    if len(word1) - min_length > 0:
        new_string += word1[min_length:]
    elif len(word2) - min_length > 0:
        new_string += word2[min_length:]
    return new_string


def merge_alternately_single_pointer(word1: str, word2: str) -> str:
    result = []

    max_length = max(len(word1), len(word2))

    for i in range(max_length):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]

    return "".join(result)


def merge_alternately_double_pointer(word1: str, word2: str) -> str:
    result = []
    n = len(word1)
    m = len(word2)
    i = 0
    j = 0

    while i < n or j < m:
        if i < n:
            result += word1[i]
            i += 1
        if j < m:
            result += word2[j]
            j += 1

    return "".join(result)
