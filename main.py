import time
import arcade
import threading
import random
from items import *
from enemies import *
from room import *
from perks import *

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
    while race not in ("Orc".casefold(),"Humain".casefold(),"Elf".casefold(),"Centaure".casefold(),"Demon".casefold()):
        race = input("Votre Race ? ").casefold()
        if race == "Orc".casefold():
            UserMana = UserMana + 50
            UserForce = UserForce + 200
            UserVie = UserVie + 150
        elif race == "Humain".casefold():
            UserMana = UserMana + 133
            UserForce = UserForce + 133
            UserVie = UserVie + 134
        elif race == "Elf".casefold():
            UserMana = UserMana + 200
            UserForce = UserForce + 50
            UserVie = UserVie + 150
        elif race == "Centaure".casefold():
            UserMana = UserMana + 100
            UserForce = UserForce + 150
            UserVie = UserVie + 150
        elif race == "Demon".casefold():
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

    if UserRace == "Orc".casefold():
        print("Un orc, tres bien. Quel serra votre Classe ?")
        while classe not in ("Chasseur".casefold(), "Chaman".casefold(), "Guerrier".casefold(), "Berserk".casefold()):
            classe = input("Votre Classe : ").casefold()
            if classe == "Chasseur".casefold():
                UserForce = UserForce + 100
                UserPrecision = UserPrecision + 150
            elif classe == "Chaman".casefold():
                UserMana = UserMana + 150
                UserForce = UserForce + 50
                UserPrecision = UserPrecision + 50
            elif classe == "Guerrier".casefold():
                UserForce = UserForce + 150
                UserPrecision = UserPrecision + 100
            elif classe == "Berserk".casefold():
                UserMana = UserMana + 50
                UserForce = UserForce + 150
                UserPrecision = UserPrecision + 50
            else:
                print("Classe non valide")
                print("Classe valide :")
                print("Chasseur - Chaman - Guerrier - Berserk")

    elif UserRace == "Humain".casefold():
        print("Un humain, classique. Quel sera votre Classe ?")
        while classe not in ("Archer".casefold(), "Moine".casefold(), "Voleur".casefold(), "Barde".casefold()):
            classe = input("Votre classe : ").casefold()
            if classe == "Archer".casefold():
                UserForce = UserForce + 50
                UserPrecision = UserPrecision + 200
            elif classe == "Moine".casefold():
                UserMana = UserMana + 200
                UserPrecision = UserPrecision + 50
            elif classe == "Voleur".casefold():
                UserMana = UserMana + 5
                UserForce = UserForce + 95
                UserPrecision = UserPrecision + 150
            elif classe == "Barde".casefold():
                UserMana = UserMana + 150
                UserForce = UserForce + 25
                UserPrecision = UserPrecision + 75
            else:
                print("Classe non valide")
                print("Classe valide :")
                print("Archer - Moine - Voleur - Barde")

    elif UserRace == "Elf".casefold():
        print("Un elf. Vous serrez un amis des éléments. Quel sera votre classe ?")
        while classe not in ("Rodeur".casefold(), "Elementaliste".casefold(), "Sentinelle".casefold(), "Gardien des runes".casefold()):
            classe = input("Votre classe : ").casefold()
            if classe == "Rodeur".casefold():
                UserMana = UserMana + 45
                UserForce = UserForce + 5
                UserPrecision = UserPrecision + 200
            elif classe == "Elementaliste".casefold():
                UserMana = UserMana + 150
                UserForce = UserForce + 5
                UserPrecision = UserPrecision + 95
            elif classe == "Sentinelle".casefold():
                UserMana = UserMana + 90
                UserForce = UserForce + 35
                UserPrecision = UserPrecision + 125
            elif classe == "Gardien des runes".casefold():
                UserMana = UserMana + 200
                UserForce = UserForce + 5
                UserPrecision = UserPrecision + 45
            else:
                print("Classe non valide")
                print("Classe valide :")
                print("Rodeur - Elementaliste - Sentinelle - Gardien des runes")
    elif UserRace == "Centaure".casefold():
        print("Un Centaure ? Vraiment ? C'est toi qui voit.")
        while classe not in ("Archer".casefold(), "Sorcier".casefold(),"Dueliste".casefold(),"Lancier".casefold()):
            classe = input("Votre classe :").casefold()
            if classe == "Archer".casefold():
                UserForce = UserForce + 100
                UserPrecision = UserPrecision + 150
            elif classe == "Sorcier".casefold():
                UserForce = UserForce + 150
                UserMana = UserMana + 25
                UserPrecision = UserPrecision + 75
            elif classe == "Dueliste".casefold():
                UserForce = UserForce + 150
                UserPrecision = UserPrecision + 100
            elif classe == "Lancier".casefold():
                UserMana = UserMana + 60
                UserForce = UserForce + 90
                UserPrecision = UserPrecision + 100
            else:
                print("Classe non valide")
                print("Classe valide :")
                print("Archer - Sorcier - Dueliste - Lancier")
    elif UserRace == "Demon".casefold():
        print("Oh, je vois... Un Demon. Dark Sasuke")
        while classe not in ("Necromancien".casefold(), "Arcaniste".casefold(), "Revenant".casefold(), "Maitre du savoir".casefold()):
            classe = input("Votre classe :").casefold()
            if classe == "Necromancien".casefold():
                UserMana = UserMana + 90
                UserForce = UserForce + 35
                UserPrecision = UserPrecision + 125
            elif classe == "Arcaniste".casefold():
                UserMana = UserMana + 150
                UserForce = UserForce + 25
                UserPrecision = UserPrecision + 75
            elif classe == "Revenant".casefold():
                UserForce = UserForce + 150
                UserPrecision = UserPrecision + 100
            elif classe == "Maitre du savoir".casefold():
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
    if UserRace == "Orc".casefold():
        UserRace = "Orc"
        if UserClasse == "Chasseur".casefold():
            armure = Armure_cuir_T1
        elif UserClasse == "Chaman".casefold():
            armure = Armure_tissu_T1
        elif UserClasse == "Guerrier".casefold():
            armure = Armure_fer_T1
        elif UserClasse == "Berserk".casefold():
            print("Le Berserk n'a aucune armure.")
            print("Bon courrage")
    elif UserRace == "Humain".casefold():
        UserRace = "Humain"
        if UserClasse == "Archer":
            armure = Armure_cuir_T1
        elif UserClasse == "Moine".casefold():
            armure = Armure_tissu_T1
        elif UserClasse == "Voleur".casefold():
            armure = Armure_cuir_T1
        elif UserClasse == "Barde".casefold():
            armure = Armure_cuir_T1
    elif UserRace == "Elf".casefold():
        UserRace = "Elf"
        if UserClasse in ("Elementaliste".casefold(), "Sentinelle".casefold(), "Gardien des runes".casefold()):
            armure = Armure_tissu_T1
        elif UserClasse == "Rodeur".casefold():
            armure = Armure_cuir_T1
    elif UserRace == "Centaure".casefold():
        UserRace = "Centaure"
        armure = Armure_fer_T1
    elif UserRace == "Demon".casefold():
        UserRace = "Demon"
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

