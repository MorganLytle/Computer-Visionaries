#include <stdio.h> //Import libraries and files
#include <stdlib.h>
#include "kernel.cu"

int main (){









/*
Allocate memory for the database on the host and the device
*/

/*make an array of char 0-9 and A-Z and randomize it*/
int Array[36] = {0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z};

/*
random variable that is 0 or 1
if 0 generate a random integer (0-9)
if 1 generate a random letter(A-Z)
fill two dimensional array with these characters
*/
int seed = 1;
srand(seed);
int M = 35;

A_col = 7;
A_row = 100;
A_sz = A_row*A_col;
B_sz = A_row;

    A_h = (float*) malloc( sizeof(float)*(A_sz) );
    for (unsigned int i=0; i < A_sz; i++) { A_h[i] = (rand()%100)/100.00; }

    B_h = (float*) malloc( sizeof(float)*B_sz );
    for (unsigned int i=0; i < B_sz; i++) { B_h[i] = (rand()%100)/100.00; }

    stopTime(&timer); printf("%f s\n", elapsedTime(timer));
    printf("    size Of vector: %u x %u\n  ", VecSize);


}
