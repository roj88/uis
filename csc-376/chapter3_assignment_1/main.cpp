/*
 * Write a C++ program that asks the user to input a decimal integer 
 * (i) and an integer radix from 2 to 16 (r) and outputs the value of
 * i in radix r (base r). (HINT: use repeated division by base r)
 */

/* 
 * File:   main.cpp
 * Author: rolandcarter
 *
 */

#include <iostream>
#include<string>

using namespace std;

int main() {
    // initialize decimal strings and ints
    string decimal, base;
    int i = 0;
    int intArray[16], d, b;
    
    // prompt user for decimal string
    cout << "Enter a decimal number string: ";
    cin >> decimal;
    
    // prompt user for base string
    cout << "Enter an integer radix from 2 to 16 (base 2 to 16): ";
    cin >> base;
    
    // convert strings to int
    d = atoi(decimal.c_str());
    b = atoi(base.c_str());
    
    // while loop performs modulus on decimal until it is 0
    while (d > 0)
    {
        intArray[i] = d % b;
        d = d / b;
        ++i;
    }

    // print output
    std::cout << "Base " << base << " number: ";
    for(int j = i - 1; j >= 0; --j)
    {
        std::cout << intArray[j];
    }

    return 0;
}
