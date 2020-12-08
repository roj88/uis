/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: rolandcarter
 *
 * Created on September 11, 2020, 12:19 AM
 */

#include <iostream>
#include <bitset>
#include <cmath>
using namespace std;


// main method
int main(){
   // declare variables
   int a, b, c, d, numberBits, userInput;
   unsigned int bit;
   

    
   // prompt the user to input an ip address and get input
   cout << "Enter an IP address (press enter between each dotted quad value):"<< endl;
   cin >> a >> b >> c >> d;
   
   
   // get user input on how they would like address displayed
   cout << "\n\nHow would you like to see your IP address:" << endl;
   cout << "\n1) Single value\n2) Four values\n3) Two values\n4) A single bit value" << endl;
   cout << "\n\nEnter your option:" << endl;
   cin >> userInput;
   
   // convert dotted quad to single int
   unsigned int singleValue = (a * pow(256, 3)) +
                              (b *pow(256, 2)) + 
                              (c * pow(256, 1))+
                              d;
   

   // return single int
   if(userInput==1){
       // print the ip4 as a single value
           cout << singleValue;
   }
   // return as quad 
   else if(userInput==2){
           // cout as dotted quad
           cout << a << "." << b << "." << c << "." << d << endl;
   }
       
   // return two ints
   else if(userInput==3){
       // prompt the user for the number of bits
       // TODO: I had an issue with this as i couldn't set the bitset<n> dynamically
       // sinc n is a constant
       // also a bit sloppy
           cout << "How many bits in the network address:" << endl;
           cin >> numberBits;
           
           // create union of items
           union Combine_network{
                char ip4_network[32];
                short target;
           };
           union Combine_host{
                char ip4_host[32];
                short target;
           };
           
           // define unions
           Combine_network cn;
           Combine_host ch;
           cn.ip4_network[1] = a, cn.ip4_network[0] = b;
           ch.ip4_host[1] = c, ch.ip4_host[0] = d;
           
           // set binaries to variables
           bitset<16> binaryNumNetwork(cn.target);
           bitset<16> binaryNumHost(ch.target);

           
           // return decimal values of unions
           cout << "\n\n" << binaryNumNetwork.to_ulong() << "," << binaryNumHost.to_ulong() << endl;
   }
   // return the bit number
   else if(userInput==4){
           cout<<"Which bit would you like to see: ";
           cin >> bit;
           
           if((1<<bit)&singleValue){
                cout<<1;
           }
            else{
               cout<<0;
            }
    }
           
 }
