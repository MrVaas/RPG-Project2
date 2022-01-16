def getusername():
    name = ""
    while name=="":
        name=input("Votre Nom ? ")
    return name

def getuserrace():
    global UserMana
    global UserForce
    global UserVie
    race = ""
    while race not in ("Orc","Humain","Elf","Centaure","Demon"):
        race = input("Votre Race ? ")
        if race == "Orc":
            UserMana = UserMana + 50
            UserForce = UserForce + 200
            UserVie = UserVie + 150
        elif race == "Humain":
            UserMana = UserMana + 133
            UserForce = UserForce + 133
            UserVie = UserVie + 134
        elif race == "Elf":
            UserMana = UserMana + 200
            UserForce = UserForce + 50
            UserVie = UserVie + 150
        elif race == "Centaure":
            UserMana = UserMana + 100
            UserForce = UserForce + 150
            UserVie = UserVie + 150
        elif race == "Demon":
            UserMana = UserMana + 150
            UserForce = UserForce + 150
            UserVie = UserVie + 200
        else:
            print("Races non valide !")
            print("Races Valides")
            print("Orc - Humain - Elf - Centaure - Demon")
    return race


UserMana = 0
UserForce = 0
UserVie = 0
UserPrecision = 0
UserName=getusername()
UserRace=getuserrace()

print(str(UserName)+ " Est un " + str(UserRace))
print("Vous avez "+ str(UserVie)+" HP")
print("Vous avez "+ str(UserMana)+" MP")
print("Vous avez "+ str(UserForce)+" de Force")