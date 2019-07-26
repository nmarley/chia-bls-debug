package num

import "testing"

func TestNum(t *testing.T) {
	num := New()
	num.Inc()
	if num.GetValue() != 2 {
		t.Error("unexpected value received")
	}
	num.Inc()
	num.Inc()
	num.Inc()
	if num.GetValue() != 5 {
		t.Error("unexpected value received")
	}

	num.Free()
}
