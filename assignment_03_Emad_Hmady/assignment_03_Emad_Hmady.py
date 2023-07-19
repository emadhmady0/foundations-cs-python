def printMenu():
    print("1. Sum Tuples\n" +
          "2. Export JSON\n" +
          "3. Import JSON\n" +
          "4. Exit\n" +
          "- - - - - - - - - - - - - - -\n")

def sumTuples(tpl1,tpl2):
    lst = []
    for i in range(len(tpl1)):
        lst.append(int(tpl1[i])+int(tpl2[i]))
    tpl3 = tuple(lst)
    return tpl3