def hitguy(atk,victim,atkf,victimd,victimhp):
    DMG = atkf-victimd
    return DMG

def fight(fdp):
    global UserName
    global UserVie
    global UserForce
    global UserMana
    global UserArmor
    global UserEquipedWeapon
    global UserThrowItem
    global UserThrowItemNb
    from items import Arme_Arc_T1
    from items import Arme_Baton_T1
    from enemies import standart_goule
    from enemies import standart_gnoll
    from enemies import standart_skaven

    print(str(fdp)+" vous fait face, préparez-vous au combat !")
    if fdp in (standart_goule,standart_gnoll,standart_skaven):
        print(str(fdp)+" est une créature standart.")
        if fdp == standart_goule:
            fdpHP = 420
            fdpMP = 0
            fdpDeg = 10
            fdpDef = 0
        elif fdp == standart_gnoll:
            fdpHP = 450
            fdpMP = 0
            fdpDeg = 15
            fdpDef = 0
        elif fdp == standart_skaven:
            fdpHP = 400
            fdpMP = 50
            fdpDeg = 20
            fdpDef = 25
        
    elif fdp in (mid_manshoon,mid_arcaniste,mid_armurefantome):
        print(str(fdp)+" est une créature remarquable.")
        if fdp == mid_manshoon:
            fdpHP = 650
            fdpMP = 100
            fdpDeg = 35
            fdpDef = 30
        elif fdp == mid_arcaniste:
            fdpHP = 650
            fdpMP = 100
            fdpDeg = 40
            fdpDef = 30
        elif fdp == mid_armurefantome:
            fdpHP = 250
            fdpMP = 150
            fdpDeg = 50
            fdpDef = 200
    elif fdp in (final_liche,final_demoniste,final_arcanewarrior):
        print(str(fdp)+" est une créature monstrueuse.")
        if fdp == final_liche:
            fdpHP = 1000
            fdpMP = 300
            fdpDeg = 150
            fdpDef = 250
        elif fdp == final_demoniste:
            fdpHP = 1010
            fdpMP = 280
            fdpDeg = 190
            fdpDef = 290
        elif fdp == final_arcanewarrior:
            fdpHP = 1060
            fdpMP = 200
            fdpDeg = 390
            fdpDef = 250

    print(str(fdp)+" STATS:")
    time.sleep(2)
    print(str(fdpHP)+" HP")
    time.sleep(2)
    print(str(fdpMP)+" MP")
    time.sleep(2)
    print(str(fdpDef)+" Def")
    time.sleep(2)

    while UserVie > 0 and fdpHP > 0:
        PDMGE = UserForce - fdpDef
        EDMGP = fdpDeg - UserArmor
        PlayerAction = ""
        while PlayerAction not in ("Throw".casefold(),"Use".casefold(),"Fuir".casefold(),"Def".casefold(),"Atk".casefold()):
            time.sleep(2)
            PlayerAction = input("Que faire ? : ").casefold()
            if PlayerAction == "Use".casefold():
                print("Vous utilisez : "+str(UserEquipedWeapon))
                if UserEquipedWeapon == Arme_Baton_T1:
                    dammages=hitguy(UserName,fdp,UserForce+40,fdpDef,fdpHP)
                    fdpHP = fdpHP - dammages
                    if fdpHP <= 0:
                        time.sleep(2)
                        print(fdp+" est mort !")
                    else:
                        print(fdp +" a perdu : "+ str(dammages)+ "HP")
                        time.sleep(2)
                        replyed=hitguy(fdp,UserName,fdpDeg,UserArmor,UserVie)
                        print(str(fdp)+" riposte !")
                        UserVie = UserVie - replyed
                        time.sleep(2)
                    if UserVie <= 0:
                        print("Vous êtes mort")
                    else:
                        print("Vous avez subit "+ str(replyed)+" dégats")
                        print("Vous avez maintenant : "+str(UserVie)+" HP")
                elif UserEquipedWeapon == Arme_Arc_T1:
                    dammages=hitguy(UserName,fdp,UserForce+20,fdpDef,fdpHP)
                    fdpHP = fdpHP - dammages
                    if fdpHP <= 0:
                        time.sleep(2)
                        print(fdp+" est mort !")
                    else:
                        print(fdp +" a perdu : "+ str(dammages)+ "HP")
                        time.sleep(2)

                        luck=random.uniform(0,50)

                        replyed=hitguy(fdp,UserName,fdpDeg-luck,UserArmor,UserVie)
                        print(str(fdp)+" Envoi une Pierre pour riposter !")
                        if replyed <= 0:
                            replyed = 0
                            time.sleep(2)
                            print("Vous avez esquivé la pierre")
                        UserVie = UserVie - replyed
                        time.sleep(2)
                        if UserVie <= 0:
                            print("Vous êtes mort")
                        else:
                            print("Vous avez subit "+ str(replyed)+" dégats")
                            print("Vous avez maintenant : "+str(UserVie)+" HP")
                else:
                    print("Vous n'avez pas d'armes")
                    replyed=hitguy(fdp,UserName,fdpDeg,UserArmor,UserVie)
                    print(str(fdp)+" Envoi une Pierre pour riposter !")
                    if replyed <= 0:
                        replyed = 0
                        time.sleep(2)
                        print("Vous avez esquivé la pierre")
                    UserVie = UserVie - replyed
                    time.sleep(2)
                    if UserVie <= 0:
                        print("Vous êtes mort")
                    else:
                        print("Vous avez subit "+ str(replyed)+" dégats")
                        print("Vous avez maintenant : "+str(UserVie)+" HP")

            elif PlayerAction == "Throw".casefold():
                if UserThrowItemNb > 0:
                    print("Vous jettez "+ UserThrowItem)
                    time.sleep(2)
                    throwluck=random.uniform(0,50)
                    if throwluck > 25:
                        dammages=hitguy(UserName,fdp,UserForce+35,fdpDef,fdpHP)
                        fdpHP = fdpHP - dammages
                        if fdpHP <= 0:
                            time.sleep(2)
                            print(fdp+" est mort !")
                        else:
                            print(fdp +" a perdu : "+ str(dammages)+ "HP")
                            time.sleep(2)

                            luck=random.uniform(0,50)

                            replyed=hitguy(fdp,UserName,fdpDeg-luck,UserArmor,UserVie)
                            print(str(fdp)+" Envoi une Pierre pour riposter !")
                            if replyed <= 0:
                                replyed = 0
                                time.sleep(2)
                                print("Vous avez esquivé la pierre")
                            UserVie = UserVie - replyed
                            time.sleep(2)
                            if UserVie <= 0:
                                print("Vous êtes mort")
                            else:
                                print("Vous avez subit "+ str(replyed)+" dégats")
                                print("Vous avez maintenant : "+str(UserVie)+" HP")
                    elif throwluck < 25:
                        print("Vous avez manqué la cible")
                        replyed=hitguy(fdp,UserName,fdpDeg,UserArmor,UserVie)
                        print(str(fdp)+" riposte !")
                        UserVie = UserVie - replyed
                        time.sleep(2)
                        if UserVie <= 0:
                            print("Vous êtes mort")
                        else:
                            print("Vous avez subit "+ str(replyed)+" dégats")
                            print("Vous avez maintenant : "+str(UserVie)+" HP")

            elif PlayerAction == "Atk".casefold():
                dammages=hitguy(UserName,fdp,UserForce,fdpDef,fdpHP)
                fdpHP = fdpHP - dammages
                if fdpHP <= 0:
                    time.sleep(2)
                    print(fdp+" est mort !")
                else:
                    print(fdp +" a perdu : "+ str(dammages)+ "HP")
                    time.sleep(2)
                    replyed=hitguy(fdp,UserName,fdpDeg,UserArmor,UserVie)
                    print(str(fdp)+" riposte !")
                    UserVie = UserVie - replyed
                    time.sleep(2)
                    if UserVie <= 0:
                        print("Vous êtes mort")
                    else:
                        print("Vous avez subit "+ str(replyed)+" dégats")
                        print("Vous avez maintenant : "+str(UserVie)+" HP")
            elif PlayerAction == "Def".casefold():
                replyed=hitguy(fdp,UserName,fdpDeg,UserArmor,UserVie)
                print(UserName+" se protège !")
                time.sleep(1)
                UserVie = UserVie - replyed
                print("Vous avez perdu"+ str(replyed)+" HP")

            elif PlayerAction == "Fuir".casefold():
                print("Vous prennez la fuite et quittez le donjon !")
                time.sleep(1)
                print("Vous avez réussi à échapper à l'affrontement")
                time.sleep(1)
                print("Vous voilà hors du donjon !")
                time.sleep(1)
                print("Vous avez echoué à votre Mission !")
                time.sleep(1)
                print("GAME OVER !")
                time.sleep(3)
                quit()

            else:
                print("Action impossible.")
                print("Fuir - Def - Atk - Use - Throw")

