#ifndef GO_BINDINGS_HELPERS_H_
#define GO_BINDINGS_HELPERS_H_

#include <algorithm>
#include <vector>
#include "relic.h"
#include "../src/bls.hpp"

using namespace bls;

namespace helpers {
    val toUint8Array(uint8_t *pointer, size_t data_size);

    val toUint8Array(std::vector<uint8_t> vec);

    val toUint8Array(bn_t bn);

    std::vector<uint8_t> toVector(uint8_t *pointer, size_t data_size);

    std::vector<uint8_t> toVector(val jsBuffer);

    std::vector<uint8_t> toVector(bn_t bn);

    template<typename T>
    inline std::vector<T> toVectorFromJSArray(val jsArray) {
        auto l = jsArray["length"].as<unsigned>();
        std::vector<T> vec;
        for (unsigned i = 0; i < l; ++i) {
            vec.push_back(jsArray[i].as<T>());
        }
        return vec;
    }

    template<typename T>
    inline val toJSArray(std::vector<T> vec) {
        val Array = val::global("Array");
        val arr = Array.new_();
        auto l = vec.size();
        for (unsigned i = 0; i < l; ++i) {
            arr.call<void>("push", vec[i]);
        }
        return arr;
    }

    std::vector<std::vector<uint8_t>> jsBuffersArrayToVector(val buffersArray);

    std::vector<bn_t *> jsBuffersArrayToBnVector(val buffersArray);

    val byteArraysVectorToJsBuffersArray(std::vector<uint8_t *> arraysVector, size_t element_size);
}  // namespace helpers

#endif  // JS_BINDINGS_HELPERS_H_
