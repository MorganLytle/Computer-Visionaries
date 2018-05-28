import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import cv #import api call script
import numpy as np
import random

#initialize list
M = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I',
'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

Database_Size = 100
String = ""
Array_List = [] #initialize list for cpu implementation 
                #list use for cpu for alphabetizing to optimize search
Array_List_Sorted = []
Array_H = np.empty(Database_Size, 7) #initialize empty array to be copied to GPU
Array_GPU = cuda.mem_alloc(Array_H.nbytes) #Allocates GPU memory for database

Num_Digits = int32(Database_Size * 7)

for y in range(0,(Database_Size - 1)):
	#create random license plate
	for x in range(0,7):
		RandIndex = random.randint(0,35)
		RandChar = M[RandIndex]
		String = String+RandChar
    Array_H[y][x] = RandChar
	
	Array_List.append(String) #put the string at the end of the list 
	String = ""

#calling license plate
licPlate = cv.apiCall()

def getLic(licPlate):
#	print (licPlate)
	return licPlate

#hardcode test license plate
i = random.randint(0, Database_Size - 1)
Array_List[i] = licPlate
Lic_Plate_Array = list(licPlate)
print("\n"+ "Test string at position " + str(i) +"\n")
print(Array_List)

cuda.memcpy_htod(Array_GPU, Array_H) #transfers array to GPU

#cuda kernel python wrapper
mod = SourceModule("""
  __global__ void listSearch(char Array_GPU, int32 Num_Digit, char licPlate){ // FIXME FIX PARAMETERS
  __shared__ float currentRow[7];
  
  int Row = blockIdx.y * blockDim.y + threadIdx.y;
  int Col=0;
  int matchedChar = 0;
  
  for(int y = 0; y < 7; ++y) //put current row into shared memory
  {
    currentRow[y] = Array_GPU[Row][y];
  }
  __syncthreads();
    
  while(Col < 7) //search current row to match with the licPlate
  {
    if(currentRow[Col] == licPlate[Col])
    {
      ++matchedChar;
    }
    
    else
    {
      matchedChar = 0;
      y = 0;
      break;
    }
    ++y;
  }
  if(matchedChar == 7)
  {
    licensePlateIndex_d = Row
  }
  else
  {
    licensePlateIndex_d = Database_Size + 1; //not found
  }
  __syncthreads();
  }
  """) 
  
grid = (,) #FIXME ADD GRID DIMENSIONS
block = (,,) #FIXME ADD BLOCK DIMENSIONS
function = mod.get_function("listSearch")
function() #FIXME ADD PARAMETERS

licensePlateIndex_h = 0

cuda.memcpy_dtoh(licensePlateIndex_h, licensePlateIndex_d) #returns location of license plate

if (licensePlateIndex_h >= Database_Size):
  print("License Plate not in database. \n")
  
  else: 
    print(licensePlateIndex_h)
    
    

 

