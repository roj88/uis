
/* 
 * File:   main.cpp
 * Author: Roland Carter
 * Date: 2020-08-30
 */

#include <iostream>
#include<string>

using namespace std;
int closest(int arr[], int target, int i, int n)
{
    //at each index we have got two options
    //to put + in front or to put - in front of it
    //accordingly call the recursion function
    if (i == n)
        return 0; //when the index reaches the end of the array

    int sum1 = arr[i] + closest(arr, target - arr[i], i + 1, n); //first when we put + , here we also
                                                                 //changed the target as we have put sum number in the bucket already

    int sum2 = -1 * arr[i] + closest(arr, target + arr[i], i + 1, n); //second when we put -1, here also we changed the
                                                                      // target due to the same reason

    //we check which one is closest to target here
    if (abs(sum1 - target) < abs(sum2 - target))
    {
        return sum1; //difference is closer
    }
    else
    {
        return sum2;
    }
}

int main()
{
    int n = 7;                          //size of the list
    int arr[] = {6, 5, 3, 2, 8, 10, 9}; //list
    int target = 17;                    //target value
    ///findthe closest number after adding
    cout << closest(arr, target, 0, n) << endl;

}
