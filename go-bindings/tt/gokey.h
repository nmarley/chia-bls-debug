// gokey.h

#ifndef _GOKEY_H_
#define _GOKEY_H_

#ifdef __cplusplus
extern "C" {
#endif

typedef void* Key;

Key KeyInit(void);
void KeyFree(Key k);

#ifdef __cplusplus
}
#endif

#endif /* _GOKEY_H_ */
