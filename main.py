from sys import exit
import time, random, os

#The function below defines the loot tables, with a generic loot table, as well as a specific one for each dungeon room
def lootTables(inventory,table):
    #The generic loot table has a random chance to give the player 1-2 health potion(s), a damage potion, some basic armour, or 5 Gold
    if table == "generic":
        lootChoice = random.randint(1,4)
        if lootChoice == 1:
            amount = random.randint(1,2)
            if amount == 1:
                print("You found a health potion!")
                loot = {"Potions": {"Health Potion": {"Effect": "Instant Health", "Amount": 1, "Score": 1}}}
                updInventory = inventoryUpdate(inventory,loot)
                return updInventory
            if amount == 2:
                print("You found two health potions!")
                loot = {"Potions": {"Health Potion": {"Effect": "Instant Health", "Amount": 2, "Score": 1}}}
                updInventory = inventoryUpdate(inventory, loot)
                return updInventory
        elif lootChoice == 2:
            print("You found a damage potion!")
            loot = {"Potions": {"Damage Potion": {"Effect": "Damage", "Amount": 1, "Score": 1}}}
            updInventory = inventoryUpdate(inventory,loot)
            return updInventory
        elif lootChoice == 3:
            print("You found some basic armour!")
            decision = input("Do you wish to equip it? (y/n)\n> ")
            if decision == "y":
                inventory = armourUnequip(inventory)
                loot = {"Armour": {"Basic Armour": {"Protection": 1, "Description": "Some basic armour that you found", "Score": 2, "Equipped": "Yes"}}}
                updInventory = inventoryUpdate(inventory,loot)
                return updInventory
            elif decision == "n":
                loot = {"Armour": {"Basic Armour": {"Protection": 1, "Description": "Some basic armour that you found", "Score": 2,"Equipped": "No"}}}
                updInventory = inventoryUpdate(inventory, loot)
                return updInventory
        elif lootChoice == 4:
            print("You found 5 Gold!")
            loot = {"Gold": 5}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
    #Room 1 & 2 loot table will either give 3 health potions, a silver sword, 15 GP, a set of chainmail armour or a book that I added that contains a little bit of information about the dungeon itself
    elif table == "r1&2":
        lootChoice = random.randint(1, 5)
        if lootChoice == 1:
            print("You found three health potions!")
            loot = {"Potions": {"Health Potion": {"Effect": "Instant Health", "Amount": 3, "Score": 1}}}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
        elif lootChoice == 2:
            print("You found a silver sword!")
            loot = {"Weapons": {"Silver Sword": {"Damage": 3, "Description": "A sword cast from silver. A reliable blade of good quality", "Score": 2}}}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
        elif lootChoice == 3:
            print("You found 15 Gold!")
            loot = {"Gold": 15}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
        elif lootChoice == 4:
            print("You found a set of chainmail armour!")
            decision = input("Do you wish to equip it? (y/n)\n> ")
            if decision == "y":
                inventory = armourUnequip(inventory)
                loot = {"Armour": {"Chainmail Armour": {"Protection": 3, "Description": "Some basic chainmail you found. Smells of rust and dried blood.", "Score": 3,"Equipped": "Yes"}}}
                updInventory = inventoryUpdate(inventory, loot)
                return updInventory
            elif decision == "n":
                loot = {"Armour": {"Chainmail Armour": {"Protection": 3, "Description": "Some basic chainmail you found. Smells of rust and dried blood.", "Score": 3,"Equipped": "No"}}}
                updInventory = inventoryUpdate(inventory, loot)
                return updInventory
        elif lootChoice == 5:
            print("You found a book? Wonder what that could contain.")
            loot = {"Special Items": {"Book of the Dungeon": {"Description": "This dungeon is thousands of years old, and they say the final room is guarded by some ferocious beast. None who meet it live to tell the tale. Beware the final room.","Score": 15}}}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
    #Room 3 & 4 doesn't give the player any weapons or armour, as they should have bought some of those from the hub. Instead, the player can find gold, or any of the potions
    elif table == "r3&4":
        lootChoice = random.randint(1, 6)
        if lootChoice == 1:
            print("You found 25GP!")
            loot = {"Gold":25}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
        elif lootChoice == 2:
            print("You found 5 Health Potions!")
            loot = {"Potions": {"Health Potion": {"Effect": "Instant Health", "Amount": 5, "Score": 1}}}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
        elif lootChoice == 3:
            print("You found 2 damage potions!")
            loot = {"Potions": {"Damage Potion": {"Effect": "Damage", "Amount": 2, "Score": 2}}}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
        elif lootChoice == 4:
            print("You found 2 dodge potions!")
            loot = {"Potions": {"Dodge Potion": {"Effect": "Dodge", "Amount": 2, "Score": 2}}}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
        elif lootChoice == 5:
            print("You found 3 defence potions!")
            loot = {"Potions": {"Defense Potion": {"Effect": "Defense", "Amount": 3, "Score": 1}}}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
        elif lootChoice == 6:
            print("You found a book? What good will that do you?")
            loot = {"Special Items": {"Tales from the Final Room": {"Description": "The book tells a story of an adventurer who went into the final room. It is clear that the book is a guess as to what is in the final room, but if it correct, the fight won't be over when it first may seem so.","Score": 25}}}
            updInventory = inventoryUpdate(inventory, loot)
            return updInventory
    # I decided not to give room 5 its own loot table, as there would be no need to give the player anything else, as the character would just be leaving the dungeon anyways.



#The function below unequipps whatever armour the player is currently wearing, so that they can now wear the improved armour they have just obtained
def armourUnequip(inventory):
    for armour in inventory["Armour"]:
        if inventory["Armour"][armour]["Equipped"] == "Yes":
            inventory["Armour"][armour]["Equipped"] = "No"
            return inventory
    return inventory


