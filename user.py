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
#apiData = cv.apiCall()
#licPlate = apiData.licPlate

#def getLic(licPlate):
#	return licPlate

#hardcode licPLate to be in the random database
licPlate = "6VJV182"
#hardcode test licPlate to database
hardCodedLocation = random.randint(0, Database_Size - 1)
Array_List[hardCodedLocation] = licPlate
print("\n"+ "Test string at position " + str(hardCodedLocation) +"\n")
print(Array_List)


def cpuSearch(licPlate): 
	print("CPU implementation\n")
	#user interface
	plateNum = raw_input('Type the license plate number you are looking for ')
	while(len(plateNum) != 7):
		plateNum =  raw_input('License plate number was not recognized. Please try again: ')


        #no car in the parking lot
        present = 0
        flag = random.randint(0,1)
#        print(flag)
	if(flag == 1):
                #car enter/leave the parking lot
                #car entered
		present = 1
                if(present == 1):
                        print('Car entered')
	                #calling license plate
        	        apiData = cv.apiCall()
               		licPlate = apiData.licPlate
                	conf = apiData.conf
	                reg = apiData.reg
	
        	        def getLic(licPlate):
                	        return licPlate

              		def getConf(conf):
                       		return conf

	                def getReg(reg):
        	                return reg

               	else:
			pass
                        #print("\n"+"Car left"+"\n")
	else:
		pass


	foundLocation = Database_Size+1 #value if plate not in database
	
	for row in range(0, (Database_Size - 1)):
		if(Array_List[row]==plateNum):
			foundLocation = row
			break
	if(foundLocation > Database_Size):
		print("\nLicense plate not found in unsorted database\n")
	else:
		print("\nLicense plate found in unsorted database at position " + str(foundLocation)+ "\n")
		print('print informaton')
		print('Owner: Morgan')
		print('licPlate: '+ licPlate)
		if (present == 1):
			print('Confidence: ' + str(conf))
			print('Region: ' + str(reg))
			print('Car in the parking lot')
		else:
			print('Car not in the parking lot')
			pass

	#no car in the parking lot
#	present = 0
#	flag = random.choice([0,1])
#	if(flag == 1)
#		#car enter/leave the parking lot 
#		present = !present
#		if(present == 1)
#			print("\n"+"Car entered"+"\n")
#		else:
#			print("\n"+"Car left"+"\n")			

def main():
	cpuSearch(licPlate)
if __name__ == "__main__":
	main()
 