def lootroom (roomstate):
    global UserVie
    global UserForce
    global UserThrowItem
    global UserThrowItemNb

    from items import loot_eat
    from items import loot_heal
    from items import loot_throw

    content = ""
    trap = "trap"
    gift = "gift"
    vide = "vide"
    eat = loot_eat
    heal = loot_heal
    throw = loot_throw

    time.sleep(2)

    print("Vous faites face à un coffre.")
    time.sleep(2)
    chest=""
    while chest not in("Oui".casefold(),"Non".casefold()):
        chest=input("Voulez-vous l'ouvrir ? ").casefold()
        if chest=="Oui".casefold():
            content=random.choice([trap,gift,vide])
            if content == trap:
                print("Le Coffre étais piéger !")
                time.sleep(2)
                UserVie = UserVie - 5
                print("Vous avez perdu 5 HP")
            elif content == gift:
                print("Il ne semble pas être piéger")
                time.sleep(2)
                gift=random.choice([eat,heal,throw])
                if gift == eat:
                    print("Vous avez trouver : "+ eat)
                    time.sleep(2)
                    print("Vous utilisez "+eat+" vous vous sentez restauré")
                    UserForce = UserForce + 5
                    UserVie = UserVie + 15
                elif gift == heal:
                    print("Vous avez trouver : "+ heal)
                    time.sleep(2)
                    print("Vous utilisez "+heal+" votre vie augmente")
                    UserVie = UserVie + 30
                elif gift == throw:
                    print("Vous avez trouver : "+throw)
                    UserThrowItem = throw
                    UserThrowItemNb = UserThrowItemNb + 1
                    print(throw + " a été ajouté à votre inventaire")
            elif content == vide:
                print("Le Coffre est Vide.")

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

    if categorie == "Armes".casefold():
        print("Stock du marchand: ")
        print(Arme_Arc_T1 + " (40 Gold)")
        print(Arme_Baton_T1+ " (10 Gold)")
        time.sleep(1.5)
        print("Voulez vous achetez un de ces objets ?")
        reply=""
        while reply not in ("Oui".casefold(),"Non".casefold()):
            reply=input("Oui / Non: ").casefold()
            if reply == "Oui".casefold():
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
            elif reply == "Non".casefold():
                time.sleep(1)
                print("Redirection au choix de catégories")
                CreateRoom(room_spawn,0)
            else:
                print("Reponse invalide")
    elif categorie == "Armures".casefold():
        print("Le marchand n'a rien pour le moment.")
        CreateRoom(room_spawn,0)

