import zvariance
import math


def stddev(list_in) -> float:
    variance = zvariance.variance(list_in)
    return math.sqrt(variance)
