#CSCI 3415 - Principles of Programming Languages
#Fall 2019 - Program 2 - Python
#Dr. Doug Williams
#Pierce Hopkins

import os
import math
import itertools  
import collections 

#--------------Class-Definitions--------------
class Year:
	def __init__(self, year, yearMaleDict, yearFemaleDict):
		self.year = year
		self.maleDict = yearMaleDict
		self.femaleDict = yearFemaleDict
	
class Decade:
	def __init__(self, year):
		self.year = year
		self.genderDict = dict()
#--------------Class-Definitions--------------


#-----------------File-Read-----------------
def ReadFiles():
	yearArray = []
	years = os.listdir('./data/')
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
		
		
	return yearArray
#-----------------File-Read-----------------


#---------------Parse-Decades---------------
def ParseDecades(yearArray, gender):
	decades = []
	decadesLength = math.ceil(len(yearArray)/10)
	print(gender, "data found for %s decades:"%(decadesLength))
	
	for i in range(decadesLength):
		print("\t The %s's"%(yearArray[i*10].year))
		newDecade = Decade(yearArray[i*10].year)
		decades.append(newDecade)
		for j in range(10):
			if (( i * 10 ) + j) < len(yearArray):
				if gender == "Male":
					newMaleDict = collections.defaultdict(int)
					for key, val in itertools.chain(decades[i].genderDict.items(), yearArray[(( i * 10 ) + j)].maleDict.items()):
						newMaleDict[key] += val
					
					decades[i].genderDict.clear()
					decades[i].genderDict = newMaleDict.copy()
				elif gender == "Female":
					newFemaleDict = collections.defaultdict(int)
					for key, val in itertools.chain(decades[i].genderDict.items(), yearArray[(( i * 10 ) + j)].femaleDict.items()): 
						newFemaleDict[key] += val
						
					decades[i].genderDict.clear()
					decades[i].genderDict = newFemaleDict.copy()
			else:
				break
				
	return decades
#---------------Parse-Decades---------------


#--------------Print-By-Decade--------------
def PrintTopTenNamesByDecade(decades, gender):#@NOTE(P): return array with top10 names
	top10GenderNamesByDecade = []
	
	cnt = 1
	for decade in decades:
		newDecade = Decade(decade.year)
		print("The top 10 most popular ", gender, " names in the %s's"%(decade.year))
		for key,val in sorted(decade.genderDict.items(), key=lambda x: x[1], reverse=True):
			if cnt == 11:
				cnt = 1
				break
			else:
				print("\t", cnt, " ", key, "\t", val)
				newDecade.genderDict[key] = val
				cnt+=1
		top10GenderNamesByDecade.append(newDecade)
	print('\n')
	
	return top10GenderNamesByDecade
#--------------Print-By-Decade--------------


#----------------Name-Rankings---------------
def PrintNameRankings(decades, gender):
	print(gender, " Name Rankings (by Name):")
	print('\t', '\t', end =" ")
	for decade in decades:
		print(decade.year, '\t', end =" ")
	print('\n')
	
	
#----------------Name-Rankings---------------


#-------------------Main--------------------
def main():
	#@NOTE(P): Open the files and read the contents
	yearArray = ReadFiles();
	#NOTE(P): Sort the entries into arrays of Python Dictionaries
	decadesMale = ParseDecades(yearArray, "Male")
	decadesFemale = ParseDecades(yearArray, "Female")
	
	top10MaleNamesByDecade = PrintTopTenNamesByDecade(decadesMale, "Male")
	top10FemaleNamesByDecade = PrintTopTenNamesByDecade(decadesFemale, "Female")
	
	PrintNameRankings(top10MaleNamesByDecade, "Male")
	PrintNameRankings(top10FemaleNamesByDecade, "Female")
#-------------------Main--------------------
if __name__ == '__main__':
	main()