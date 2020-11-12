import zcount
import zmean
import zstddev


def cov(list_x, list_y):
    sum_of = 0
    for i in range(0, int(zcount.count(list_x))):
        sum_of += ((list_x[i] - zmean.mean(list_x)) * (list_y[i] - zmean.mean(list_y)))
    covar = sum_of/(zcount.count(list_x) - 1)
    return covar


def corr(list_x, list_y):
    return cov(list_x, list_y)/(zstddev.stddev(list_x) * zstddev.stddev(list_y))