def CreateRoom(room, state):
    if room == room_spawn:
        state = 0
        time.sleep(1)
        print("Armures - Armes - Rien")
        ItemBuy=""
        while ItemBuy not in ("Armes".casefold(),"Armures".casefold(),"Rien".casefold()):
            ItemBuy = input("Quel est votre choix: ").casefold()
            if ItemBuy == "Armes".casefold():
                showShopItem(ItemBuy)
            elif ItemBuy == "Armures".casefold():
                showShopItem(ItemBuy)
            elif ItemBuy == "Rien".casefold():
                print("Vous quittez l'échoppe du Marchand !")
            else:
                print("Choix invalide")
                print("Armes - Armures - Rien")
        state=state+int(1)
    if room == room_dj1:
        Enconter=random.choice([standart_goule,standart_gnoll,standart_skaven])
        getperks(UserLevel,UserClasse,UserRace)
        fight(Enconter)
        state=state+int(1)
    elif room == room_dj2:
        Enconter=random.choice([standart_goule,standart_gnoll,standart_skaven])
        fight(Enconter)
        state=state+int(1)
    elif room == room_dj3:
        Enconter=random.choice([standart_goule,standart_gnoll,standart_skaven])
        fight(Enconter)
        state=state+int(1)
    elif room == room_dj4:
        Enconter=random.choice([mid_manshoon,mid_arcaniste,mid_armurefantome])
        fight(Enconter)
        state=state+int(1)
    elif room == room_dj5:
        Enconter=random.choice([final_arcanewarrior,final_demoniste,final_liche])
        fight(Enconter)
        state=state+int(1)
    elif room == room_chest1:
        lootroom(state)
        state=state+int(1)
    elif room == room_chest2:
        lootroom(state)
        state=state+int(1)
    elif room == room_chest3:
        lootroom(state)
        state=state+int(1)
    elif room == room_chest4:
        lootroom(state)
        state=state+int(1)

