// pk.cpp
// ../src/bls.hpp
//#include <cstring>
#include "bls.hpp"
#include "pk.h"

// Serialize the key into bytes
void* PKSerialize(PublicKey pk) {
    // caller is responsible for freeing this
    void* vptr = (uint8_t*)malloc(bls::PublicKey::PUBLIC_KEY_SIZE);

    bls::PublicKey* key = (bls::PublicKey*)pk;
    uint8_t* buffer = (uint8_t*)malloc(bls::PublicKey::PUBLIC_KEY_SIZE);
    key->Serialize(buffer);
    //std::vector<uint8_t> vecBuffer = key->Serialize();
    // for (uint8_t p : vecBuffer) {
      //   printf("p: %02x\n", p);
    // }
    memmove(vptr, (const void*)buffer, bls::PublicKey::PUBLIC_KEY_SIZE);
    free(buffer);

    return vptr;
}

