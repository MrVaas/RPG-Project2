import time
from items import *
from enemies import *
from room import *

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
        print("Un Centaure ? Vraiment ? C'est toi qui voit.")
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

def getuserarmor():
    global UserRace
    global UserClasse
    armure=""
    if UserRace == "Orc":
        if UserClasse == "Chasseur":
            armure = Armure_cuir_T1
        elif UserClasse == "Chaman":
            armure = Armure_tissu_T1
        elif UserClasse == "Guerrier":
            armure = Armure_fer_T1
        elif UserClasse == "Berserk":
            print("Le Berserk n'a aucune armure.")
            print("Bon courrage")
    elif UserRace == "Humain":
        if UserClasse == "Archer":
            armure = Armure_cuir_T1
        elif UserClasse == "Moine":
            armure = Armure_tissu_T1
        elif UserClasse == "Voleur":
            armure = Armure_cuir_T1
        elif UserClasse == "Barde":
            armure = Armure_cuir_T1
    elif UserRace == "Elf":
        if UserClasse in ("Elementaliste", "Sentinelle", "Gardien des runes"):
            armure = Armure_tissu_T1
        elif UserClasse == "Rodeur":
            armure = Armure_cuir_T1
    elif UserRace == "Centaure":
        armure = Armure_fer_T1
    elif UserRace == "Demon":
        armure = Armure_arcane_T1

    return armure

def getuserstuff():
    global UserArmor
    global UserArmorName
    global UserMana
    global UserForce

    if UserArmorName == Armure_cuir_T1:
        UserArmor = UserArmor + 10
    elif UserArmorName == Armure_tissu_T1:
        UserArmor = UserArmor + 5
        UserMana = UserMana + 10
    elif UserArmorName == Armure_fer_T1:
        UserArmor = UserArmor + 25
    elif UserArmorName == Armure_arcane_T1:
        UserMana = UserMana + 20
        UserArmor = UserArmor + 20
        UserForce = UserForce + 10

def getCombatsDegats(Attaker, Armor, Atk, VictimHP, VictimName):

    VictimHP = (VictimHP + Armor) - Atk
    dmg = Atk - Armor
    print(str(Attaker)+ " a attaquer "+ str(VictimName))
    time.sleep(1)
    print(str(Attaker)+ " a fait "+ str(dmg)+ " degats")


def getStartPoint():
    global UserName
    global UserMoney
    from room import room_spawn

    print(str(UserName)+" vous vennez de rentrer dans l'échoppe du Marchand !")
    room = room_spawn

    return room

def showShopItem(categorie):
    global Arme_Baton_T1
    global Arme_Arc_T1
    global UserMoney
    global UserEquipedWeapon

    if categorie == "Armes":
        print("Stock du marchand: ")
        print(Arme_Arc_T1 + " (40 Gold)")
        print(Arme_Baton_T1+ " (10 Gold)")
        time.sleep(1.5)
        print("Voulez vous achetez un de ces objets ?")
        reply=""
        while reply not in ("Oui","Non"):
            reply=input("Oui / Non: ")
            if reply == "Oui":
                print("1: "+ Arme_Arc_T1)
                print("2: "+ Arme_Baton_T1)
                choice=""
                while choice not in ("1","2"):
                    choice=input("1 / 2: ")
                    if choice== "1":
                        UserMoney = UserMoney - 40
                        if UserMoney < 0:
                            print ("vous ne pouvez pas faire ça")
                            UserMoney = UserMoney + 40
                        else:
                            print("Vous vennez d'acheter :"+ Arme_Arc_T1)
                            UserEquipedWeapon = Arme_Arc_T1
                            time.sleep(1)
                            print(Arme_Arc_T1+" a été equipé")
                    elif choice=="2":
                        UserMoney = UserMoney - 10
                        if UserMoney < 0:
                            print ("vous ne pouvez pas faire ça")
                            UserMoney = UserMoney + 10
                        else:
                            print("Vous vennez d'acheter :"+ Arme_Baton_T1)
                            UserEquipedWeapon = Arme_Baton_T1
                            time.sleep(1)
                            print(Arme_Baton_T1+" a été equipé")
                    else:
                        print("Reponse invalide")
            elif reply == "Non":
                time.sleep(1)
                print("Redirection au choix de catégories")
                CreateRoom(room_spawn,0)
            else:
                print("Reponse invalide")
    elif categorie == "Armures":
        print("Le marchand n'a rien pour le moment.")

def CreateRoom(room, state):
    if room == room_spawn:
        state = 0
        time.sleep(1)
        print("Armures - Armes")
        ItemBuy=""
        while ItemBuy not in ("Armes","Armures"):
            ItemBuy = input("Quel est votre choix: ")
            if ItemBuy == "Armes":
                showShopItem(ItemBuy)
            elif ItemBuy == "Armures":
                showShopItem(ItemBuy)
            else:
                print("Choix invalide")

### GAME CODE ###

UserMana = 0
UserForce = 0
UserVie = 0
UserPrecision = 0
UserArmor = 0
UserMoney = 300
UserState = 0
UserEquipedWeapon = ""
UserEquipedArmor = ""
UserName=getusername()
UserRace=getuserrace()
UserClasse=getuserclasse()
time.sleep(1)

print(str(UserName)+ " Est un "+str(UserClasse)+ " " + str(UserRace))
time.sleep(1)
print("Vous avez "+ str(UserVie)+" HP")
time.sleep(1)
print("Vous avez "+ str(UserMana)+" MP")
time.sleep(1)
print("Vous avez "+ str(UserForce)+" de Force")
time.sleep(1)
print("Vous avez "+ str(UserMoney)+ " Gold en poche")
time.sleep(1.5)
UserRoom=getStartPoint()
time.sleep(1.5)
CreateRoom(room_spawn,UserState)




