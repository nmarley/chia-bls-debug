// gokey.go
package gokey

// #cgo CXXFLAGS: -std=c++14
// #include "gokey.h"
import "C"

// Key struct
type Key struct {
	key C.gokey
}

// New creates a new Key object
func New() Key {
	var ret Key
	ret.key = C.new_key()
	return ret
}

// Free frees the key object
//func (k Key) Free() {
//	C.KeyFree(k.key)
//}
// #cgo LDFLAGS: -L./src
