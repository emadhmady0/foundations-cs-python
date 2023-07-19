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

# Function that takes a dictionary and a file name
# This function writes a dictionary to a json file 
# This function transforms a dictionary into a valid json format
# using string manipulation techniques we add the opening and closing curly brakets, 
# we add a new line after each key:value pairs and we add a tab before each key:value pairs

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

# Function that reads from a file and gives the user a list of dictionaries
# we first remove the curly braces using string string slicing
# Then we split the data string into lst by every ",\n"
# Then we replace every ","\t" , and empty spaces with nothing using the replace built-in method
# Then we split every key:value pairs into lst1 by every ":"
# Finally we do a for loop on list1 and assign every key:value pairs to list_of_dictionaries and return the list

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

def main():
    close_program = False
    while(close_program == False):
        printMenu()
        menu_user_input = int(input("Choose an option from the menu above: "))
        match (menu_user_input):
            case 1:
                frst_tuple_strng = input("input first tuple in the following form: x,y,z...: ")
                tuple1_lst = frst_tuple_strng.split(",")
                tuple1 = tuple(tuple1_lst)
                scnd_tuple_strng = input("input second tuple in the following form: x,y,z...:") 
                tuple2_lst = scnd_tuple_strng.split(",")
                tuple2 = tuple(tuple2_lst)
                print("\n" + str(sumTuples(tuple1,tuple2)) + "\n")
            case 2:
                number_of_dict_items_user_input = int(input("how many key:value pairs do you want to add to the Json File? "))
                dict_list = []
                for i in range(number_of_dict_items_user_input):
                    dict_user_input = input("Input a dictionary item in the following form (key:value): ")
                    dict_list.append(dict_user_input.split(":"))
                dict1 = transformListToDictionary(dict_list)
                exportJson(dict1,"assignment_03_Emad_Hmady/text.json")
                print("\n" + "Data added to file successfully" + "\n")
            case 3:
                folder = "assignment_03_Emad_Hmady/"
                file_name_user_input = input("Enter the name of the Json file: ")
                directory = folder+file_name_user_input
                print(importJson(directory))
            case 4:
                close_program = True
            
main()


############
# Exercise #
############

# a. 1/6N+8000N^3+24 = O(N^3) Cubic
# b. 1/6N^3 = O(N^3) Cubic
# c. 1/6N! +200N^4 = O(N!) Factorial
# d. NlogN +1000 = O(NLogN) N*Logarithmic
# e. logN +N = O(N) Linear
# f. 1⁄2N(N-1) = O(N^2) Quadratic
# g. N^2+220NlogN^2+3N+9000 = O(N^2) Quadratic
# h. N!+3^N+2^N+N^3+N^2 = O(N!) Factorial