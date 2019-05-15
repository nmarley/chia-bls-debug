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


# x = Fq(q, 0x02a8d2aaa6a5e2e08d4b8d406aaf0121a2fc2088ed12431e6b0663028da9ac5922c9ea91cde7dd74b7d795580acc7a61)
# y = Fq(q, 0x0145bcfef3c097722ea4994dc043be38a47ca15cf0f7622286ba6f85c4b5ddd412c43042938ab6a2eafcaae38119e305)
# z = Fq.one(q)
#
# jp = JacobianPoint(x, y, z, False)
# n = 7429792268441337100724157164307770750544294956256514405682157408702131069250
# print("NGMpy jp:", jp)
# print("NGMpy n:", n)
#
# res = jp * n
# print("NGMpy res:", res)

# ========================================================================

p1x= Fq(q,0x01a89b5b9147007d2f6d05419c96928acbf319b5563c3f05a12ee0b11265d8d24e3fccd613ba5e4bc59d40d80d0cb734)
p1y= Fq(q,0x14fa6c10f0b6a3691f19d01560a410081b16486f49f03f8bafb45c149c5664b610494be7c234e674d9e1e4c45dd3ac5d)
p1z= Fq(q,0x028b79fde7812ee45d49329b80877c7148f942b9e1eec4450d74df0b896bbba82588608527156d45d5f955c70233c60a)

p2x= Fq(q,0x0241693bcdbbd80196f04dda45614cde8ce7830b67e160aa5d9865dc8da4eb868a49edaf0f47a8e5a9d6ea8674f2adec)
p2y= Fq(q,0x1465ed4d5ea6cefed637b0849112d1181b734354ebf5737be960a38c09a94fad3b0f7145dac1e4eaed1b25178756e7b4)
p2z= Fq(q,0x06d9b63732d28524ace23d230dfc5002194c7d2c26be6f4c7c86735f7c5896395e494f57c49811fa938077233b9387b7)

resX= Fq(q,0x157cab11ec3354b77ccce4cfa8a4063897f62d55b75a49f51fa568b09e4dbb87416987d4e65b145371586340eddd2520)
resY= Fq(q,0x025b922e4d1e76beb38b242c22d76c77d0daddac848e27dc3f16465005634f27ea64cc4101513df6207cb56f204250d0)
resZ= Fq(q,0x1223495578cfe0f0a9c2b09343931aa52d197f32ae098d63c1b2cb683ccf120be5691b24083b642060660489e81a0803)

p1 = JacobianPoint(p1x, p1y, p1z, False)
p2 = JacobianPoint(p2x, p2y, p2z, False)
expected = JacobianPoint(resX, resY, resZ, False)

res = p1 + p2
