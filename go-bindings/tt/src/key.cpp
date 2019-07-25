#include "key.hpp"

// Construct a key from a bytearray
Key Key::FromBytes(uint8_t* bytes) {
    Key k;
    k.keydata = bytes;
    return k;
}

std::string Key::GetColour() {
    return this->colour;
}

void Key::SetColour(std::string colour) {
    this->colour = colour;
}

Key::Key() { }
Key::~Key() { }
