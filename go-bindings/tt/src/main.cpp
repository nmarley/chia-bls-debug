#include "key.hpp"

#include <iostream>

int main(void) {
    Key k1;
    Key k2;

    k2.SetColour("gold");

    std::cout << "k1 colour is: " << k1.GetColour() << std::endl;
    std::cout << "k2 colour is: " << k2.GetColour() << std::endl;
}
