#ifndef JS_BINDINGS_WRAPPERS_AGGREGATIONINFOWRAPPER_H_
#define JS_BINDINGS_WRAPPERS_AGGREGATIONINFOWRAPPER_H_

#include "../helpers.h"
#include "PublicKeyWrapper.h"

namespace js_wrappers {

class AggregationInfoWrapper : public JSWrapper<AggregationInfo> {
 public:
    explicit AggregationInfoWrapper(const AggregationInfo &info);

    static AggregationInfoWrapper
    FromMsgHash(const PublicKeyWrapper &pkw, val messageHashBuffer);

    static AggregationInfoWrapper
    FromMsg(const PublicKeyWrapper &pkw, val messageBuffer);

    static AggregationInfoWrapper
    FromBuffers(val pubKeys, val messageHashes, val exponentBns);

    static AggregationInfo
    FromBuffersUnwrapped(val pubKeyWrappers, val messageHashes,
                         val exponentBns);

    val GetPubKeys() const;

    val GetMessageHashes() const;

    val GetExponents() const;
};

}  // namespace js_wrappers

#endif  // JS_BINDINGS_WRAPPERS_AGGREGATIONINFOWRAPPER_H_
