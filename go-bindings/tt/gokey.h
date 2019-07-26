// gokey.h

#ifndef _GOKEY_H_
#define _GOKEY_H_

#include <inttypes.h>

#ifdef __cplusplus
extern "C" {
#endif

// C++ -> C struct remap of Key
typedef struct {
    uint8_t *keydata;
    const char *colour;
} gokey;

gokey new_key(void);
// KeyInit(void);
void KeyFree(gokey k);

#ifdef __cplusplus
}
#endif

#endif /* _GOKEY_H_ */
