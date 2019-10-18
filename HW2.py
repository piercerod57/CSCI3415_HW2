#CSCI 3415 - Principles of Programming Languages
#Fall 2019 - Program 2 - Python
#Dr. Doug Williams
#Pierce Hopkins

import os
import math
import itertools  
import collections 

def main():
	#--------------Class-Definitions--------------
	class Year:
		def __init__(self, year, maleDict, femaleDict):
			self.year = year
			self.maleDict = maleDict
			self.femaleDict = femaleDict
	
	class Decade:
		def __init__(self, year):
			self.year = year
			self.maleDict = dict()
			self.femaleDict = dict()
	#--------------Class-Definitions--------------
	
	#Open the files and read the contents
	#-----------------File-Read-----------------
	years = os.listdir('./data/')
	
	yearArray = []
	decades = []
	
	for year in years:
		
		yearMaleDict = {}
		yearFemaleDict = {}
		
		print("Attempting to read: " + year)
		file = open("./data/" + year, "r")
		fl = file.readlines()
		
		for line in fl:
			x = line.split(',')
			x[2] = x[2].replace("\n", "")
			
			if x[1] == "M":
				yearMaleDict[x[0]] = int(x[2])
			elif x[1] == "F":
				yearFemaleDict[x[0]] = int(x[2])
		
		newYear = Year(year.strip("yob.txt"), yearMaleDict, yearFemaleDict)
		yearArray.append(newYear)
	#-----------------File-Read-----------------
	
	
	#---------------Parse-Decades---------------
	decadesLength = math.ceil(len(yearArray)/10)
	print("Data found for %s decades:"%(decadesLength))
	
	for i in range(decadesLength):
		print("\t The %s's"%(yearArray[i*10].year))
		newDecade = Decade(yearArray[i*10].year)
		decades.append(newDecade)
		for j in range(10):
			if (( i * 10 ) + j) < len(yearArray):
				#print(yearArray[(( i * 10 ) + j)]["year"])
				#@NOTE(P): Break these for loops into function?
				newMaleDict = collections.defaultdict(int)
				for key, val in itertools.chain(decades[i].maleDict.items(), yearArray[(( i * 10 ) + j)].maleDict.items()):
					newMaleDict[key] += val
				
				decades[i].maleDict.clear()
				decades[i].maleDict = newMaleDict.copy()
				
				newFemaleDict = collections.defaultdict(int)
				for key, val in itertools.chain(decades[i].femaleDict.items(), yearArray[(( i * 10 ) + j)].femaleDict.items()): 
					newFemaleDict[key] += val
					
				decades[i].femaleDict.clear()
				decades[i].femaleDict = newFemaleDict.copy()
				#for key in yearArray[(( i * 10 ) + j)].maleDict: 
				#	if key in decades[i].maleDict:
				#		
				#	else: 
				#		decades[i].maleDict[key] = yearArray[(( i * 10 ) + j)].maleDict[key]
				#		pass
				#for key in yearArray[(( i * 10 ) + j)].femaleDict: 
				#	if key in decades[i].femaleDict: 
				#		newDict = Counter(decades[i].femaleDict) + Counter(yearArray[(( i * 10 ) + j)].femaleDict[key])
				#		decades[i].femaleDict.clear()
				#		decades[i].femaleDict = newDict.copy()
				#	else: 
				#		decades[i].femaleDict[key] = yearArray[(( i * 10 ) + j)].femaleDict[key]
				#		pass
			else:
				break
	#---------------Parse-Decades---------------
	#for key,val in decades[0].maleDict.items():
	#	print(key, "=>", val)
		
	for key,val in decades[0].femaleDict.items():
		print(key, "=>", val)
	

if __name__ == '__main__':
	main()