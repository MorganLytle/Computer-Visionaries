
def cpuSearch(licPlate):

        print("CPU implementation\n")
        #user interface
        plateNum = raw_input('Type the license plate number you are looking for ')
        while(len(plateNum) != 7):
                plateNum =  raw_input('License plate number was not recognized. Please try again: ')

        hardCodedLocation = random.randint(0, Database_Size - 1)
        Array_List[hardCodedLocation] = licPlate
        #Lic_Plate_Array = list(licPlate) #not sure what this is
        print("\n"+ "Test string at position " + str(hardCodedLocation) +"\n")
        print(Array_List)

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
        while(len(plateNum) != 7):
                plateNum =  raw_input('License plate number was not recognized. Please try again: ')

        hardCodedLocation = random.randint(0, Database_Size - 1)
        Array_List[hardCodedLocation] = licPlate
        #Lic_Plate_Array = list(licPlate) #not sure what this is
        print("\n"+ "Test string at position " + str(hardCodedLocation) +"\n")
        print(Array_List)

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

