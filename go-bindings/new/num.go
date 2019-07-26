package num

// #include "num.h"
import "C"
import "unsafe"

type GoNum struct {
	num C.Num
}

func New() GoNum {
	var ret GoNum
	ret.num = C.NumInit()
	return ret
}
func (n GoNum) Free() {
	C.NumFree(unsafe.Pointer(n.num))
}
func (n GoNum) Inc() {
	C.NumIncrement(unsafe.Pointer(n.num))
}
func (n GoNum) GetValue() int {
	return int(C.NumGetValue(unsafe.Pointer(n.num)))
}
