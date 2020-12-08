/*
 * Create a program in C++ which simulates a direct cache. The memory array
 * that contains the data to be cached is byte addressable and can contain 256
 * single byte entries or lines. The cache has only 8 entries or lines. 
 * The Data field in each line of the cache is 8 bits. Since the data stored 
 * in each line of the cache is only 8 bits, there is no need for a line field.
 * Only a tag field is needed which is log2(256) = 8 bits.
 * 
 * The memory array can be filled with any values of your choice. The program
 * should work by taking user input of a memory address (index). This input
 * represents the memory data that should be cached. Your program will check the
 * cache to see if the item is already cached. If it is not, your program should
 * count a cache miss, and then replace the item currently in the cache with
 * the data from the inputted address. Allow the user to input addresses (in a
 * loop), until they so choose to end the program. The program 
 */

/* 
 * File:   main.cpp
 * Author: rolandcarter
 *
 */

#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    // the following variables will count cache use outcomes
    // cacheHit is the number of times the cache has the value requested,
    // cacheMiss is the number of times this value is not in the cache
    // cacheAccess is the number of times the program is accessed by the user
    int cacheHit = 0, cacheMiss = 0, cacheAccess = 0;
    int userInput; // store user inputs
    int memoryArraySize = 256;
    
    // main memory and cache memory
    int mainMemory[memoryArraySize];
    int cacheMemory[8];
    
    // create 256 bit array of random ints
    for(int i = 0; i < memoryArraySize; ++i){
        mainMemory[i] = rand() % 101;
    }
    
    // initially fill cache with random values from the main memory
    // giving a 3 % probability that the user input will be cached
    for(int i = 0; i < 8; ++i){
        int randInt256 = rand() % 256;
        cacheMemory[randInt256 % 8] = randInt256;
    }
    
    do{
        cout << "\nEnter a memory reference between 0 and 255 (inclusive), or enter -1 the exit the program: ";
        cin >> userInput;
        
        // error handling for id user enters a value outside of 0 and 255 or -1
        if(userInput < -1 || userInput > 255){
             cout << "Number outside of bounds. Please enter a number between 0 and 255";
             cout << endl;
             cout << endl;
        }
        else{
            if(userInput!=-1){
                // increment accesses
                ++cacheAccess;
            }

            // see if cached in memory
            if(cacheMemory[userInput % 8] == userInput){
                // increment if its a hit
                ++cacheHit;

                // output if it is a hit
                cout << "This memory reference is in the cache (HIT)" << endl;
            }
            else if(cacheMemory[userInput % 8] != userInput && userInput != -1){
                // increment if its a miss
                ++cacheMiss;

                // add value to cache
                cacheMemory[userInput % 8] = userInput;

                // output if it's a hit and let user know its not added to cache
                cout << "This memory reference is not in the cache (MISS)" << endl;
                cout << "Adding this reference to the cache" << endl;
            }
        }
    } while(userInput != -1); // -1 is a user exit
    
    // output cache stats
    cout << "Thank you for using cache program.... Exiting!" << endl;
    cout << endl;
    cout << "Number of accesses:\t" << cacheAccess << endl;
    cout << "Number of hits:\t" << cacheHit << endl;
    cout << "Number of misses:\t" << cacheMiss << endl;
    
    
    return 0;
}