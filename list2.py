 #Riley
#1/22/18
#Comp Prog

def confidential():
    global x
    global list_con
    list_con = ["Riley", "25", "4", "2003", "Austin"]
    for x in list_con:
        print (x)
    printing1()
    printing2()

def printing1():
    global x
    global list_con
    print ("I was born in", x) 

def printing2():
    global x
    print ("The month was", list_con[2])
    print ("Jolene") 
    for x in list_con:
        print (x)

confidential()
