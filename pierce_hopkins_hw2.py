"""
CSCI 3415 - Principles of Programming Languages
Fall 2019 - Program 2 - Python
Dr. Doug Williams
Pierce Hopkins
"""

import os
import math
import itertools
import collections

class Year:
    """
    This class is used to store the data from year text files
    """
    def __init__(self, year, male_dict, female_dict):
        self.year = year
        self.male_dict = male_dict
        self.female_dict = female_dict

    def print_year(self):
        """
        Prints year
        """
        print(self.year)


    def print_dict(self):
        """
        Prints dicts
        """
        print(self.male_dict, self.female_dict)

class Decade:
    """
    This class is used to store the data in a way that is convenient
    for our purposes of manipulation.
    """
    def __init__(self, year):
        self.year = year
        self.gender_dict = dict()

    def print_year(self):
        """
        Prints year
        """
        print(self.year)
    def print_dict(self):
        """
        Prints dicts
        """
        print(self.gender_dict)
#-------------End-Class-Definitions--------------



def read_files():
    """
    Reads in year files and creates array of objects
    Parameters:
    arg1 (): n/a
    Returns:
    Year[] year_array: array of all data from year files
    """
    year_array = []
    years = os.listdir('./data/')
    for year in years:

        year_male_dict = {}
        year_female_dict = {}

        print("Attempting to read: " + year)
        file = open("./data/" + year, "r")
        file_lines = file.readlines()

        for line in file_lines:
            line_split = line.split(',')
            line_split[2] = line_split[2].replace("\n", "")

            if line_split[1] == "M":
                year_male_dict[line_split[0]] = int(line_split[2])
            elif line_split[1] == "F":
                year_female_dict[line_split[0]] = int(line_split[2])

        new_year = Year(year.strip("yob.txt"), year_male_dict, year_female_dict)
        year_array.append(new_year)


    return year_array
#----------------End-File-Read-----------------



def parse_decades(year_array, gender):
    """
    Takes year data and parses into decades
    Parameters:
    arg1 (year_array): array of year data
    arg2 (gender): string that denotes which gender to parse data for
    Returns:
    Decade[] decades: fully parsed year data
    """
    decades = []
    decades_length = math.ceil(len(year_array)/10)
    print(gender, "data found for %s decades:"%(decades_length))

    for i in range(decades_length):
        print("\t The %s's"%(year_array[i*10].year))
        new_decade = Decade(year_array[i*10].year)
        decades.append(new_decade)
        for j in range(10):
            if ((i*10)+j) < len(year_array):
                if gender == "Male":
                    new_male_dict = collections.defaultdict(int)

                    #@NOTE(P): Pylint complained about the line
                    #with the key,val for loop being too long
                    tmp_gd = decades[i].gender_dict.items()
                    tmp_md = year_array[((i*10)+j)].male_dict.items()

                    for key, val in itertools.chain(tmp_gd, tmp_md):
                        new_male_dict[key] += val

                    decades[i].gender_dict.clear()
                    decades[i].gender_dict = new_male_dict.copy()
                elif gender == "Female":
                    new_female_dict = collections.defaultdict(int)

                    #@NOTE(P): Pylint complained about the line
                    #with the key,val for loop being too long
                    tmp_gd = decades[i].gender_dict.items()
                    tmp_fd = year_array[((i*10)+j)].female_dict.items()

                    for key, val in itertools.chain(tmp_gd, tmp_fd):
                        new_female_dict[key] += val

                    decades[i].gender_dict.clear()
                    decades[i].gender_dict = new_female_dict.copy()
            else:
                break

    return decades
#--------------End-Parse-Decades---------------




def print_top_ten_names_by_decade(decades, gender):
    """
    Sorts, prints and returns an array of top 10 most popular names by decade
    Parameters:
    arg1 (decades): array of decade data
    arg2 (gender): string that denotes which gender to parse data for
    Returns:
    Decade[] top_10_gender_names_by_decade: the top 10 names by decade
    """
    top_10_gender_names_by_decade = []

    cnt = 1
    for decade in decades:
        new_decade = Decade(decade.year)
        print("The top 10 most popular", gender, "names in the %s's"%(decade.year))
        for key, val in sorted(decade.gender_dict.items(), key=lambda x: x[1], reverse=True):
            if cnt != 11:
                print("\t", cnt, " ", key, "\t", val)
                new_decade.gender_dict[key] = val
                cnt += 1
            else:
                cnt = 1
                break
        top_10_gender_names_by_decade.append(new_decade)
        print('\n')
    print('\n')

    return top_10_gender_names_by_decade
#-------------End-Print-By-Decade--------------




def alphebetize_names(decades):
    """
    alphabetizes names for the purposes of printing
    Parameters:
    arg1 (decades): array of decade data
    Returns:
    string[] alphabetized_name_list: list of alphabetized names
    """
    alphabetizedname_list = []
    for decade in decades:
        for name in decade.gender_dict:
            if name not in alphabetizedname_list:
                alphabetizedname_list.append(name)
    alphabetizedname_list.sort()
    return alphabetizedname_list
#-----------End-Alphabetize-Names--------------



def print_name_rankings(decades, gender):
    """
    Prints names and their rank by decade
    Parameters:
    arg1 (decades): array of decade data
    arg2 (gender): string that denotes which gender to parse data for
    Returns:
    n/a
    """
    print(gender, " Name Rankings (by Name):")
    print('\t', '\t', end=" ")
    for decade in decades:
        print(decade.year, '\t', end=" ")
    print('\n', end='')

    name_list = alphebetize_names(decades)
    for name in name_list:
        print(name, end="\t")
        if len(name) < 8:
            print('\t', end='')

        for decade in decades:
            if name in decade.gender_dict:
                temp = sorted(decade.gender_dict.items(), key=lambda x: x[1], reverse=True)
                sorted_name_list = list()
                for temp_name in temp:
                    sorted_name_list.append(temp_name[0])
                index = sorted_name_list.index(name)
                print(' ', index+1, '\t', end='')
            else:
                print(' ', '-', '\t', end='')
        print('', end='\n')
    print('\n')
#---------------End-Name-Rankings---------------



def main():
    """
    main function
    Parameters:
    n/a
    Returns:
    n/a
    """
    #@NOTE(P): Open the files and read the contents
    year_array = read_files()
    #NOTE(P): Sorts the entries into arrays of Python Dictionaries
    decades_male = parse_decades(year_array, "Male")
    decades_female = parse_decades(year_array, "Female")

    top_10_male_names_by_decade = print_top_ten_names_by_decade(decades_male, "Male")
    top_10_female_names_by_decade = print_top_ten_names_by_decade(decades_female, "Female")

    print_name_rankings(top_10_male_names_by_decade, "Male")
    print_name_rankings(top_10_female_names_by_decade, "Female")
#------------------End-Main--------------------
if __name__ == '__main__':
    main()
