#include <stdio.h> //Import libraries and files
#include <stdlib.h>
#include "kernel.cu"











/*
Allocate memory for the database on the host and the device
*/


/*
random variable that is 0 or 1
if 0 generate a random integer (0-9)
if 1 generate a random letter(A-Z)
fill two dimensional array with these characters
*/
A_h = (float*) malloc(sizeof(foat)*A_sz);
for (unsigned int i = 0;i<A_sz;i++)
{A_h[i] =(rand()%100)/100.00}

