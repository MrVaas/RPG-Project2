def getusername():
    name = ""
    while name=="":
        name=input("Votre Nom ? ")
    return name

Username=getusername()
print("Votre nom est : " + str(Username))