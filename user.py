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
#hardCodedLocation = random.randint(0, Database_Size - 1)
#Array_List[hardCodedLocation] = licPlate
#print("\n"+ "Test string at position " + str(hardCodedLocation) +"\n")
#print(Array_List)


def cpuSearch(licPlate):

        present = random.randint(0,1)
        i = 1
        while (i<2):
                print("CPU implementation\n")
                #user interface
                plateNum = raw_input('Type the license plate number you are looking for ')
                while(len(plateNum) != 7):
                        plateNum =  raw_input('License plate number was not recognized. Please try again: ')

                hardCodedLocation = random.randint(0, Database_Size - 1)
                Array_List[hardCodedLocation] = licPlate
                print("\n"+ "Test string at position " + str(hardCodedLocation) +"\n")
                print(Array_List)

                #randomlize car in parking or not
                present = random.randint(0,1)
                #randomlize car enter or not
                flag = random.randint(0,1)
                if (flag == 1):
                        #car entered/leave the parking lot
                        if (present == 0):
                                present = 1
                                print('Car entered')
                        else:
                                present = 0
                                print('Car left')
               		#call api for pic info
                	apiData = cv.apiCall()
                	licPlate = apiData.licPlate
                	def getLic(licPlate):
                        	return licPlate
			#JUSTADD
			print('license plate of the car just entered: ' + licPlate)
		else:
			print('No car has entered or left the parking lot')

                foundLocation = Database_Size+1 #value if plate not in database

                print("\nUnsorted List\n")

#                startTime = time.clock()
                for row in range(0, (Database_Size - 1)):
                        if(Array_List[row]==plateNum):
                                foundLocation = row
                                break
                if(foundLocation > Database_Size):
                        print('License plate ' + plateNum + ' not found in unsorted database')
                else:
                        print('License plate ' + plateNum + ' found in unsorted database at position ' + str(foundLocation)+"\n")
                        #call dictionary info
                        print('license plate: ' + licPlate)
                        if(present == 1):
                                print('Car is in the parking lot')
                        else:
                                print('Car is not in the paking lot')

#                unsortedRuntime = float(time.clock()-startTime)
#                print("Time used to find license plate in unsorted list: ")
#                print(str(decimal.Decimal(unsortedRuntime))+ " seconds\n")


                cont = raw_input('Do you want to make another search (Y/N)?')
		#if(cont == Y)
		#	i = 1
			
		
	
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
		
def main():
	cpuSearch(licPlate)
if __name__ == "__main__":
	main()
 
