#ifndef _KEY_HPP_
#define _KEY_HPP_

#include <inttypes.h>
#include <string>

class Key {
    uint8_t* keydata{nullptr};
    std::string colour{"white"};

public:
    uint8_t* GetBytes();
    static Key FromBytes(uint8_t* bytes);
    std::string GetColour();
    void SetColour(std::string);

    Key();
    ~Key();
};

#endif /* _KEY_HPP_ */
