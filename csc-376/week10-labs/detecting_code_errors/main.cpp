/*
 * Create a program in C++ which checks for 1 bit errors in an error detection 
 * system which uses a single parity bit (the single parity bit checks the 
 * parity of all bits in each code).  Each code is 8 bits (7 bits for data and 
 * one for parity). The code distance is 2. You program should check for even 
 * parity (parity bit is 1 for even parity). Your program should allow the user 
 * to input a single unsinged decimal value up to 255, and then output whether 
 * there is a 1 bit error or not.
 */

/* 
 * File:   main.cpp
 * Author: rolandcarter
 *
 */

#include <iostream>

using namespace std;


int main() {
    // initialize variables
    unsigned int userInput, finalBit;
    
    // get user input
    cout << "Enter a number between 0 and 255 (including 0 and 255):";
    cin >> userInput;
    
    // get least significant bit in user's input
    finalBit = userInput & 1;
    
    // count the number of bits in the user input 
    // this also includes the parity bit, so decrement if it is 1
    int numberBits = 0;
    while(userInput){
        // increment if least bit is 1
        numberBits += userInput &1;
        // shift one bit to the right
        userInput >>= 1;
    }
    // decrement if it is 1
    if(finalBit == 1){
        --numberBits;
    }
    
    // output the number of set bits and parity bits
    cout << endl << "Number of set bits: " << numberBits << endl;
    cout << "Parity bit: " << finalBit << endl;
    
    // else-if statement for if the number of bits is even
    if(numberBits % 2 == 0){
        if(finalBit == 0){
            cout << "Bit error present";
        }
        else if (finalBit != 0){
            cout << "Bit error not present";
        }
    }
    // else-if statement for if the number of bits is odd
    else if (numberBits % 2 != 0){
        if(finalBit == 0){
            
            cout << "Bit error not present";
        }
        else if (finalBit != 0){
            cout << "Bit error present";
        }
    }
    
    return 0;
}

