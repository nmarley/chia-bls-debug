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


# x_c0 = Fq(q, 0x09e35c2bcad146e49aa19e4df6699d08f9ccc12d1c7625788f2ada0bad3e5741dc736e2935fe3ebcb0fef6db1166786f)
# x_c1 = Fq(q, 0x1245709e2a671d31cbdd537bb3cdcbde39e66511dd390a4a28a0ee0beea98782695d119e2d7ed66ef3f15e6c2a223bf9)
# x_val = Fq2(q, x_c0, x_c1)
# print("x_val = ", x_val)
#
# y_c0 = Fq(q, 0x1167ad422b392c865d7cbae6adc4f4827a090a6de6c3a9e28f93786e3fc7f516d7dcf8abdbe8df476dda27ba7adb2aad)
# y_c1 = Fq(q, 0x0029180da059941e8194ce794161f2b77266d955d61f591dbb177591b6e6d6792454935b388fb769ac91d739491f7110)
# y_val = Fq2(q, y_c0, y_c1)
# print("y_val = ", y_val)
#
# sk = 0x22fb42c08c12de3a6af053880199806532e79515f94e83461612101f9412f9e

# =========================================================================

# testing FQ2 point arith

# xx = x_val * x_val
# print("xx:", xx)
#
# xy = x_val * y_val
# print("xy:", xy)
#
# yx = y_val * x_val
# print("yx:", yx)
#
# yy = y_val * y_val
# print("yy:", yy)

#x4 = 4 * x_val
#print("x4:", x4)

#dbl = double_point_jacobian(g2pj)
#print("dbl = ", dbl)

#square = add_points_jacobian(g2pj, g2pj)
#print("square = ", square)

# res = g2pj * sk
# print("res = ", res)

# res: G2Projective(x=Fq2(Fq(0x7caed..6f42f) + Fq(0x19747..6f4d9) * u), y=Fq2(Fq(0x7533c..08817) + Fq(0x144ea..fbe12) * u), z=Fq2(Fq(0xdc8ed..0db08) + Fq(0x188a8..123c8) * u))


# makeFQ2 := func(c0Hex, c1Hex string) *bls.FQ2 {
#     c0, _ := new(big.Int).SetString(c0Hex, 16)
#     c1, _ := new(big.Int).SetString(c1Hex, 16)
#     return bls.NewFQ2(bls.NewFQ(c0), bls.NewFQ(c1))
# }


resJacobian = JacobianPoint(
    Fq2(q,
        0x07094a722e8bffb9ffe74450ec66cec97df3830907e0c68de204800d44472a6018e008c8a6ced2a79a8b0997dde94424,
        0x022f824d1a34a15bf54093cde8bdd0939e4df53551ec4e90ed293faa0a21c8ddd3977a78feefa4c6aaf1d95488471768,
    ),
    Fq2(q,
        0x0b5a4936ad59c671883f8e8b42ba9596d2447e854c28dbf2b7246f74d7d2ec79918ad6db14bedef2ad2330e0f92bbb74,
        0x12b0f954f476fee2793c139ed186e29ccd79515c52d681cb0d9d03d0ba1a20d988bc4f97b331ab89ac6837eeb2db7fab,
    ),
    Fq2(q,
        0x08ce489a1cf272726fddce17183e3c2d8f9ac956da024105b7f61e3b88def409910df159067dbe8f21b54f74f5b6aaaf,
        0x0052301b40b3283d03299cf282c3e56ee4cdb2abac3eb23b762eeb236dcdacf248a926b6711f6ed35923ae72923ee220,
    ),
    False,
)
print("NGMpy resJacobian:", resJacobian)

addEndJacobian = JacobianPoint(
    Fq2(q,
        0x0356a2f73692091119cfb08d3914fafab16fdab286022823a8825df932b7db790d9a75a9f5f07f95647e6e1eaad395ac,
        0x1527e3c8de0411fc5aeb7f1989fec31d01f8dac358d7e1557b86ab525191fa0b9045df63b963ed856c909fd5acc19861,
    ),
    Fq2(q,
        0x040e147d2f332d7da1756e51f686428bcad7d1031ee184e5cd937e7a6a1d074e6407ceba6ffd3f356002b7c24403826f,
        0x0426112bd6dfb5fc17af15a6e039e5dfe88a69e6958cd20e1ab267d5219436c8089fc662d463b801b2c8b431cac841e5,
    ),
    Fq2(q,
        0x169659cd2b8245676b7f255ea7c0d91f3b3e22bb87432a49f7334f26694958f73c94e27dce438905a213f06c50422196,
        0x09b32a5da729bb31e40c9fe528098e901c24a2885d977dfe9cba268c6cc738cb09a7302aa6c8906d07a1d00e736adc15,
    ),
    False,
)
print("NGMpy addEndJacobian:", addEndJacobian)

res = resJacobian + addEndJacobian
print("NGMpy finalres:", res)