#The function below updates the inventory with the item passed into it
def inventoryUpdate(inventory, item):
    itemList = list(item)
    if itemList[0] == "Weapons":
        inventory["Weapons"].update(item["Weapons"])
        updInventory = inventory
        return updInventory
    elif itemList[0] == "Armour":
        inventory["Armour"].update(item["Armour"])
        updInventory = inventory
        return updInventory
    elif itemList[0] == "Potions":
        itemName = list(item["Potions"].items())
        itemNamer = itemName[0][0]
        if itemNamer in inventory["Potions"]:
            amountOfPotions = inventory["Potions"][itemNamer]["Amount"]
            inventory["Potions"][itemNamer]["Amount"] += amountOfPotions
        else:
            inventory["Potions"].update(item["Potions"])
        updInventory = inventory
        return updInventory
    elif itemList[0] == "Special Items":
        inventory["Special Items"].update(item["Special Items"])
        updInventory = inventory
        return updInventory
    elif itemList[0] == "Gold":
        goldAmount = item["Gold"]
        inventory["Gold"] += goldAmount
        return inventory

#The function below checks whether the player, and if they are, giving them the choice to exit, restart from the last room they entered, or restart from the begining
def deathCheck(health):
    if health <= 0:
        print("\nYou died!")
        descision = int(input("""
        Do you want to:
        1) Exit the game
        2) Retry the game from the beginning
        > """))
        if descision == 1:
            print("Alright then, see you soon!")
            exit(0)
        elif descision == 2:
            main()
    else:
        pass

#The function below updates the amount of gold the player has based upon the amount they spend
def goldSpend(inventory,goldSpent):
    goldRemaining = inventory["Gold"]
    inventory["Gold"] = goldRemaining - goldSpent
    return inventory

#The function below checks what effect the player has active on them, and then creating a list with how that will impact them
def effectChecker(activeEffect):
    impact = []
    for i in range(len(activeEffect)):
        if activeEffect[i] == "Hydration":
            print("You feel more hydrated!")
            impact.append(["none",0])
            return activeEffect, impact
        elif activeEffect[i] == "Instant Health":
            healthGenerated = random.randint(6, 12)
            print(f"You gain {healthGenerated} health!")
            impact.append(["heal",healthGenerated])
        elif activeEffect[i] == "Defense":
            print("You will take 20% reduced damage from the next attack!")
            activeEffect.append("Defense")
            impact.append(["defense",20])
        elif activeEffect[i] == "Dodge":
            print("You will dodge the next attack!")
            activeEffect.append("Dodge")
            impact.append(["dodge",1])
        elif activeEffect[i] == "Damage":
            damageIncrease = random.randint(1, 10)
            print(f"You'll do {damageIncrease} extra damage on you next attack!")
            activeEffect = "Damage"
            impact.append(["damage",damageIncrease])
        else:
            impact.append(["nothing", 0])
    return activeEffect, impact

#The below function finds the profile of the enemy that is being fought by the player, and returns the appropriate stat block
def enemyProfiles(enemy):
    if enemy == "zombie":
        profile = {"Zombie":{"Health":5, "Attack": 2}}
        return profile
    elif enemy == "werewolf":
        profile = {"Werewolf": {"Health": 15, "Attack": 5}}
        return profile
    elif enemy == "gremlin":
        profile = {"Gremlin": {"Health": 8, "Attack": 3}}
        return profile
    elif enemy == "bear":
        profile = {"Bear": {"Health": 40, "Attack": 10}}
        return profile
    elif enemy == "bear final form":
        profile = {"Bear Final Form": {"Health": 50, "Attack": 25}}
        return profile
    elif enemy == "mimic":
        profile = {"Mimic": {"Health": 20, "Attack": 8}}
        return profile

#The function below removes an effect from the active effects list once it has been used
def effectPopper(activeEffects, effectToPop):
    for i in range(len(activeEffects)):
        if activeEffects[i][0] == effectToPop:
            activeEffects[i].pop()
            return activeEffects

def impactFinder(impact, impactToFind):
    for i in range(len(impact)):
        if impact[i][0] == impactToFind:
            return True, i
    return False, 420

#The function below is the combat function for both the player and the enemy they are fighting
def combat(health, inventory, activeEffects, enemyProfile):
    enemyList = list(enemyProfile.items())
    enemyName = enemyList[0][0]
    beforeDamageHPA = enemyProfile[enemyName]["Health"]
    beforeDamageHPB = beforeDamageHPA
    pCombat = True
    eCombat = False
    combat = True
    while combat:
        while pCombat:
            dChance = 10
            activeEffects, impact = effectChecker(activeEffects)
            print("It is your turn now, what do you do?")
            descision = int(input(f"""
            1) Attack the {enemyName}
            2) Consume a potion
            3) Prepare to dodge the next attack
            > """))
            if descision == 1:
                print("\nWhat weapon do you wish to attack with?")
                weaponList = []
                iterator = 1
                allWeapons = [*inventory["Weapons"].keys()]
                for weapon in allWeapons:
                    print(f"{iterator}) {weapon}")
                    weaponList.append(weapon)
                    iterator += 1
                weaponDescision = int(input("> "))
                weaponID = weaponList[weaponDescision - 1]
                found, position = impactChecker(impact,"damage")
                if found:
                    damageDealt = inventory["Weapons"][str(weaponID)]["Damage"] + impact[position][1]
                    activeEffects = effectPopper(activeEffects, "Damage")
                else:
                    damageDealt = inventory["Weapons"][str(weaponID)]["Damage"]
                beforeDamageHPB -= damageDealt
                print(f"You deal {damageDealt} damage to the {enemyName}!")
                time.sleep(1)
                print(f"The {enemyName} now has {beforeDamageHPB}/{beforeDamageHPA} HP!")
                time.sleep(0.5)
                enemyProfile[enemyName]["Health"] -= damageDealt
                if enemyProfile[enemyName]["Health"] <= 0:
                    combat = False
                    pCombat = False
                else:
                    eCombat = True
                    pCombat = False
            elif descision == 2:
                potionNo = 1
                potionList = []
                for potion in list(inventory["Potions"]):
                    print(f"{potionNo}) {potion}")
                    potionList.append(potion)
                    potionNo += 1
                potionUse = int(input("\nWhich potion do you want to use?\n> ")) - 1
                potionUsed = potionList[potionUse]
                inventory, health, potionEffect = potionUpdate(inventory, potionUsed, health)
                activeEffects.append(potionEffect)
                eCombat = True
                pCombat = False
            elif descision == 3:
                dChance = 70
                eCombat = True
                pCombat = False

        while eCombat:
            print(f"\nIt is now the {enemyName}'s turn!")
            time.sleep(1)
            print(f"The {enemyName} is going to attack you!")
            enemyDamage =  enemyProfile[enemyName]["Attack"]
            found, position = impactFinder(impact, "dodge")
            if found:
                print("Because you drank a dodge potion, you dodge the attack!")
                activeEffects = effectPopper(activeEffects, "Dodge")
                eCombat = False
                pCombat = True
            else:
                # The code below reduces the enemy's damage, according to how much protection their armour gives them
                found, position = impactFinder(impact, "defense")
                if found:
                    print("Because you drank a defence potion, you take 20% less damage.")
                    enemyDamage *= 0.8
                    enemyDamage = round(enemyDamage)
                    activeEffects = effectPopper(activeEffects, "Defense")
                for armour in inventory["Armour"]:
                    if inventory["Armour"][armour]["Equipped"] == "Yes":
                        armourName = armour
                if inventory["Armour"][armour]["Protection"] != 0:
                    armourReduction = (10-inventory["Armour"][armourName]["Protection"])/10
                    enemyDamage *= armourReduction
                    enemyDamage = round(enemyDamage)
                # The portion of code below decides whether the player will dodge the enemies attack
                dodging = random.randint(1, 100)
                if dodging <= dChance:
                    print(f"You dodged the {enemyName}'s attack!")
                    eCombat = False
                    pCombat = True
                else:
                    health -= enemyDamage
                    deathCheck(health)
                    print(f"You have taken {enemyDamage} damage! You now have {health}/20 health!")
                    eCombat = False
                    pCombat = True

    return health, inventory, activeEffects

