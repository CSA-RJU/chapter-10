 #Riley
#1/24/18
#Comp Prog

namelist = ["Michael", "Carl", "Natalie", "Riley", "Cameron"]

def names(namelist):
    add1 = input ("Type a name.|").title()
    namelist.append(add1)
    print (namelist)
    x = names2(namelist)
    return(x)

def names2(namelist):
    choice = input ("Would you like to add another name? (y/n)|")
    if choice == "yes" or choice == "y":
        add2 = input ("|").title()
        namelist.append(add2)
        names2(namelist)
    elif choice == "no" or choice == "n":
        #print (namelist)
        pass
    else:
        print ("Not a valid input!")
        names2(namelist)
    return namelist

print(names(namelist))
