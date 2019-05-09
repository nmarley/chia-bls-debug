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


#print("Fq6.zero = ", Fq6.zero(q))
#print("Fq2.zero = ", Fq2.zero(q))
#print("Fq.zero = ", Fq.zero(q))

#print("Fq6.one = ", Fq6.one(q))
#print("Fq2.one = ", Fq2.one(q))
#print("Fq.one = ", Fq.one(q))

Fq12OneRoot = Fq6(q, Fq2.zero(q), Fq2.one(q), Fq2.zero(q))
# FQ12OneRoot := bls.NewFQ6(bls.FQ2Zero, bls.FQ2One, bls.FQ2Zero)
nwsq = ~Fq12(q, Fq12OneRoot, Fq6.zero(q))
print("nwsq = ", nwsq)


#x_c0 = Fq(q, 0x06427044c2270e673490af1756c840361b4090bca24ae94a2f6ad442a5470e94dc6dd392834cf28f3274e85dc2d036e4)
#x_c1 = Fq(q, 0x0efe0745224dd9cc23e7d7d63ba7b86ea8deee05b113e02c607afc75f740cb4d0c01d2d361e3fd028b9c24d816afb45a)
#x_val = Fq2(q, x_c0, x_c1)
# print("x_val = ", x_val)



y_c0 = Fq(q, 0x0b7d5c8331ab2a86a94a97acdd248d828d2f7fefa3429a0637076418882154099f40023d81b1f43f6ae860901ebcbd04)
y_c1 = Fq(q, 0x0a21795e4ad60a5630d919d16421cdcf494ef30f91ebd2c07755ab5493444366e831c16c26bd010d6b87ea6fa59fc428)
y_val = Fq2(q, y_c0, y_c1)
print("y_val = ", y_val)

nwcu = ~Fq12(q, Fq6.zero(q), Fq12OneRoot)
#print("nwcu = ", nwcu)
#nwcu[1][1]
# Fq2(Fq(0xd0088..fd556), Fq(0xd0088..fd555))


#n = x_val * nwsq
#print("n = ", n)

#new_x = x_val * nwsq[0][2]
#print("new_x = ", new_x)

new_y = y_val * nwcu[1][1]
print("new_y = ", new_y)

# xVal := bls.NewFQ2(bls.NewFQ(c0), bls.NewFQ(c1))
# fmt.Println("NGM(Untwist) xVal:", xVal)
