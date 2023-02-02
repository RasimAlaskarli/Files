def load_library(filename):
    #Reads the file
    myfile = open(filename, "r")
    #Dictionary for books
    elementlist = dict()
    while True:
        line = myfile.readline()
        if len(line) == 0:
            break
        #Splits the string according to the symbol '|'
        key, value = line.split("|")
        #Adds the book name as key and author as value
        elementlist[key] = str(value.strip())
    myfile.close()
    return elementlist

def index_by_author(dictionary):
    #Dictionary that we will return
    newdict = dict()

    for key in dict(dictionary):
        if key not in newdict:
            #Creates a list for every value of newdict
            newdict[dictionary[key]] = list()

    for key in dict(dictionary):
        for item in newdict:
            #If the key exists in newdict it appends as a value to said key
            if dictionary[key] == item:
                newdict[item].append(key)
    return newdict

def report_author_counts(lib_fpath, rep_filepath):
    myfile = open(lib_fpath, "r")
    #Dicitionary with book names as keys and authors as values
    elementlist = dict()
    #Dictionary with authors as keys and the number of books they have written as values
    newdict = dict()
    #The line that the program is on
    linenum=0
    while True:

        line = myfile.readline()
        if len(line) == 0:
            #If the file is empty, TOTAL BOOK: 0
            if linenum == 0:
                newdict["TOTAL BOOKS"] = 0
            break
        linenum += 1
        #Splits the string according to the symbol '|'
        key,value = line.split("|")
        #Gets rid of \n at the end of the string
        elementlist[str(key).replace("\n","")] = str(value).replace("\n", "")

    for item in elementlist:
        i = 0
        for item2 in elementlist:
            #If the author is the same then increase the number of books(i)
            if elementlist[item] == elementlist[item2]:
                i += 1

        #The value of dictionary is equal to i
        newdict[elementlist[item]] = i
        #The number of total books is the length of dictionary
        newdict["TOTAL BOOKS"] = len(elementlist)

    with open(rep_filepath, 'w') as f:
        #Write everything to file
        for item in newdict:
            f.write(item)
            f.write(": ")
            f.write(str(newdict[item]))
            #If it is not the last item then add \n else do not add it
            if item != list(newdict)[-1]:
                f.write("\n")
    f.close()
    myfile.close()







