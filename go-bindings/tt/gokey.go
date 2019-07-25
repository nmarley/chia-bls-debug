// gokey.go
package gokey

// #cgo CXXFLAGS: -std=c++14
// #cgo LDFLAGS: -L./src -lkey
// #include "gokey.h"
import "C"

// Key struct
type Key struct {
    key C.Key
}

// New creates a new Key object
func New() Key {
    var ret Key
    ret.key = C.KeyInit()
    return ret
}

// Free frees the key object
func (k Key) Free() {
    C.KeyFree(k.key)
}