#The function below prints out the entire inventory for the player to see
def viewInventory(inventory):
    for category in inventory.items():
        iteration = 1
        if category[0] != "Gold":
            print(f"\n{category[0]}:\n")
            for item in category[1]:
                print(f"{iteration}) {item}:")
                iteration += 1
                for descriptor in inventory[category[0]][item]:
                    print(f"{descriptor}: {inventory[category[0]][item][descriptor]}")
        else:
            amountGold = inventory["Gold"]
            print(f"\nGold: {amountGold}\n")

def impactChecker(impact,effectToLookfor):
    for i in range(len(impact)):
        if impact[i][0] == effectToLookfor:
            return True, i
    return False, 69

#The function below updates the active effect that the player has, heals them if they've used a health potion
#and removes the potion from the inventory if the player has no more of that potion
def potionUpdate(inventory, potion, health):
    potionEffect,impact = effectChecker(inventory["Potions"][potion]["Effect"])
    found, position = impactChecker(impact,"heal")
    if found:
        if health + impact[position][1] > 20:
            health = 20
            print("You now have 20/20HP!")
        else:
            health += impact[position][1]
            print(f"You now have {health}/20HP!")
    inventory["Potions"][potion]["Amount"] -= 1
    if inventory["Potions"][potion]["Amount"] == 0:
        inventory["Potions"].pop(potion)
    return inventory, health, potionEffect

#The function below defines what happens in the forest before entering the dungeon
def theForest(inventory, health):
    print("You find yourself in the thicket, standing at the mouth of the dungeon")
    time.sleep(1)
    print("You know that you must go into the dungeon, but before you go in, you can prepare.\n")
    time.sleep(1)
    print("What do you do?")
    decision = int(input("""
    1) Scavenge the forest, there must be something here.
    2) Go straight into the dungeon.
    3) Check your inventory out 
    4) Go home to your family
    > """))
    if decision == 4:
        #I decided to punish the player for cowardice if they go back home, mainly because immediately going back home would defeat the object of the game
        print("\nAs you begin to walk back to your family's house, you realise that they were the ones who wanted you to do this.")
        time.sleep(2)
        print("They wanted you to avenge your brother.")
        time.sleep(1)
        print("Coward.")
        health = 0
        deathCheck(health)
    elif decision == 1:
        event = random.randint(1,100)
        if event == 1:
            # I decided to include a 1% chance of the player finding a bottomless pit that they fall into while scavenging
            print("\nAs you begin to scavenge around the forest, you fall into a bottomless pit")
            print("You think as you're falling, that you were probably already prepared enough.\nBut now you must accept your fate.")
            health = 0
            deathCheck(health)
        elif event == 100:
            # To make sure everything was equal, there is also a 1% chance of finding an extremely over-powered weapon that will kill everything instantly
            time.sleep(2)
            print("\nBy some absolute miracle, you found an AK-47, as well as an excessive amount of ammunition!")
            print("With this unstoppable force by your side, you feel confident to go now go straight into the dungeon")
            gun = {"Weapons": {"AK-47": {"Damage": 10000, "Description": "The Gods decided to be merciful to you today", "Score": -1}}}
            updInventory = inventoryUpdate(inventory, gun)
            return updInventory
        else:
            # However 98% of the time the player will just find a copper shortsword, that is a *slight* improvement in weapon over the big stick they had before
            time.sleep(1)
            print("\nWhile potentially not as grand as you may have hoped for, you found a copper shortsword!")
            print("With an improvement in weapon over your big stick, you enter the dungeon, slightly more confident.")
            copperShortsword = {"Weapons": {"Copper Shortsword": {"Damage": 2, "Description": "It's a miracle you found this in a forest", "Score": 2}}}
            updInventory = inventoryUpdate(inventory, copperShortsword)
            return updInventory
    elif decision == 2:
        #I felt as if it would still be a bit unfair to give the player that walks in without scavenging nothing, so I gave them a singular health potion
        print("Full of confidence, you walk into the dungeon, knowing the gods will act in your favour.")
        print("As you walk in, you find a health potion! Lucky you!")
        healthPot = {"Potions": {"Health Potion": {"Effect": "Instant Health", "Amount": 1, "Score": 1}}}
        updInventory = inventoryUpdate(inventory, healthPot)
        return updInventory
    elif decision == 3:
        viewInventory(inventory)
        print("What do you do next?")
        decision = int(input("""
        1) Scavenge the forest, there must be something here.
        2) Go straight into the dungeon.
        3) Go home to your family
        > """))
        if decision == 1:
            event = random.randint(1, 100)
            if event == 1:
                # I decided to include a 1% chance of the player finding a bottomless pit that they fall into while scavenging
                print("\nAs you begin to scavenge around the forest, you fall into a bottomless pit")
                print(
                    "You think as you're falling, that you were probably already prepared enough.\nBut now you must accept your fate.")
                health = 0
                deathCheck(health)
            elif event == 100:
                # To make sure everything was equal, there is also a 1% chance of finding an extremely over-powered weapon that will kill everything *instantly*q
                time.sleep(2)
                print("\nBy some absolute miracle, you found an AK-47, as well as an excessive amount of ammunition!")
                print("With this unstoppable force by your side, you feel confident to go now go straight into the dungeon")
                gun = {"Weapons": {
                    "AK-47": {"Damage": 10000, "Description": "The Gods decided to be merciful to you today", "Score": -1}}}
                updInventory = inventoryUpdate(inventory, gun)
                return updInventory
            else:
                # However 98% of the time the player will just find a copper shortsword, that is a *slight* improvement in weapon over the big stick they had before
                time.sleep(1)
                print("\nWhile potentially not as grand as you may have hoped for, you found a copper shortsword!")
                print("With an improvement in weapon over your big stick, you enter the dungeon, slightly more confident.")
                copperShortsword = {"Weapons": {
                    "Copper Shortsword": {"Damage": 2, "Description": "It's a miracle you found this in a forest",
                                          "Score": 2}}}
                updInventory = inventoryUpdate(inventory, copperShortsword)

                return updInventory
        elif decision == 2:
            # I felt as if it would still be a bit unfair to give the player that walks in without scavenging nothing, so I gave them a singular health potion
            print("Full of confidence, you walk into the dungeon, knowing the gods will act in your favour.")
            print("As you walk in, you find a health potion! Lucky you!")
            healthPot = {"Potions": {"Health Potion": {"Effect": "Instant Health", "Amount": 1, "Score": 1}}}
            updInventory = inventoryUpdate(inventory, healthPot)
            return updInventory
        elif decision == 3:
            # I decided to punish the player for cowardice if they go back home, mainly because immediately going back home would defeat the object of the game
            print("\nAs you begin to walk back to your family's house, you realise that they were the ones who wanted you to do this.")
            time.sleep(2)
            print("They wanted you to avenge your brother.")
            time.sleep(1)
            print("Coward.")
            health = 0
            deathCheck(health)

