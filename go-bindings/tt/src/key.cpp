#include "key.hpp"

// Construct a key from a bytearray
Key Key::FromBytes(uint8_t* bytes) {
    Key k;
    k.keydata = bytes;
    return k;
}
