
/* 
 * File:   main.cpp
 * Author: Roland Carter
 * Date: 2020-08-30
 */

#include <iostream>
#include<string>
#include <cmath>

using namespace std;

int main() {
    // initialize binary strings and ints
    string binary, b;
    int digit, i;
    int finalNum = 0;
    
    // prompt user for binary string
    cout << "Enter a binary string: ";
    cin >> binary;
    
    for(i = 0; i <= binary.length() - 1; ++i)
    {
        // get binary string token
        b = binary[i];
        
        // convert token (0 or 1) to integer
        digit = atoi(b.c_str());
        
        // add resulting outputs for each 2^
        finalNum += (digit * pow(2, binary.length() - 1 - i));
    }
    // print output matrix C in matrix form
    std::cout << "Base 10 Output: " << finalNum << endl;

    return 0;
}