#This defines what happens in the dungeon enterance, where the player can scavenge the room for items they can use
def dungeonEnterance(inventory, health, activeEffects):
    time.sleep(2)
    #I decided to include a 10% chance that the player falls down the stairs, and a 1% chance that they also break their neck from that stair falling.
    fallDownStairs = random.randint(1,100)
    if fallDownStairs % 10 == 0:
        print("\nAs you enter the dungeon, you fall down the stairs!")
        time.sleep(1)
        if fallDownStairs == 100:
            print("Today was not your lucky day, as you fell down the stairs, you broke your neck!")
            health = 0
            deathCheck(health)
        else:
            # The damage the player takes from falling down the stairs is random, and will potentially barely impact them, or leave them on 1HP!
            damage = random.randint(1,19)
            print(f"While you were unlucky, you didn't die! You take {damage} damage!\nYou now have {health-damage}/20 health.")
            time.sleep(1)
            health -= damage
    print("\nAs you continue down the stairs to the dungeon, you look around this stone brick room. You see the wooden entrance to the first and second chamber.")
    time.sleep(1)
    print("You have time to prepare for the fight, you see a pile of assorted objects in the corner of the room, perhaps containing something of use/value.")
    time.sleep(1)
    oneDone = False
    preparing = True
    while preparing:
        print("What do you do?")
        decision = int(input("""
        1) Check out that pile in the corner, maybe you'll find something
        2) Scavenge the rest of the room, surely there's something around here
        3) Check out my inventory to see if you really need to prepare
        4) Sleep, you've got two big fights upcoming and you need your rest
        5) Drink one of my potions
        > """))
        if decision == 1:
            if not oneDone:
                oneDone = True
                inventory = lootTables(inventory,"generic")
                time.sleep(0.5)
                inventory = lootTables(inventory, "generic")
                time.sleep(0.5)
                inventory = lootTables(inventory, "generic")
                time.sleep(0.5)
                kontinue = input("\nDo you want to continue preparing? (y/n)\n> ")
                if kontinue.lower() == "y":
                    preparing = True
                else:
                    preparing = False
            elif oneDone:
                print("You begin to walk over to the pile, and you remember that you've already searched it!\n")
                preparing = True
        elif decision == 3:
            viewInventory(inventory)
            preparing = True
        elif decision == 2:
            inventory = lootTables(inventory,"generic")
            time.sleep(0.5)
            kontinue = input("\nDo you want to continue preparing? (y/n)\n> ")
            if kontinue.lower() == "y":
                preparing = True
            else:
                preparing = False
        elif decision == 4:
            #The sleep choice has the potential to fully heal the player (not really needed unless they fell down the stairs), but also a 20% chance of killing the player
            deathChance = random.randint(1,100)
            if deathChance % 5 == 0:
                print("\nUnfortunately, sleeping unguarded at the enterance of a dungeon is pretty stupid.")
                health = 0
                deathCheck(health)
            else:
                time.sleep(3)
                print("By some absolute miracle, nothing happened to you while you sleep. You regain all of you HP!")
                print("With all of your health back, you feel confident enough to walk into the first chamber!")
                health = 20
                preparing = False
        elif decision == 5:
            potionNo = 1
            potionList = []
            for potion in list(inventory["Potions"]):
                print(f"{potionNo}) {potion}")
                potionList.append(potion)
                potionNo += 1
            potionUse = int(input("\nWhich potion do you want to use?\n> ")) -1
            potionUsed = potionList[potionUse]
            inventory, health, potionEffect = potionUpdate(inventory, potionUsed, health)
            activeEffects.append(potionEffect)
            kontinue = input("\nDo you want to continue preparing? (y/n)\n> ")
            if kontinue.lower() == "y":
                preparing = True
            else:
                preparing = False
    return inventory, health, activeEffects

