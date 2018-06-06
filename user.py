import cv
import random
import numpy as np

#initialize list
M = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G',
'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

String = ""
Array_List = [] 
Database_Size = 100
for y in range(0,(Database_Size-1)):
	#create random license plate
	for x in range(0,7):
		RandIndex = random.randint(0,35)
		RandChar = M[RandIndex]
		String = String+RandChar
	#put the string in an array 
	Array_List.append(String)
	String = ""

#calling license plate
licPlate = cv.apiCall()
def getLic(licPlate):
	return licPlate

#hardcode test license plate
i = random.randint(0,(Database_Size-1))
Array_List[i] = licPlate
print (i)
print(Array_List)

def cpuSearch(licPlate): 
	print("CPU implementation\n")
	#user interface
	plateNum = raw_input('Type the license plate number you are looking for ')
	userNum = [plateNum]	
	while(len(plateNum) != 7):

		plateNum =  raw_input('License plate number was not recognized. Please try again: ')
	#hardcode test licPlate to database
#	hardCodedLocation = random.randint(0, Database_Size - 1)
#	Array_List[hardCodedLocation] = licPlate
#	print(Array_List)

	#foundLocation = Database_Size+1 #value if plate not in database
	
	for row in range(0, (Database_Size - 1)):
		if(Array_List[row]==plateNum):
			foundLocation = row
			break
		else:
			foundLocation = Database_Size + 1 #value if plate not in database
	if(foundLocation > Database_Size):
		print("\nLicense plate not found in unsorted database\n")
	else:
		print("\nLicense plate found in unsorted database at position " + str(foundLocation)+ "\n")

def main():
	cpuSearch(licPlate)
if __name__ == "__main__":
	main()
 