### GAME CODE ###
UserMana = 0
UserForce = 0
UserVie = 0
UserPrecision = 0
UserArmor = 0
UserMoney = 300
UserState = 0
UserLevel = 0
UserEquipedWeapon = ""
UserEquipedArmor = ""
UserThrowItem = ""
UserThrowItemNb = 0
UserName=getusername()
UserRace=getuserrace()
UserClasse=getuserclasse()
time.sleep(1)

## CHEAT ZONE UwU ##
if UserName == "Alakazam":
    if UserRace == "orc":
        if UserClasse == "chaman":
            UserForce = 10000
            UserVie = 10000
            UserArmor = 10000
            UserMana = 10000
            print("Alakazam le Chaman - Activé")

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
time.sleep(2)
CreateRoom(room_dj1,UserState)
time.sleep(2)
CreateRoom(room_chest1,UserState)
time.sleep(2)
CreateRoom(room_dj2,UserState)
time.sleep(2)
CreateRoom(room_chest2,UserState)
time.sleep(2)
CreateRoom(room_dj3,UserState)
time.sleep(2)
CreateRoom(room_chest3,UserState)
time.sleep(2)
CreateRoom(room_dj4,UserState)
time.sleep(2)
CreateRoom(room_chest4,UserState)
time.sleep(2)
CreateRoom(room_dj5,UserState)


print("Vous êtes arrivé à la fin du jeu. Bravo !")
time.sleep(5)




