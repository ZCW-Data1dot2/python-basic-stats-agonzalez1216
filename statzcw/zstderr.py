import zstddev
import math
import zcount


def stderr(list_in) -> float:
    return zstddev.stddev(list_in)/ math.sqrt(zcount.count(list_in))
