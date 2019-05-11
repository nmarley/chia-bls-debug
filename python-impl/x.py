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

setrecursionlimit(10**6)


sk = 0x22fb42c08c12de3a6af053880199806532e79515f94e83461612101f9412f9e
rp = JacobianPoint(
    Fq2(q,
        0x09e35c2bcad146e49aa19e4df6699d08f9ccc12d1c7625788f2ada0bad3e5741dc736e2935fe3ebcb0fef6db1166786f,
        0x1245709e2a671d31cbdd537bb3cdcbde39e66511dd390a4a28a0ee0beea98782695d119e2d7ed66ef3f15e6c2a223bf9,
    ),
    Fq2(q,
        0x1167ad422b392c865d7cbae6adc4f4827a090a6de6c3a9e28f93786e3fc7f516d7dcf8abdbe8df476dda27ba7adb2aad,
        0x0029180da059941e8194ce794161f2b77266d955d61f591dbb177591b6e6d6792454935b388fb769ac91d739491f7110,
    ),
    Fq2(q,
        0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001,
        0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
    ),
    False,
)
# print("NGMpy sk:", sk)
# print("NGMpy rp:", rp)

res = rp * sk
# print("NGMpy res:", res)

