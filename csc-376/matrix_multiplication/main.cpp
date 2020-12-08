
/* 
 * File:   main.cpp
 * Author: Roland Carter
 * Date: 2020-08-30
 */

#include <iostream>

using namespace std;

int main() {
    // initialize matrices
    // note: A, B written as two 2x2 arrays for added readability   
    int A[5][5] = {{2, 3, 5, 6, 1},{2, 5, 6, 2, 3}};
    int B[5][5] = {{4, 8, 5, 3, 1},{7, 6, 4, 6, 2}};
    int C[5][5];
    int squareMatrixSize = 5;
    
    // initialize index elements for multiplication
    int i, j, k;
    
    // iterate through index elements
    // note: two iterations are done in this case, hence the hard coded 2,
    // but in a generalized program, these would be replaced by the row and
    // column lengths
    for (i = 0; i < squareMatrixSize; ++i)
    {
        for (j = 0; j < squareMatrixSize; ++j)
        {
            C[i][j] = 0;
            for (k = 0; k < squareMatrixSize; ++k)
            {
                C[i][j] +=  A[i][k] * B[k][j];
            }
        }
    }
    
    // print output matrix C in matrix form
    std::cout << "Matrix Multiplication Output:" << endl;
    for(i = 0; i < squareMatrixSize; ++i)
    {
        for(j = 0; j < squareMatrixSize; ++j)
        {
            cout << "\t" << C[i][j];
            if(j == squareMatrixSize-1)
                cout << endl;
        }
    }
    
    return 0;
}