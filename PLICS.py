import os
file_path = os.path.realpath(__file__)
script_dir = os.path.abspath( os.path.dirname( __file__ ) )
broken = False
helpbroken = False
newrepolbroken = False
newrepol = "newRePol is the command that allows you to calculate the properties of any given regular poligons, and thus is the most important command in the entire program! just follow the give instructions!"
n = 0
d = 0
e = 0
i = 0
s = 0
les = 0
ver = "Version PLICSv0.0.0-Alpha2.0.3-1"
log = ["realease ver, nothing to see.","Ver PLICSv0.0.0-alpha2: Added notes, credits and readme commands, fixed minor problems with the newRePol command, added descriptions to the help command.", "Ver PLICSv0.0.0-Alpha2.0.3: FINALLY added the GNU General Public License, commands to display it as well as its warranty, and a better way to display the readme. There is still a lot to do, the main commands is still with lots of errors and the help command is still far from complete.", "Ver PLICSv0.0.0-Alpha2.0.3-1: I FORGOT TO ADD THE LICENSE TO THE RIGHT FOLDER BRUH"]
polygon = ["triangle", "square", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon"]
commands = ["help", "newPol", "exit", "newRePol", "notes", "credits", "readme", "license", "warranty"]
for lis in range(0,40):
    print("")
print("Hey there! This is the Polygon Information Calculation System (PLICS)!")
print(ver)
print("    PLICS  Copyright (C) 2022 ThaNook")
print("    This program comes with ABSOLUTELY NO WARRANTY; for details type 'warranty'.")
print("    This is free software, and you are welcome to redistribute it")
print("    under certain conditions; for more information,")
print("    read the license provided with this code, by using the 'license' command")
print("    or reading the 'License_gpl-3.0.txt' file in the same folder as this script.")
print("  Comands: help, notes, exit, newRePol, readme... ")
while broken == False :
    print("Hey! this is PLICS!")
    com = str(input("> "))
    print(com)
    if(com == "help"):
        while helpbroken == False:   
            print("About what command do you want to know about? (use 'ls' for lists and 'quit' to leave)")
            com = input("[help]> ")
            if(com == "help"):
                print("you really dont know what the help command does?")
            elif(com == "notes"):
                print("shows update notes for this update and all previous. I will be posting it somewhere else too at somepoint")
            elif(com == "credits"):
                print("prints everyone that has worked on this stupid little project with me!")
            elif(com == "newRePol"):
                print(newrepol)
            elif(com == newrepol):
                print("you copypasted the entire thing why")
            elif(com == "readme"):
                print("why dont you run the command and read it?")
            elif(com == "newPol"):
                print("the comand that is not done yet!")
            elif(com == "quit"):
                helpbroken = True
            elif(com == "ls"):
                print("All commands avalable:")
                print(commands)
            else:
                print("what?")  
    elif(com == "notes"):
        print("These are the notes for the updates so far:") 
        for les in range(0,len(log)):
            print(log[les])
            print("")
        else:
            les=0
    elif(com == "readme"):
        print(" ")
        with open(script_dir +"/texts/readmedaddy") as README:
            print(README.read())
    elif(com == "warranty"):
        print(" ")
        with open(script_dir +"/texts/warranty.txt") as WARRANTY:
            print(" ")
            print(WARRANTY.read())
    elif(com == "credits"):
        print("me (tanuki, @malditotanuki on twitter), the user nikhilkumarsingh on github for the TextFormatter script. ")
    elif(com == "license"):
        print(" ")
        with open(script_dir + "/texts/License_gpl-3.0.txt") as GPL:
            print(GPL.read())
    elif(com == "newRePol"):
        while newrepolbroken == False:
            print("What do you know about the regular poligon?")
            print("Number of sides = n, Number of diagonals = d, Exterior angles = e, Interior angles = i, All intenal angles added = s")
            print("(and 'quit' to exit :) )")
            temp = input("[newRePol]> ")
            if(temp == "quit"):
                newrepolbroken = True
            elif temp == "n" or temp == "e" or temp == "i" or temp == "s" or temp == "d":
                print("and whats that?")
                num1 = input("[newRePol](insert number)> ")
                if type(num1) == int or float:
                    num = int(num1)
                else:
                    num = 0
                print("hang on...")
                if(temp == "n"):
                    print(temp)
                    n = num
                    e =  360 /n 
                    i = 180 - 360 / n
                    d = n - 3
                    s = i * n
                elif(temp == "d"):
                    print(temp)
                    d = num
                    n = d + 3
                    e =   360/ n
                    i = 180 - 360 / n
                    s = i * n
                elif(temp == "e"):
                    e = num
                    print(temp)
                    n = e/360
                    i = 180 - 360 / n
                    s = i * n
                    d = n - 3
                elif(temp == "i"):
                    i =  num
                    n= 180 - 360 / i
                    s = i * n
                    d = n - 3
                    e =   360/n
                    print(temp)
                elif(temp == "s"):
                    s = num
                    n  = s + 360 /180
                    d = n - 3
                    e =   360/n
                    i = 180 - 360 / n
                    print(temp)       
                else:
                    print(temp)
                    print("heh")
                print("Thats a:")
                nd = str(n)
                dd = str(d)
                id = str(i)
                ed = str(e)
                sd = str(s)
                if type(n) == int and n <= len(polygon):
                    print(polygon[n-3])
                else:
                    print("i dont fucking know")
                print("with " +nd+ " sides," +dd+ " diagonals, each on of its internal angles is " +id+ " degres,")
                print("each one of its external angles is " +ed+ " degres and the sum of all internal angles is " +sd)
                print(" ")            
            else:
                print("huh")
        else:
            print(" ")
            newrepolbroken = False
    elif(com == "exit"):
        print("thanks for using PLICS!")
        broken = True
    else:
        print("Uknown command! try again!")
