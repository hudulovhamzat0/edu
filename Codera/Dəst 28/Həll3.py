from math import gcd
from functools import reduce

def en_cox_ortaq_vuruq(siyahi):
    return reduce(gcd, siyahi)

siyahi = list(map(int, input().split()))
print(en_cox_ortaq_vuruq(siyahi))
