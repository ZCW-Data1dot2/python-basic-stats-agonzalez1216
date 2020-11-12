import zcount


def median(list_in) -> float:
    median_index = int(zcount.count(list_in)//2)
    list_in.sort()
    if zcount.count(list_in) % 2 == 0:
        return list_in[median_index]+list_in[median_index-1]/2
    return list_in[median_index]
