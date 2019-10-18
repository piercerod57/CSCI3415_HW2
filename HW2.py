#CSCI 3415 - Principles of Programming Languages
#Fall 2019 - Program 2 - Python
#Dr. Doug Williams
#Pierce Hopkins

import os
import math

def main():
	class Decade:
		def __init__(self, year):
			self.year = year
			self.maleDict = dict()
			self.femaleDict = dict()
	#Open the file back and read the contents
	years = os.listdir('./data/')
	
	yearArray = []
	decades = []
	
	#-----------------File-Read-----------------
	for year in years:
		
		yearMaleArray = []
		yearFemaleArray = []
		
		print("Attempting to read: " + year)
		file = open("./data/" + year, "r")
		fl = file.readlines()
		
		for line in fl:
			x = line.split(',')
			x[2] = x[2].replace("\n", "")
			nameEntry = dict(name = x[0], gender = x[1], count = x[2])
			
			if nameEntry["gender"] == "M":
				yearMaleArray.append(nameEntry)
			elif nameEntry["gender"] == "F":
				yearFemaleArray.append(nameEntry)
		
		yearDict = dict(year = year.strip("yob.txt"), maleNames = yearMaleArray, femaleNames = yearFemaleArray)
		yearArray.append(yearDict)
	#-----------------File-Read-----------------
	
	
	#---------------Parse-Decades---------------
	decadesLength = math.ceil(len(yearArray)/10)
	print("Data found for %s decades:"%(decadesLength))
	
	for i in range(decadesLength):
		print("\t The %s's"%(yearArray[i*10]["year"]))
		newDecade = Decade(yearArray[i*10]["year"])
		decades.append(newDecade)
		for j in range(10):
			if (( i * 10 ) + j) < len(yearArray):
				#print(yearArray[(( i * 10 ) + j)]["year"])
				for maleName in yearArray[(( i * 10 ) + j)]["maleNames"]:
					#if maleName["name"] in decades[i].maleDict:
					#	decades[i].maleDict[maleName["name"]] = decades[i].maleDict.get(maleName["name"]) + maleName["count"]
					#else:
					decades[i].maleDict[maleName["name"]] = maleName["count"]
						
				
				for femaleName in yearArray[(( i * 10 ) + j)]["femaleNames"]:
					#if femaleName["name"] in decades[i].femaleDict:
					#	decades[i].femaleDict[femaleName["name"]] = decades[i].femaleDict.get(femaleName["name"]) + femaleName["count"]
					#else:
					decades[i].femaleDict[femaleName["name"]] = femaleName["count"]
			else:
				break
	#---------------Parse-Decades---------------
	for key,val in decades[0].maleDict.items():
		print(key, "=>", val)
	

if __name__ == '__main__':
	main()