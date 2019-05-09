# flake8: noqa: E501
from aggregation_info import AggregationInfo
from bls import BLS
from ec import (default_ec, default_ec_twist, generator_Fq, generator_Fq2,
                hash_to_point_Fq, hash_to_point_Fq2, sw_encode, twist, untwist,
                y_for_x)
from fields import Fq, Fq2, Fq6, Fq12
from itertools import combinations
from keys import PrivateKey, PublicKey, ExtendedPrivateKey
import random
from signature import Signature
from sys import setrecursionlimit
import time
from threshold import Threshold
from util import hash256
from bls12381 import q

setrecursionlimit(10**6)


print("Fq6.zero = ", Fq6.zero(q))
print("Fq2.zero = ", Fq2.zero(q))
print("Fq.zero = ", Fq.zero(q))

print("Fq6.one = ", Fq6.one(q))
print("Fq2.one = ", Fq2.one(q))
print("Fq.one = ", Fq.one(q))


Fq12OneRoot = Fq6(q, Fq2.zero(q), Fq2.one(q), Fq2.zero(q))
# FQ12OneRoot := bls.NewFQ6(bls.FQ2Zero, bls.FQ2One, bls.FQ2Zero)
nwsq = ~Fq12(q, Fq12OneRoot, Fq6.zero(q))
print("nwsq = ", nwsq)
