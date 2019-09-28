// sk.cpp
// ../src/bls.hpp
#include <cstring>
#include "bls.hpp"
#include "sk.h"

SecretKey SecretKeyFromSeed(void *p, int size) {
    // caller is responsible for freeing this
    void* skPtr = (bls::PrivateKey*)malloc(sizeof(bls::PrivateKey));
    bls::PrivateKey sk = bls::PrivateKey::FromSeed((uint8_t *)p, size);
    memmove(skPtr, (const void*)&sk, sizeof(bls::PrivateKey));
    return skPtr;
}

// Serialize the key into bytes
void* SKSerialize(SecretKey sk) {
    // caller is responsible for freeing this
    void* vptr = (uint8_t*)malloc(bls::PrivateKey::PRIVATE_KEY_SIZE);

    bls::PrivateKey* key = (bls::PrivateKey*)sk;
    uint8_t* buffer = (uint8_t*)malloc(bls::PrivateKey::PRIVATE_KEY_SIZE);
    key->Serialize(buffer);
    memmove(vptr, (const void*)buffer, bls::PrivateKey::PRIVATE_KEY_SIZE);
    free(buffer);
    return vptr;
}

// SecretKeyFree frees the memory allocated for the secret key
void SecretKeyFree(SecretKey sk) {
    bls::PrivateKey* key = (bls::PrivateKey*)sk;
    free(key);
}

// Return the public key
PublicKey SKGetPublicKey(SecretKey sk) {
    bls::PrivateKey* key = (bls::PrivateKey*)sk;

    // caller is responsible for freeing this
    void* pkPtr = (uint8_t*)malloc(bls::PublicKey::PUBLIC_KEY_SIZE);
    bls::PublicKey pk = key->GetPublicKey();
    memmove(pkPtr, (const void*)&pk, bls::PublicKey::PUBLIC_KEY_SIZE);
    return pkPtr;
}
