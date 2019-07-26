#include "src/key.hpp"
#include "gokey.h"

gokey new_key() {
    Key *key = new Key();
    gokey gkey;

    gkey.keydata = (*key).GetBytes();
    gkey.colour = (*key).GetColour().c_str();

    return gkey;
}

//void KeyFree(Key k) {
//    Key *key = (Key *)k;
//    delete key;
//}
