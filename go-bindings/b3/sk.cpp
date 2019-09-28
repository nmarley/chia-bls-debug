// sk.cpp
// ../src/bls.hpp
#include <cstring>
#include "bls.hpp"
#include "sk.h"

SecretKey SecretKeyFromSeed(void *p, int size) {
    // caller is responsible for freeing this
    void* skPtr = (bls::PrivateKey*)malloc(bls::PrivateKey::PRIVATE_KEY_SIZE);
    bls::PrivateKey sk = bls::PrivateKey::FromSeed((uint8_t *)p, size);
    memmove(skPtr, (const void*)&sk, bls::PrivateKey::PRIVATE_KEY_SIZE);
    return skPtr;
}

SecretKey SecretKeyFromBytes(void *p, bool modOrder) {
    // caller is responsible for freeing this
    void* skPtr = (bls::PrivateKey*)malloc(bls::PrivateKey::PRIVATE_KEY_SIZE);
    bls::PrivateKey sk = bls::PrivateKey::FromBytes((uint8_t *)p, modOrder);
    memmove(skPtr, (const void*)&sk, bls::PrivateKey::PRIVATE_KEY_SIZE);
    return skPtr;
}

// Serialize the key into bytes
void* SKSerialize(SecretKey sk) {
    // caller is responsible for freeing this
    uint8_t* buffer = (uint8_t*)malloc(bls::PrivateKey::PRIVATE_KEY_SIZE);
    bls::PrivateKey* key = (bls::PrivateKey*)sk;
    key->Serialize(buffer);
    return (void*)buffer;
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
