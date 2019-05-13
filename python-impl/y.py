# flake8: noqa: E501
from aggregation_info import AggregationInfo
from bls import BLS
from ec import (default_ec, default_ec_twist, generator_Fq, generator_Fq2,
                hash_to_point_Fq, hash_to_point_Fq2, sw_encode, twist, untwist,
                y_for_x, AffinePoint, JacobianPoint, double_point_jacobian,
                add_points_jacobian,)
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
from pairing import (int_to_bits)

setrecursionlimit(10**6)


sk1 = PrivateKey.from_seed(bytes([1, 2, 3, 4, 5]))
pk1 = sk1.get_public_key()
# print("pk1.value:", pk1.value)

g1p = JacobianPoint(
    Fq(q, 0x02a8d2aaa6a5e2e08d4b8d406aaf0121a2fc2088ed12431e6b0663028da9ac5922c9ea91cde7dd74b7d795580acc7a61),
    Fq(q, 0x0145bcfef3c097722ea4994dc043be38a47ca15cf0f7622286ba6f85c4b5ddd412c43042938ab6a2eafcaae38119e305),
    Fq(q, 0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001),
    False
)
print("g1p:", g1p)

dbl = g1p * 2
print("dbl:", dbl)
