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

def exportJson(dict,filename):
    f = open(filename,"w")
    json_text = "{\n"
    for key,value in dict.items():
        json_text+=  ("\t"+'"'+ key+'"'+":"+'"'+value+'"'+",\n")
    json_text = json_text[:len(json_text)-2] + "\n}"
    f.write(json_text)
    f.close()

def transformListToDictionary(lst):
    dicty = {}
    for i in lst:
        dicty[i[0]] = i[1]
    return dicty

def importJson(filename):
    f = open(filename,"r")
    file_data = f.read()
    strng = file_data[3:len(file_data)-2]
    lst = strng.split(",\n")
    lst1=[]
    lst_of_dictionaries = []
    for i in lst:
        str1 = i.replace("\t","")
        str2 = str1.replace('"',"")
        str3 = str2.replace(" ", "")
        lst1.append(str3.split(":"))
    for i in lst1:
        dic = {}
        dic[i[0]] = i[1]
        lst_of_dictionaries.append(dic)
    return lst_of_dictionaries