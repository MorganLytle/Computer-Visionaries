import numpy as np
import random

String = ""
Array = [] 
#Array = np.empty(100)
M = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I',
'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for y in range(0,99):
	for x in range(0,7):
		RandIndex = random.randint(0,35)
		RandChar = M[RandIndex]
		String = String+RandChar
	#put the string in an array 
	Array[y].append(string)
#print(String)
print(Array)
