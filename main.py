import time
from Items import *

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
            print("Races Valides :")
            print("Orc - Humain - Elf - Centaure - Demon")
    return race

def getuserclasse():
    global UserRace
    global UserMana
    global UserForce
    global UserVie
    global UserPrecision
    classe = ""

    if UserRace == "Orc":
        print("Un orc, tres bien. Quel serra votre Classe ?")
        while classe not in ("Chasseur", "Chaman", "Guerrier", "Berserk"):
            classe = input("Votre Classe : ")
            if classe == "Chasseur":
                UserForce = UserForce + 100
                UserPrecision = UserPrecision + 150
            elif classe == "Chaman":
                UserMana = UserMana + 150
                UserForce = UserForce + 50
                UserPrecision = UserPrecision + 50
            elif classe == "Guerrier":
                UserForce = UserForce + 150
                UserPrecision = UserPrecision + 100
            elif classe == "Berserk":
                UserMana = UserMana + 50
                UserForce = UserForce + 150
                UserPrecision = UserPrecision + 50
            else:
                print("Classe non valide")
                print("Classe valide :")
                print("Chasseur - Chaman - Guerrier - Berserk")

    elif UserRace == "Humain":
        print("Un humain, classique. Quel sera votre Classe ?")
        while classe not in ("Archer", "Moine", "Voleur", "Barde"):
            classe = input("Votre classe : ")
            if classe == "Archer":
                UserForce = UserForce + 50
                UserPrecision = UserPrecision + 200
            elif classe == "Moine":
                UserMana = UserMana + 200
                UserPrecision = UserPrecision + 50
            elif classe == "Voleur":
                UserMana = UserMana + 5
                UserForce = UserForce + 95
                UserPrecision = UserPrecision + 150
            elif classe == "Barde":
                UserMana = UserMana + 150
                UserForce = UserForce + 25
                UserPrecision = UserPrecision + 75
            else:
                print("Classe non valide")
                print("Classe valide :")
                print("Archer - Moine - Voleur - Barde")

    elif UserRace == "Elf":
        print("Un elf. Vous serrez un amis des éléments. Quel sera votre classe ?")
        while classe not in ("Rodeur", "Elementaliste", "Sentinelle", "Gardien des runes"):
            classe = input("Votre classe : ")
            if classe == "Rodeur":
                UserMana = UserMana + 45
                UserForce = UserForce + 5
                UserPrecision = UserPrecision + 200
            elif classe == "Elementaliste":
                UserMana = UserMana + 150
                UserForce = UserForce + 5
                UserPrecision = UserPrecision + 95
            elif classe == "Sentinelle":
                UserMana = UserMana + 90
                UserForce = UserForce + 35
                UserPrecision = UserPrecision + 125
            elif classe == "Gardien des runes":
                UserMana = UserMana + 200
                UserForce = UserForce + 5
                UserPrecision = UserPrecision + 45
            else:
                print("Classe non valide")
                print("Classe valide :")
                print("Rodeur - Elementaliste - Sentinelle - Gardien des runes")
    elif UserRace == "Centaure":
        print("Un Centaure ? Vraiment ? C'est toi voit.")
        while classe not in ("Archer", "Sorcier","Dueliste","Lancier"):
            classe = input("Votre classe :")
            if classe == "Archer":
                UserForce = UserForce + 100
                UserPrecision = UserPrecision + 150
            elif classe == "Sorcier":
                UserForce = UserForce + 150
                UserMana = UserMana + 25
                UserPrecision = UserPrecision + 75
            elif classe == "Dueliste":
                UserForce = UserForce + 150
                UserPrecision = UserPrecision + 100
            elif classe == "Lancier":
                UserMana = UserMana + 60
                UserForce = UserForce + 90
                UserPrecision = UserPrecision + 100
            else:
                print("Classe non valide")
                print("Classe valide :")
                print("Archer - Sorcier - Dueliste - Lancier")
    elif UserRace == "Demon":
        print("Oh, je vois... Un Demon. Dark Sasuke")
        while classe not in ("Necromancien", "Arcaniste", "Revenant", "Maitre du savoir"):
            classe = input("Votre classe :")
            if classe == "Necromancien":
                UserMana = UserMana + 90
                UserForce = UserForce + 35
                UserPrecision = UserPrecision + 125
            elif classe == "Arcaniste":
                UserMana = UserMana + 150
                UserForce = UserForce + 25
                UserPrecision = UserPrecision + 75
            elif classe == "Revenant":
                UserForce = UserForce + 150
                UserPrecision = UserPrecision + 100
            elif classe == "Maitre du savoir":
                UserMana = UserMana + 100
                UserForce = UserForce + 90
                UserPrecision = UserPrecision + 60
            else:
                print("Classe non valide")
                print("Classe valide")
                print("Necromancien - Arcaniste - Revenant - Maitre du savoir")
    return classe


UserMana = 0
UserForce = 0
UserVie = 0
UserPrecision = 0
UserName=getusername()
UserRace=getuserrace()
UserClasse=getuserclasse()
UserArmor=checkarmor()

time.sleep(2)
print(str(UserName)+ " Est un "+str(UserClasse)+ " " + str(UserRace))
print("Vous avez "+ str(UserVie)+" HP")
print("Vous avez "+ str(UserMana)+" MP")
print("Vous avez "+ str(UserForce)+" de Force")