from collections import Counter

def compute_word_importance(fpath1, fpath2):

    counter = dict()
    #First file
    myfile = open(fpath1, "r")
    #Second file
    myfile2 = open(fpath2, "r")
    #List for words in first file
    list1 = list()
    #List for words in second file
    list2 = list()
    #Temporary list to convert from type list to type string
    tmplist = list()
    while True:
        line = myfile.readline()
        if len(line) == 0:
            break
        #Splits the line according to blank space
        word = line.split()
        #Appends the word to tmplist
        tmplist.append(word)
    for i in range(0, len(tmplist)):
        for j in range(0, len(tmplist[i])):
            #Appends the words from tmplist to list1
            list1.append(tmplist[i][j])
    tmplist = list()
    while True:
        line = myfile2.readline()
        if len(line) == 0:
            break
        #Splits the line according to blank space
        word = line.split()
        #Appends the word to tmplist
        tmplist.append(word)
    for i in range(0, len(tmplist)):
        for j in range(0, len(tmplist[i])):
            #Appends the words from tmplist to list2
            list2.append(tmplist[i][j])
    for item in list1:
        if item not in counter:
            #If the word is not in counter it assigns 1 to it
            counter[item] = 1
        else:
            #If the word is in counter it adds one to it
            counter[item] += 1
    for item in list2:
        if item not in counter:
            #If the word is not in counter it assigns -1 to it
            counter[item] = -1
        else:
            #If the word is in counter it subtracts one to it
            counter[item] -= 1

    myfile.close()
    myfile2.close()
    #counter2 is an element of type Counter
    counter2 = Counter(counter)
    return counter2

