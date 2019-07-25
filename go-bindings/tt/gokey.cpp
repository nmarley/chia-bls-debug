#include "src/key.hpp"
#include "gokey.h"

Key KeyInit() {
    Key key = new Key();
    return (void*)key;
}

void KeyFree(Key k) {
    Key *key = (Key *)k;
    delete key;
}
