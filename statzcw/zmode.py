from collections import Counter

def mode(list_in) -> float:
    counts = Counter(list_in)
    for key, value in counts.items():
        if value == max(counts.values()):
            ret_mode = key
    return ret_mode

