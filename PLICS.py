broken = False
helpbroken = False
newrepolbroken = False
n = 0
d = 0
e = 0
i = 0
s = 0
ver = "Version B.0.1"
polygon = ["triangle", "square", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon"]
commands = ["help", "newPol", "exit", "newRePol"]
print("Hey there! This is the Polygon Information Calculation System (PLICS)!")
print(ver)
print("Comands: help, newPol, exit, newRePol... ")

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
            elif(com == "quit"):
                helpbroken = True
            elif(com == "ls"):
                print("All commands avalable:")
                print(commands)
            else:
                print("what?")        
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
    elif(com == "exit"):
        print("thanks for using PLICS!")
        broken = True
    else:
        print("Uknown command! try again!")
