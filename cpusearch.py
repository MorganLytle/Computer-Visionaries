
def cpuSearch(licPlate):

	present = random.randint(0,1)
	i = 1
	while i < 2:
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
	                #call api for pic info
        	        apiData = cv.apiCall()
                	licPlate = apiData.licPlate
                	def getLic(licPlate):
                        	return licPlate

			#car entered/leave the parking lot
			if (present == 0):
				present = 1
				print('Car ' + licPlate +' entered')
			else:
				present = 0
				print('Car '+ licPlate + ' left')
       		#call api for pic info
#        	apiData = cv.apiCall()
#        	licPlate = apiData.licPlate
#        	def getLic(licPlate):
#        		return licPlate		 

        	foundLocation = Database_Size+1 #value if plate not in database

        	#print("\nUnsorted List\n")

#        	startTime = time.clock()
        	for row in range(0, (Database_Size - 1)):
                	if(Array_List[row]==plateNum):
                        	foundLocation = row
                        	break

                if(foundLocation > Database_Size):
                        print('License plate ' + plateNum + ' not found in unsorted database')
                else:
                        print('License plate ' + plateNum + ' found in unsorted database at position ' + str(foundLocation)+"\n")

	       		#call dictionary info
			print('Car information')
			print('license plate: ' + licPlate)
			if(present == 1):
				print('Car is in the parking lot')
			else:
				print('Car is not in the paking lot')
	
#       	unsortedRuntime = float(time.clock()-startTime)
#        	print("Time used to find license plate in unsorted list: ")
#       	print(str(decimal.Decimal(unsortedRuntime))+ " seconds\n")

		
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

