#ifndef _KEY_HPP_
#define _KEY_HPP_

#include <inttypes.h>

class Key {
    uint8_t* keydata{nullptr};

public:
    static Key FromBytes(uint8_t* bytes);

    Key();
    ~Key();
};

#endif /* _KEY_HPP_ */
