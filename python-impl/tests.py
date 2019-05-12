# flake8: noqa: E501
from aggregation_info import AggregationInfo
from ec import (default_ec, default_ec_twist, generator_Fq, generator_Fq2,
                hash_to_point_Fq, hash_to_point_Fq2, sw_encode, twist, untwist,
                y_for_x)
from fields import Fq, Fq2, Fq6, Fq12
from itertools import combinations
from keys import PrivateKey, PublicKey, ExtendedPrivateKey
import random
from signature import Signature, PrependSignature
from sys import setrecursionlimit
import time
from threshold import Threshold
from util import hash256

setrecursionlimit(10**6)




def test_vectors():
    sk1 = PrivateKey.from_seed(bytes([1, 2, 3, 4, 5]))
    pk1 = sk1.get_public_key()
    sig1 = sk1.sign(bytes([7, 8, 9]))
    # print("NGMpy IN TEST, sig1: ", sig1.serialize().hex())
    sig1.verify()

#    sk2 = PrivateKey.from_seed(bytes([1, 2, 3, 4, 5, 6]))
#    pk2 = sk2.get_public_key()
#    sig2 = sk2.sign(bytes([7, 8, 9]))
#    assert(sk1.serialize() == bytes.fromhex("022fb42c08c12de3a6af053880199806532e79515f94e83461612101f9412f9e"))
#    assert(pk1.get_fingerprint() == 0x26d53247)
#    assert(pk2.get_fingerprint() == 0x289bb56e)
#    assert(sig1.serialize() == bytes.fromhex("93eb2e1cb5efcfb31f2c08b235e8203a67265bc6a13d9f0ab77727293b74a357ff0459ac210dc851fcb8a60cb7d393a419915cfcf83908ddbeac32039aaa3e8fea82efcb3ba4f740f20c76df5e97109b57370ae32d9b70d256a98942e5806065"))
#    assert(sig2.serialize() == bytes.fromhex("975b5daa64b915be19b5ac6d47bc1c2fc832d2fb8ca3e95c4805d8216f95cf2bdbb36cc23645f52040e381550727db420b523b57d494959e0e8c0c6060c46cf173872897f14d43b2ac2aec52fc7b46c02c5699ff7a10beba24d3ced4e89c821e"))
