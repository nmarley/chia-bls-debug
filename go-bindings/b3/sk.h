// sk.h
#include "pk.h"
#ifdef __cplusplus
extern "C" {
#endif

#define SECRET_KEY_SIZE 32

typedef void* SecretKey;
SecretKey SecretKeyFromSeed(void *, int);
void* SKSerialize(SecretKey);
void SecretKeyFree(SecretKey);

PublicKey SKGetPublicKey(SecretKey);

#ifdef __cplusplus
}
#endif
