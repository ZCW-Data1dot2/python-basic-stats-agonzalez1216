import zcount
import zmean


def variance(list_in) -> float:
    amt_of_nums = zcount.count(list_in)
    mean = zmean.mean(list_in)
    sqaure_dev = [(x - mean) ** 2 for x in list_in]
    return sum(sqaure_dev)/amt_of_nums