#This defines what happens in the first room, where the player fights a zombie, so that they can get used to the turn-based combat system
def dungeonFirstRoom(inventory, health, activeEffects):
    print("\nAs you walk into the chamber, you first notice the burning torches within the room.\nThe room smells of old blood, and rotting flesh.")
    print("Then as you catch your bearings of the room, a Zombie appears infront of you!")
    zombieProfile = enemyProfiles("zombie")
    health, inventory, activeEffects = combat(health, inventory, activeEffects, zombieProfile)
    time.sleep(1)
    print("You see the zombie's now definitely lifeless corpse on the floor, and you look to the end of the room, and a chest appears before you!")
    inventory = lootTables(inventory,"generic")
    time.sleep(0.5)
    inventory = lootTables(inventory,"generic")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r1&2")
    time.sleep(0.5)
    print("Before you head into the second room, what do you do to prepare?")
    descision = int(input("""
    1) Check out your inventory then head on in
    2) Drink a potion and then go in
    3) Sleep to rest and recover before the fight, and then head in
    4) Go straight into the next room
    > """))
    if descision == 4:
        return inventory, health, activeEffects
    elif descision == 1:
        viewInventory(inventory)
        return inventory, health, activeEffects
    elif descision == 2:
        potionNo = 1
        potionList = []
        for potion in list(inventory["Potions"]):
            print(f"{potionNo}) {potion}")
            potionList.append(potion)
            potionNo += 1
        potionUse = int(input("\nWhich potion do you want to use?\n> ")) - 1
        potionUsed = potionList[potionUse]
        inventory, health, potionEffect = potionUpdate(inventory, potionUsed, health)
        activeEffects.append(potionEffect)
        return inventory, health, activeEffects
    elif descision == 3:
        deathChance = random.randint(1, 100)
        if deathChance % 5 == 0:
            print("\nUnfortunately, sleeping unguarded right next to a dungeon room is a pretty stupid idea.")
            health = 0
            deathCheck(health)
        else:
            time.sleep(3)
            print("By some absolute miracle, nothing happened to you while you sleep. You regain all of you HP!")
            print("With all of your health back, you feel confident enough to walk into the first chamber!")
            health = 20
            return inventory, health, activeEffects

#This defines what happens in the second room, where the player fights a gremlin
def dungeonSecondRoom(inventory, health, activeEffects):
    print("\nYou walk into the room, and this one looks eerily like the last, bar the smell of rotten flesh.")
    time.sleep(2)
    print("You look around the room expecting a foe of some form to appear, but none appeared.")
    time.sleep(0.5)
    print("When suddenly, a gremlin begins to scream and charge at you!")
    gremlinProfile = enemyProfiles("gremlin")
    health, inventory, activeEffects = combat(health, inventory, activeEffects, gremlinProfile)
    time.sleep(1)
    print("You see the butchered corpse of the goblin infront of the door you came in through.")
    time.sleep(0.5)
    print("You walk over to the loot chest, to claim some treasures before you go into")
    inventory = lootTables(inventory, "generic")
    time.sleep(0.5)
    inventory = lootTables(inventory, "generic")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r1&2")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r1&2")
    time.sleep(0.5)
    print("With your new found treasures, you head into the hub, to prepare yourself for the struggle of the last three rooms.\n")
    return inventory, health, activeEffects

