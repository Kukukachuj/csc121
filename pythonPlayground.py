names_list =[]
idNumbers_list=[]


def modify(items):
    for i in range(len(items)):
        print(items[i])

def addCus():
    exitCommand = True
 


def main(): 
    names_list =[]
    idNumbers_list=[]

    exitCommand = True

    while exitCommand == True:

        names = input("Enter Custemer name: ")
        names_list += [names]
        idNumbers = input(f"Enter {names} ID number: ")
        idNumbers_list += [idNumbers]
        exitIt = input("continue? adding?")
        if exitIt == "Y":
            exitCommand = True
        else:
            exitCommand = False
    
    
    print("Edit Name(1)  ADD email(2)")
    print("List Names(3) make username(4)")  
    print("Select next option: ")

    menuOption = input()

    if menuOption == "1":
        print (names_list)
        print(idNumbers_list)
        for item in names_list:
            i = item
            for item2 in idNumbers_list:
                b = item2
        print (f"{i + b}")
        

    
    

   
   



if __name__ == "__main__":
    main()