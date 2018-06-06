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
'Caroline', 'Calvin', 'Nick', 'Ahri', 'POOP']

lastNames = ['Thagreat', 'Wong', 'Lam', 'Choi', 'Theboss',
'Thefrog', 'Lilwayne', 'Falcon', 'Ike', 'Vert'
'Marth', 'Fox', 'Marvel', 'Waconda', 'Uzi',
'Mario', 'Luigi', 'Cashmioutsyd', 'Howbowdat', 'Korotkov', 'SCOOP']

Database_Size = 100
String = ""
Array_List = [] #initialize list for cpu implementation 
                #list use for cpu for alphabetizing to optimize search
Array_List_Sorted = []
Array_H = np.chararray((Database_Size,7))#initialize empty array to be copied to GPU
#Array_GPU = cuda.mem_alloc(Array_H.nbytes) #Allocates GPU memory for database
#Array_GPU = cuda.mem_alloc(databaseClasses.nbytes)
Num_Digits = int(Database_Size * 7)
databaseClasses = []

class dataBase:
	def __init__(test, licPlate, reg, name, present, wanted):
		test.licPlate = licPlate
		test.reg = reg
		test.name = name
		test.present = present
		test.wanted = wanted

for y in range(0,(Database_Size - 1)):
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
	
	RandClass = dataBase(String, RandRegion, RandName, RandPres, RandWanted)
	databaseClasses.append(RandClass)	
	print(databaseClasses[y].name) 
	#databaseClasses[y] = dataBase.append(String, RandRegion, RandName, RandPres, RandWanted)

	#FIXME: assign string to array of class
	#FIXME: randomly fill names
	#FIXME: fill present and wanted vars 0 or 1 		
	Array_List.append(String) #put the string at the end of the list 
	String = ""

databaseGPU = cuda.mem_alloc(databaseClasses.nbytes)

#calling license plate
apiData = cv.apiCall()
licPlate = apiData.licPlate
print("-----------------------------------\n")

def getLic(licPlate):
#	print (licPlate)
	return licPlate
def cpuSearch(licPlate): 

	print("CPU implementation\n")
	#hardcode test license plate
	hardCodedLocation = random.randint(0, Database_Size - 1)
	Array_List[hardCodedLocation] = licPlate
	#Lic_Plate_Array = list(licPlate) #not sure what this is 
	print("\n"+ "Test string at position " + str(hardCodedLocation) +"\n")
	#print(Array_List)

	foundLocation = Database_Size+1 #value if plate not in database

	print("\nUnsorted List\n")

	startTime = time.clock()
	for row in range(0, (Database_Size - 1)):
		if(Array_List[row]==licPlate):
			foundLocation = row
			break
	if(foundLocation > Database_Size):
		print("\nLicense plate not found in unsorted database\n")
	else:
		print("\nLicense plate found in unsorted database at position " + str(foundLocation)+ "\n")
	unsortedRuntime = float(time.clock()-startTime) 
	print("Time used to find license plate in unsorted list: ")
	print(str(decimal.Decimal(unsortedRuntime))+ " seconds\n")

	#create sorted list
	Array_List_Sorted = sorted(Array_List)

	print("\nSorted List\n")
	print(Array_List_Sorted)

	foundLocation = Database_Size + 1 #value if plate not in database
	startTime = time.clock()
	for row in range(0, (Database_Size - 1)):
		if(Array_List_Sorted[row]==licPlate):
			foundLocation = row
			break 

	if(foundLocation > Database_Size):
		print("\nLicense plate not found in sorted database\n")  
	else:
		print("\nLicense plate found in sorted database at position " + str(foundLocation)+ "\n")
	sortedRuntime = float(time.clock() - startTime)
	print(str(decimal.Decimal(sortedRuntime))+ " seconds\n")
	print("-----------------------------------\n")


#cuda.memcpy_htod(Array_GPU, Array_H) #transfers array to GPU

#cuda kernel python wrapper
#mod = SourceModule("""
	#__global__ void listSearch(char Array_GPU, int32 Num_Digit, char licPlate){ // FIXME FIX PARAMETERS
	#__shared__ float currentRow[7];
  
	#int Row = blockIdx.y * blockDim.y + threadIdx.y;
	#int Col=0;
	#int matchedChar = 0;
  
	#for(int y = 0; y < 7; ++y) //put current row into shared memory
	#{
		#currentRow[y] = Array_GPU[Row][y];
	#}
	#__syncthreads();
    
	#while(Col < 7) //search current row to match with the licPlate
	#{
		#if(currentRow[Col] == licPlate[Col])
		#{
			#++matchedChar;
		#}
    
		#else
		#{
			#matchedChar = 0;
			#y = 0;
			#break;
		#}
		#++y;
	#}
	#if(matchedChar == 7)
	#{
		#licensePlateIndex_d = Row
	#}
	#else
	#{
		#licensePlateIndex_d = Database_Size + 1; //not found
	#}
	#__syncthreads();
	#}
	#""") 
  
#grid = (,) #FIXME ADD GRID DIMENSIONS
#block = (,,) #FIXME ADD BLOCK DIMENSIONS
#function = mod.get_function("listSearch")
#function() #FIXME ADD PARAMETERS

#licensePlateIndex_h = 0

#cuda.memcpy_dtoh(licensePlateIndex_h, licensePlateIndex_d) #returns location of license plate

#if (licensePlateIndex_h >= Database_Size):
	#print("License Plate not in database. \n")
  
	#else: 
		#print(licensePlateIndex_h)
    
def main():
	cpuSearch(licPlate)	 
if __name__ == "__main__":
	main()
 