#This defines what happens in the hub, where the player has the opportunity to spend their gold to prepare themselves for the final three rooms
def dungeonMiddleHub(inventory, health, activeEffects):
    time.sleep(0.5)
    print("\nYou look around this place. You hear the hustle and bustle from the market down the street. The roads are fairly clean considering its position.")
    time.sleep(1.5)
    print("You have (in theory) as much time as you could need in this place to prepare for the final room.")
    time.sleep(0.5)
    hubbing = True
    while hubbing:
        goldRemaining = inventory["Gold"]
        print(f"You have {goldRemaining}GP")
        time.sleep(0.5)
        print("What do you do?")
        descision = int(input("""
        1) View your inventory
        2) Go to the markets to buy equipment
        3) Try and find an inn to stay in for the night
        4) Proceed into the final rooms
        > """))
        if descision == 1:
            viewInventory(inventory)
            time.sleep(0.5)
            hubbing = True
        elif descision == 4:
            return inventory, health, activeEffects
        elif descision == 3:
            time.sleep(1)
            print("After searching for an inn to stay for the night, you come across a local inn!")
            time.sleep(1.5)
            print("The innkeeper tells you that the fare is 3GP per night!")
            time.sleep(1.5)
            if goldRemaining >= 3:
                print("Would you like to stay the night? (y/n)")
                sleep = input("> ")
                sleep = sleep.lower()
                if sleep == "y":
                    print(f"You give the innkeeper 3GP to stay at the inn that night!")
                    inventory = goldSpend(inventory, 3)
                    health = 20
                    time.sleep(4)
                    print("You sleep the night, and you're now at full health again!\n")
                    hubbing = True
                else:
                    print("You apologise to the innkeeper for wasting his time, but you decide to not stay there tonight.")
                    hubbing = True
            else:
                print("Unfortunately, you do not have the gold remaining!\nYou apologise to the innkeeper for the inconvenience, and you walk out the inn.")
                hubbing = True
        elif descision == 2:
            time.sleep(1)
            print("You walk over to the market, and find various different stalls. Which stall do you go to?")
            stall = int(input("""
            1) Andy's Amazing Armour
            2) Patricia's Perfect Potions Stand
            3) William's Wicked Weapons
            > """))
            if stall == 1:
                time.sleep(1)
                print("You walk over to the armour stand, and are greeted by a jolly man called Andy, and he tells you of what he has in stock.")
                time.sleep(1)
                print("""
                1) Re-enforced Steel Armour (5GP)
                2) Hallowed Armour (10GP)
                3) Re-enforced Chainmail Armour (2GP)
                """)
                print("\nWhich set of armour do you want?")
                armourChosen = int(input("> "))
                if armourChosen == 1:
                    if goldRemaining < 5:
                        print("Unfortunately, you don't have the gold for that armour! You apologise to Andy, and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print("You hand Andy over the 5GP, and you now own a set of Re-enforced Steel Armour!")
                        inventory = goldSpend(inventory, 5)
                        print("Do you wish to equip it? (y/n)\n> ")
                        equip = input()
                        equip = equip.lower()
                        if equip == "y":
                            inventory = armourUnequip(inventory)
                            loot = {"Armour": {"Re-enforced Steel Armour": {"Protection": 5,"Description": "A set of polished re-enforced steel armour, made personally by the finest blacksmith in the dungeon.", "Score": 4, "Equipped": "Yes"}}}
                            inventory = inventoryUpdate(inventory, loot)
                            hubbing = True
                        elif equip == "n":
                            loot = {"Armour": {"Re-enforced Steel Armour": {"Protection": 5,"Description": "A set of polished re-enforced steel armour, made personally by the finest blacksmith in the dungeon.","Score": 4, "Equipped": "No"}}}
                            inventory = inventoryUpdate(inventory, loot)
                            hubbing = True
                elif armourChosen == 2:
                    if goldRemaining < 10:
                        print("Unfortunately, you don't have the gold for that armour! You apologise to Andy, and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print("You hand Andy over the 10GP, and you now own a set of Hallowed Armour!")
                        inventory = goldSpend(inventory, 10)
                        print("Do you wish to equip it? (y/n)\n> ")
                        equip = input()
                        equip = equip.lower()
                        if equip == "y":
                            inventory = armourUnequip(inventory)
                            loot = {"Armour": {"Hallowed Armour": {"Protection": 7,"Description": "A set of divine Hallowed Armour, forged personally by the finest blacksmith in the dungeon.", "Score": 8, "Equipped": "Yes"}}}
                            inventory = inventoryUpdate(inventory, loot)
                            hubbing = True
                        elif equip == "n":
                            loot = {"Armour": {"Hallowed Armour": {"Protection": 7,"Description": "A set of divine Hallowed Armour, forged personally by the finest blacksmith in the dungeon.","Score": 8, "Equipped": "No"}}}
                            inventory = inventoryUpdate(inventory, loot)
                            hubbing = True
                elif armourChosen == 3:
                    if goldRemaining < 2:
                        print("Unfortunately, you don't have the gold for that armour! You apologise to Andy, and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print("You hand Andy over the 2GP, and you now own a set of Re-enforced Chainmail Armour!")
                        inventory = goldSpend(inventory, 2)
                        print("Do you wish to equip it? (y/n)\n> ")
                        equip = input()
                        equip = equip.lower()
                        if equip == "y":
                            inventory = armourUnequip(inventory)
                            loot = {"Armour": {"Re-enforced Chainmail Armour": {"Protection": 4,"Description": "A set of re-enforced chainmail armour, forged personally by the finest blacksmith in the dungeon.", "Score": 5, "Equipped": "Yes"}}}
                            inventory = inventoryUpdate(inventory, loot)
                            hubbing = True
                        elif equip == "n":
                            loot = {"Armour": {"Re-enforced Chainmail Armour": {"Protection": 4,"Description": "A set of re-enforced chainmail armour, forged personally by the finest blacksmith in the dungeon.","Score": 5, "Equipped": "No"}}}
                            inventory = inventoryUpdate(inventory, loot)
                            hubbing = True
            elif stall == 2:
                time.sleep(1)
                print("You walk over to the potion stand, and are greeted by a mysterious lady called Patricia, and she presents to you of what she has in stock.")
                time.sleep(1)
                print("""
                1) Health Potion (1GP per potion)
                2) Dodge Potion (3GP per potion)
                3) Damage Potion (3GP per potion)
                4) Defence Potion (2GP per potion)
                """)
                print("Which potion would you like?")
                potionChosen = int(input("> "))
                print("How many would you like?")
                amount = int(input("> "))
                if potionChosen == 1:
                    cost = amount * 1
                    if cost > goldRemaining:
                        print("Unfortunately, you do not have enough for that! You apologise to the Patricia, and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print(f"You hand over {amount*1}GP to Patricia and she hands you the {amount} Health Potion(s)")
                        inventory = goldSpend(inventory, amount)
                        potion = {"Potions": {"Health Potion": {"Effect": "Instant Health", "Amount": amount, "Score": 1}}}
                        inventory = inventoryUpdate(inventory, potion)
                        hubbing = True
                elif potionChosen == 2:
                    cost = amount * 3
                    if cost > goldRemaining:
                        print("Unfortunately, you do not have enough for that! You apologise to the Patricia, and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print(f"You hand over {cost}GP to Patricia and she hands you the {amount} Dodge Potion(s)")
                        inventory = goldSpend(inventory, cost)
                        potion = {"Potions": {"Dodge Potion": {"Effect": "Dodge", "Amount": amount, "Score": 2}}}
                        inventory = inventoryUpdate(inventory, potion)
                        hubbing = True
                elif potionChosen == 3:
                    cost = amount * 3
                    if cost > goldRemaining:
                        print("Unfortunately, you do not have enough for that! You apologise to the Patricia, and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print(f"You hand over {cost}GP to Patricia and she hands you the {amount} Health Potion(s)")
                        inventory = goldSpend(inventory, cost)
                        potion = {"Potions": {"Damage Potion": {"Effect": "Damage", "Amount": amount, "Score": 2}}}
                        inventory = inventoryUpdate(inventory, potion)
                        hubbing = True
                elif potionChosen == 4:
                    cost = amount * 2
                    if cost > goldRemaining:
                        print("Unfortunately, you do not have enough for that! You apologise to the Patricia, and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print(f"You hand over {cost}GP to Patricia and she hands you the {amount} Health Potion(s)")
                        inventory = goldSpend(inventory, cost)
                        potion = {"Potions": {"Defense Potion": {"Effect": "Defense", "Amount": amount, "Score": 1}}}
                        inventory = inventoryUpdate(inventory, potion)
                        hubbing = True
            elif stall == 3:
                time.sleep(1)
                print("You walk over to the weapons stand, and are greeted by the weird but wonderful William, and he tells you of what he has in.")
                time.sleep(1)
                print("""
                1) Night's Edge (7GP)
                2) The Zenith (50GP)
                3) True Hallowed Blade (20GP)
                """)
                print("Which one do you want to buy?")
                blade = int(input("> "))
                if blade == 1:
                    if goldRemaining < 7:
                        print("You don't have enough gold to afford that weapon unfortunately! You apologise to William and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print("You hand over 7GP over to William, and he hands you the mythical Night's Edge!")
                        inventory = goldSpend(inventory, 7)
                        blade = {"Weapons": {"Night's Edge": {"Damage": 7, "Description": "The legendary Night's Edge blade! Forged out of some of the most powerful weapons, from both heaven and hell.", "Score": 4}}}
                        inventory = inventoryUpdate(inventory, blade)
                        hubbing = True
                elif blade == 2:
                    if goldRemaining < 50:
                        print("You don't have enough gold to afford that weapon unfortunately! You apologise to William and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print("You hand over 50GP over to William, and he hands you the blade of legends, The Zenith!")
                        inventory = goldSpend(inventory, 50)
                        blade = {"Weapons": {"The Zenith": {"Damage": 30, "Description": "The sword only dreamed of in legend, The Zenith. A blade so powerful, they say it needs to be slightly adjusted in strength.", "Score": 10}}}
                        inventory = inventoryUpdate(inventory, blade)
                        hubbing = True
                elif blade == 3:
                    if goldRemaining < 20:
                        print("You don't have enough gold to afford that weapon unfortunately! You apologise to William and walk away from the stall.")
                        hubbing = True
                    else:
                        time.sleep(1)
                        print("You hand over 20GP over to William, and he hands you the legendary True Hallowed Blade!")
                        inventory = goldSpend(inventory, 20)
                        blade = {"Weapons": {"True Hallowed Blade": {"Damage": 15, "Description": "A blade so powerful, those who fight against it, regret doing so.", "Score": 4}}}
                        inventory = inventoryUpdate(inventory, blade)
                        hubbing = True

#This defines what happens in the third room, where the player fights a werewolf
def dungeonThirdRoom(inventory, health, activeEffects):
    print("\nYou walk into the third chamber, the smell of blood more apparent in this room.")
    time.sleep(1)
    print("The blood doesn't smell as old as it did in the other rooms. It is clear to you that what awaits you in these next few rooms will be far more difficult.")
    time.sleep(1)
    print("You prepare yourself for these upcoming fights. You remind yourself why you are here. For your family.")
    time.sleep(1)
    print("As you collect yourself, you hear howling come from in front of you, as a werewolf starts charging at you!")
    time.sleep(0.5)
    wolfProfile = enemyProfiles("werewolf")
    health, inventory, activeEffects = combat(health, inventory, activeEffects, wolfProfile)
    time.sleep(1)
    print("You look at the werewolf, it transforming back into the poor soul that was cursed all those years ago. At least their suffering has ended.")
    time.sleep(0.5)
    print("With each room, you wish more and more you could see your family once again.")
    time.sleep(1)
    print("You walk over to the loot chest, to hopefully get some loot to prepare yourself for the next room.")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    print("With your newfound loot, you have some time to prepare for the next room.")
    prepare = True
    while prepare:
        print("What do you do?")
        descision = int(input("""
        1) View your inventory
        2) Consume one of your potions
        3) Head into the fourth room
        > """))
        if descision == 1:
            viewInventory(inventory)
            time.sleep(1)
            prepare = True
        elif descision == 2:
            potionNo = 1
            potionList = []
            for potion in list(inventory["Potions"]):
                print(f"{potionNo}) {potion}")
                potionList.append(potion)
                potionNo += 1
            potionUse = int(input("\nWhich potion do you want to use?\n> ")) - 1
            potionUsed = potionList[potionUse]
            inventory, health, potionEffect = potionUpdate(inventory, potionUsed, health)
            activeEffects.append(potionEffect)
            time.sleep(1)
            prepare = True
        elif descision == 3:
            prepare = False
    return inventory, health, activeEffects

# This defines what happens in the fourth room, where the player fights a mimic
def dungeonFourthRoom(inventory, health, activeEffects):
    print("\nYou walk into the room, and you smell the blood again, but this time instead of fur, rotting flesh, or anything like that, you smell rust?")
    time.sleep(1)
    print("Your confusion is only furthered when you find that the chest for defeating the enemy in the middle of the room already?")
    time.sleep(1)
    print("You approach the chest, perhaps it rewards you already for getting this far?")
    time.sleep(1)
    print("As you go to open the chest, you discover that this is no chest at all, it's a mimic!")
    time.sleep(0.5)
    mimicProfile = enemyProfiles("mimic")
    health, inventory, activeEffects = combat(health, inventory, activeEffects, mimicProfile)
    time.sleep(0.5)
    print("You now see the broken chest in-front of you, and before you're even able to go over to the loot chest, the mimic spits out 20GP! ")
    loot = {"Gold": 20}
    inventory = inventoryUpdate(inventory, loot)
    time.sleep(0.5)
    print("After collecting the extra 20GP, you walk over to the loot chest, that will hopefully contain enough for you to be able to defeat the beast in the final room!")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    inventory = lootTables(inventory, "r3&4")
    time.sleep(0.5)
    print("With your new found items, you walk into the preparation room, to hopefully prepare you for this final battle.")
    return inventory, health, activeEffects

#This defines what happens in the preparation room, before the final room.
def dungeonPreparationRoom(inventory, health, activeEffects):
    print("\nYou enter into the preparation room, it doesn't really smell of a whole lot.")
    time.sleep(1)
    print("You feel a whole lot safer in this room compared to all the other rooms (other than the hub), almost as if the dungeon knows the dangers you are about to face.")
    time.sleep(1)
    print("You have a difficult fight up ahead of you, and you should prepare yourself.")
    time.sleep(1)
    prepare = True
    while prepare:
        print("What do you do?")
        descision = int(input("""
               1) Scavenge the room for something, anything of potential use
               2) View your inventory
               3) Consume one of your potions
               4) Head into the final room
               > """))
        if descision == 2:
            viewInventory(inventory)
            time.sleep(1)
            prepare = True
        elif descision == 3:
            potionNo = 1
            potionList = []
            for potion in list(inventory["Potions"]):
                print(f"{potionNo}) {potion}")
                potionList.append(potion)
                potionNo += 1
            potionUse = int(input("\nWhich potion do you want to use?\n> ")) - 1
            potionUsed = potionList[potionUse]
            inventory, health, potionEffect = potionUpdate(inventory, potionUsed, health)
            activeEffects.append(potionEffect)
            time.sleep(1)
            prepare = True
        elif descision == 4:
            prepare = False
        elif descision == 1:
            inventory = lootTables(inventory, "r3&4")
            time.sleep(0.5)
            prepare = True
    return inventory, health, activeEffects

#This defines what happens in the final room, where you fight the bear
def dungeonFinalRoom(inventory, health, activeEffects):
    time.sleep(0.5)
    print("\nAs you walk into this final chamber, you take it all in. As far as you know, these may be the last sights you will ever see.")
    time.sleep(1.5)
    print("You see scratch marks all around the room.")
    time.sleep(1.5)
    print("And then you see it.")
    time.sleep(0.5)
    print("The creature you'd only heard rumours of. The creature that none who see live to tell the tale.")
    time.sleep(2)
    print("The Bear.")
    time.sleep(1.5)
    bearProfile = enemyProfiles("bear")
    health, inventory, activeEffects = combat(health, inventory, activeEffects, bearProfile)
    time.sleep(1)
    print("\nYou've done it? You defeated the thing that caused so many unfortunate souls to pass?")
    time.sleep(1.5)
    print("You're confused, because it was almost too ea-")
    time.sleep(0.3)
    print("It's not dead.")
    time.sleep(1)
    print("It gets up, as if awoken from its slumber. This is the foe that you had heard of.")
    time.sleep(0.5)
    print("You pray that the gods show mercy upon you.")
    time.sleep(1)
    bearFFProfile = enemyProfiles("bear final form")
    health, inventory, activeEffects = combat(health, inventory, activeEffects, bearFFProfile)
    time.sleep(1)
    print(f"You've done it! You  defeated the bear! With {health}HP left, no less!")
    time.sleep(0.5)
    print("The doors to the stairs out of the dungeon present themselves to you.")
    time.sleep(1)
    print("You are finally worthy of going back home. Back home to your family.")
    time.sleep(2)
    print("\n\nEND OF GAME")
    return inventory, health

#This defines what happens after the player has cleared the dungeon, calculates their score, and then offers the player the opportunity to play again
def postGame(inventory, health):
    print("\nWell done! You defeated the bear, and cleared the dungeon!")
    time.sleep(1)
    print("It is now time to calculate what your final score is!")
    print("Your score is calculated based upon what items you collected in your time in the dungeons, as represented by the 'Score' tag given to the items (as you would've seen in your inventory).")
    time.sleep(2)
    totalScore = 0
    #The code below decides the amount of score the player will get for all the items in their inventory
    for item in list(inventory["Weapons"].keys()):
        itemScore = inventory["Weapons"][item]["Score"]
        totalScore += itemScore
    for item in list(inventory["Armour"].keys()):
        itemScore = inventory["Armour"][item]["Score"]
        totalScore += itemScore
    for item in list(inventory["Special Items"].keys()):
        itemScore = inventory["Special Items"][item]["Score"]
        totalScore += itemScore
    for item in list(inventory["Potions"].keys()):
        itemScore = inventory["Potions"][item]["Score"] * inventory["Potions"][item]["Amount"]
        totalScore += itemScore
    goldScore = inventory["Gold"] * 2
    totalScore += goldScore
    print(f"Your total score is {totalScore}! Well Done!")
    time.sleep(1)
    playAgain = input("Would you like to play again? (y/n)\n> ")
    playAgain = playAgain.lower()
    if playAgain == "y":
        main()
    else:
        print("Okay then, see you again soon!")
        exit(0)

#The main function that calls all other functions for the game
def main():
    os.system('cls')
    baseHealth = 20
    activeEffects = []
    baseInventory = {
        "Weapons": {
            "Big Stick": {"Damage": 1, "Description": "It's a big stick", "Score": 1}
        },
        "Armour": {
            "Basic Clothes": {"Protection": 0, "Description": "Just some regular clothing", "Score": 1,
                              "Equipped": "Yes"}
        },
        "Potions": {
            "Water": {"Effect": "Hydration", "Amount": 1, "Score": 1}
        },
        "Special Items": {
            "Family Heirloom": {"Description": "You wear this to remember your family at home. Do not let them down.",
                                "Score": 5}
        },
        "Gold": 15
    }
    inventory = theForest(baseInventory, baseHealth)
    inventory, health, activeEffects = dungeonEnterance(inventory, baseHealth, activeEffects)
    inventory, health, activeEffects = dungeonFirstRoom(inventory, health, activeEffects)
    inventory, health, activeEffects = dungeonSecondRoom(inventory, health, activeEffects)
    inventory, health, activeEffects = dungeonMiddleHub(inventory, health, activeEffects)
    inventory, health, activeEffects = dungeonThirdRoom(inventory, health, activeEffects)
    inventory, health, activeEffects = dungeonFourthRoom(inventory, health, activeEffects)
    inventory, health, activeEffects = dungeonPreparationRoom(inventory, health, activeEffects)
    inventory, health = dungeonFinalRoom(inventory, health, activeEffects)
    postGame(inventory, health)

if __name__ == "__main__":
        print("Before the game starts, I just wanted to say that if you don't equip an armour set you already own if you get it again from the loot table, you will break the code!")
        input("Press ENTER if you understand and want to start the game!\n> ")
        main()
