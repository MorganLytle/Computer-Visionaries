import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import cv #import api call script
import numpy as np
import random
import time
import decimal

#initialize list
M = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G',
'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

regions = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
'North Carolina', 'North Dakota', 'Ohio, Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
'West Virginia', 'Wisconsin', 'Wyoming', 'Canada'] 

firstNames = ['Jenn', 'Janis', 'Jasmine', 'Jessica', 'Zoey',
'Bob', 'Captain', 'Sam', 'Morgan', 'Kevin', 'Tsz',
'Daniel', 'Richard', 'Kermit', 'Justin', 'Uriel',
'Caroline', 'Calvin', 'Nick', 'Ahri', 'Tsz']

lastNames = ['Thagreat', 'Wong', 'Lam', 'Choi', 'Theboss',
'Thefrog', 'Lilwayne', 'Falcon', 'Ike', 'Vert'
'Marth', 'Fox', 'Marvel', 'Waconda', 'Uzi',
'Mario', 'Luigi', 'Cashmioutsyd', 'Howbowdat', 'Korotkov', 'SCOOP']

Database_Size = 1000
String = ""
Array_List = [] #initialize list for cpu implementation 
                #list use for cpu for alphabetizing to optimize search
Array_List_Sorted = []
Array_H = np.chararray((Database_Size,7))#initialize empty array to be copied to GPU
print(type(Array_H))
Array_GPU = cuda.mem_alloc(Array_H.nbytes) #Allocates GPU memory for database
Num_Digits = int(Database_Size * 7)
databaseClasses = []

licensePlate = {}
hardCodedLocation = 0
def getLic():
        #calling license plate API
        apiData = cv.apiCall()
        licPlate = apiData.licPlate
        return licPlate


for y in range(0,(Database_Size)):
	#create random license plate
	for x in range(0,7):
		RandIndex = random.randint(0,35)
		RandChar = M[RandIndex]
		String = String+RandChar
                Array_H[y][x] = RandChar
	
	RandRegion = regions[random.randint(0,49)]
	RandName = firstNames[random.randint(0,19)] + ' ' + lastNames[random.randint(0,19)]
	RandPres = random.choice([0,1])
	RandWanted = random.choice([0, 1])	

	innerPlate = {'plateNum':String, 'name':RandName, 'region':RandRegion, 'present':RandPres, 'wanted':RandWanted}
	licensePlate[y] = innerPlate

	Array_List.append(String) #put the string at the end of the list 
	String = ""
	
apiInfo = cv.apiCall()
hardCodedLocation = random.randint(0, Database_Size - 1)
hardCodedPlate = getLic()
hardCodedReg = apiInfo.reg
hardCodedName = "Morgan Lytle"
#RandPres = licensePlate[hardCodedLocation]['present']
RandWanted = licensePlate[hardCodedLocation]['wanted']

innerPlate = {'plateNum':hardCodedPlate, 'name':hardCodedName, 'region':hardCodedReg, 'wanted':RandWanted}
licensePlate[hardCodedLocation] = innerPlate

#Array_List[hardCodedLocation] = getLic()
#print("\n"+ "Test string at position " + str(hardCodedLocation) +"\n")
#print(Array_List)

#print(licensePlate[1])
#print(licensePlate[1]['region']) 
print("-----------------------------------\n")

#size = np.int32(2560)
#Array_H = np.random.randn(1, size).astype(np.float32)

cuda.memcpy_htod(Array_GPU, Array_H) #transfers array to GPU
Num_Digits = np.int32(Database_Size * 7)
#cuda kernel python wrapper
mod = SourceModule("""
	__global__ void gpuSearch(char** Array_GPU, int Database_Size, int Num_Digits, char* licPlate){ 
	__shared__ float currentRow[7];
  
	int Row = blockIdx.y * blockDim.y + threadIdx.y;
	int Col=0;
	int matchedChar = 0;
  	int licensePlateIndex = 0;
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
			Col = 0;
			break;
		}
		++Col;
	}
	if(matchedChar == 7)
	{
		licensePlateIndex = Row;
	}
	else
	{
		licensePlateIndex = Database_Size + 1; //not found
	}
	__syncthreads();
	}
	""") 
licPlate = "6VJV182" #FIXME unhardcode
#Num_Digit = Database_Size*7
blockSize = 256  
grid = (10,1) #FIXME ADD GRID DIMENSIONS
block = (256,1,1) #FIXME ADD BLOCK DIMENSIONS
function = mod.get_function("gpuSearch")
function(Array_GPU, Database_Size, Num_Digits, licPlate, grid = (10,1), block = (256,1,1)) #FIXME ADD PARAMETERS

licensePlateIndex_h = 0

#a_doubled = np.empty_like(Array_H)

cuda.memcpy_dtoh(licensePlateIndex_h, licensePlateIndex_d) #returns location of license plate

if (licensePlateIndex_h >= Database_Size):
	print("License Plate not in database. \n")
  
else: 
	print(licensePlateIndex_h)
    
def main():
	#cpuSearch(licPlate)	 
	licPlate = getLic() #getting api license plate
	present = random.randint(0,1)
        i = 1
        #call api for pic info
       # apiData = cv.apiCall()
       # licPlate = getLic()#apiData.licPlate

	while i < 2:
                print("CPU implementation\n")
                #user interface
                plateNum = raw_input('Type the license plate number you are looking for ')
                while(len(plateNum) != 7):
                        plateNum =  raw_input('License plate number was not recognized. Please try again: ')

  #             hardCodedLocation = random.randint(0, Database_Size - 1)
                Array_List[hardCodedLocation] = getLic()
                print("\n"+ "Test string at position " + str(hardCodedLocation) +"\n")
                print(Array_List)

                #randomlize car in parking or not
  #              present = random.randint(0,1)
              

                foundLocation = Database_Size+1 #value if plate not in database

                for row in range(0, (Database_Size - 1)):
                        if(Array_List[row]==plateNum):
                                foundLocation = row
				break

                #randomlize car enter or not
                flag = random.randint(0,1)
                if (flag == 1):
#                        #call api for pic info
 #                       #apiData = cv.apiCall()
                        licPlate = getLic()#apiData.licPlate

                        #car entered/leave the parking lot
                        if (present== 0):
                                present=1
                                print('Car ' + licPlate +' entered')
                        else:
                                present=0
                                print('Car '+ licPlate + ' left')

                if(foundLocation > Database_Size):
                        print('License plate ' + plateNum + ' not found in unsorted database')
                else:
                        print('License plate ' + plateNum + ' found in unsorted database at position ' + str(foundLocation)+"\n")

                        #call dictionary info
                        print('Car information')
                        print('license plate: ' + licPlate)
			print('Owner name: '+ licensePlate[foundLocation]['name'])
			print('Region: '+licensePlate[foundLocation]['region'])	

                        if(present == 1):
                                print('Car is in the parking lot')
                        else:
                                print('Car is not in the paking lot')
			#wanted = random.randint(0,1)
			if (licensePlate[foundLocation]['wanted'] == 1):
				print('The car is wanted')
			else:
				print('The car is not wanted')

                cont = raw_input('Do you want to make another search (Y/N)?')
                while (cont != 'Y' or cont != 'N'):
                        if (cont == 'Y'):
                                i = 1
                                print('Another search')
                                break
                        elif(cont == 'N'):
                                i = 2
                                print('End of searching')
                                break
  			cont = raw_input('Do you want to make another search (Y/N)?')

if __name__ == "__main__":
	main()
 

