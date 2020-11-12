import zcount


def mean(list_in) -> float:
    if zcount.count(list_in) > 0:
        return sum(list_in)/zcount.count(list_in)
    else:
        print('data set empty')
