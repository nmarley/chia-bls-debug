#include "AggregationInfoWrapper.h"

namespace js_wrappers {
    AggregationInfoWrapper::AggregationInfoWrapper(const AggregationInfo &info) : JSWrapper(info) {}

    AggregationInfoWrapper AggregationInfoWrapper::FromMsgHash(const PublicKeyWrapper &pkw, val messageHashBuffer) {
        PublicKey pk = pkw.GetWrappedInstance();
        std::vector<uint8_t> messageHash = helpers::toVector(messageHashBuffer);
        AggregationInfo info = AggregationInfo::FromMsgHash(pk, messageHash.data());
        return AggregationInfoWrapper(info);
    }

    AggregationInfoWrapper AggregationInfoWrapper::FromMsg(const PublicKeyWrapper &pkw, val messageHashBuffer) {
        PublicKey pk = pkw.GetWrappedInstance();
        std::vector<uint8_t> message = helpers::toVector(messageHashBuffer);
        AggregationInfo info = AggregationInfo::FromMsg(pk, message.data(), message.size());
        return AggregationInfoWrapper(info);
    }

    AggregationInfo AggregationInfoWrapper::FromBuffersUnwrapped(val pubKeyWrappersArray, val messageHashes,
                                                                 val exponentBns) {
        std::vector<std::vector<uint8_t>> messageHashesVectors = helpers::jsBuffersArrayToVector(messageHashes);
        std::vector<uint8_t *> messageHashesVector;
        for (auto &i : messageHashesVectors) {
            messageHashesVector.push_back(i.data());
        }
        std::vector<PublicKey> pubKeysVector = PublicKeyWrapper::Unwrap(
                helpers::toVectorFromJSArray<PublicKeyWrapper>(pubKeyWrappersArray));
        std::vector<bn_t *> exponentsVector = helpers::jsBuffersArrayToBnVector(exponentBns);

        AggregationInfo info = AggregationInfo::FromVectors(pubKeysVector, messageHashesVector, exponentsVector);
        return info;
    }

    AggregationInfoWrapper AggregationInfoWrapper::FromBuffers(val pubKeys, val messageHashes, val exponentBns) {
        AggregationInfo info = AggregationInfoWrapper::FromBuffersUnwrapped(pubKeys, messageHashes, exponentBns);
        return AggregationInfoWrapper(info);
    }

    val AggregationInfoWrapper::GetPubKeys() const {
        std::vector<PublicKey> pubKeys = wrapped.GetPubKeys();
        std::vector<val> pubKeyWrappers;
        for (auto &pubKey : pubKeys) {
            pubKeyWrappers.emplace_back(val(PublicKeyWrapper(pubKey)));
        }
        return helpers::toJSArray<val>(pubKeyWrappers);
    }

    val AggregationInfoWrapper::GetMessageHashes() const {
        std::vector<uint8_t *> messageHashesPointers = wrapped.GetMessageHashes();
        return helpers::byteArraysVectorToJsBuffersArray(messageHashesPointers, BLS::MESSAGE_HASH_LEN);
    }

    val AggregationInfoWrapper::GetExponents() const {
        std::vector<PublicKey> pubKeys = wrapped.GetPubKeys();
        std::vector<uint8_t *> messageHashes = wrapped.GetMessageHashes();
        std::vector<val> exponents;
        auto l = pubKeys.size();
        for (unsigned i = 0; i < l; ++i) {
            bn_t *exponent;
            wrapped.GetExponent(exponent, messageHashes[i], pubKeys[i]);
            val serializedExponent = helpers::toUint8Array(*exponent);
            exponents.push_back(serializedExponent);
        }
        return helpers::toJSArray<val>(exponents);
    }
}
