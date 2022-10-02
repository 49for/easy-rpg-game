from ast import If
import random as r

hp = 0
coins = 0
damage = 0

def printParameters():
    print("У тебя {0} жизней, {1} урона и {2} монет.".format(hp, damage, coins))

def printHp():
    print("У тебя", hp, "жизней.")

def printCoins():
    print("У тебя", coins, "монет.")

def printDamage():
    print("У тебя", damage, "урона.")

def meetShop():
    global hp
    global damage
    global coins

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("У тебя маловато монет!")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    weapons = ["AK-47", "Iron Sword", "Showel", "Flower", "Bow", "Fish"]
    weaponRarities = ["Spoiled", "Rare", "Legendary"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12

    print("На пути тебе встретился торговец!")
    printParameters()
    
    while input("Что ты будешь делать (зайти/уйти): ").lower() == "зайти":
        print("1) Одна единица здоровья -", oneHpCost, "монет;")
        print("2) Три единицы здоровья -", threeHpCost, "монет;")
        print("3) {0} {1} - {2} монет".format(weaponRarity, weapon, weaponCost))

        choice = input("Что хочешь приобрести: ")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print("Я такое не продаю.")

def meetMonster():
    global hp
    global coins

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Grock", "Clop", "Cholop", "Madrock", "Lilbitch"]

    monster = r.choice(monsters)

    print("Ты набрел на монстра - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("Что будешь делать (атака/бег): ").lower()

        if choice == "атака":
            monsterHp -= damage
            print("Ты атаковал монстра и у него осталось", monsterHp, "жизней.")
        elif choice == "бег":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр оказался чересчур сильным и догнал тебя...")
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            print("Монстр атаковал и у тебя осталось", hp, "жизней.")
        
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        coins += loot
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет.")
        printCoins()


def meetTown():
    global hp
    global damage
    global coins

    town = r.randint(0, 3)

    if town == 0:
        town0 = input("На твоём пути небольшая деревушка, что будешь делать? (отдохнуть / идти дальше): ")
        if town0 == "отдохнуть":
            hp += 1
            print("Добрая старушка решила впустить тебя переночевать и сытно накормила")
            printHp()
        else:
            print("Ты решаешся продолжить своё путешевствие.")
        
    elif town == 1:
        town1 = input("Ты встретил аванпост рыцарей, что будешь делать? (пройти мимо / заплатить за отдых): ")
        if town1 == "заплатить за отдых":
            hp +=1
            coins -=2
            print("Солдаты согласились впустить тебя на ночлег.")
            printParameters()
        else:
            print(" 'Монеты всегда стоит сохранять,' думаешь ты, уходя от аванпоста")

    elif town == 3:
        town3 = input("Ты наткнулся на большой город, каковы твои действия? (зайти / продолжить путешевствие): ")
        if town3 == "зайти":
            print("пройдя проверку тебя впускают в город")
            townsit = r.randint(0, 2)               
                
            if townsit == 0:
                    hp +=1
                    coins -=1
                    print("Ты нашёл место для ночлега за небольшую плату")

                    printParameters()

            elif townsit == 1:
                    bar = input ("Прогуливаясь по городу ты увидел бордель (зайти / пройти мимо): ")
                    if bar == "зайти":
                        hp +=2
                        coins -=2
                        print ("После недолгих раздумий ты решаешь зайти...")
                        printParameters()
                    else:
                        print ("Ты решаешь сохранить свои сбережения.")
            elif townsit == 2:
                    grab = r.randint(0,2)
                    if grab == 0: 
                     hp -=1
                     coins -=3
                     print("Зайдя за переулок тебя вырубают грабители,проснувшись ты обнаружил пропажу денег")
                     printParameters()
                    else:
                        cash = r.randint(1,5)
                        print("Тебе удаётся отбится и заработать немного монет")

                        coins += cash
                        printParameters()
        else:
            print("Ты решаешь не прерывать своё путешевствие.")
            printParameters()

                    

def initGame(initHp, initCoins, initDamage):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDamage

    print("Ты отправился в странствие навстречу приключениям и опасностям. Удачного путешествия!")
    printParameters()

def gameLoop():
    situation = r.randint(0, 4)

    if situation == 0:
        meetShop()
    elif situation == 1:
        meetMonster()
    elif situation == 2:
        meetTown() 

    else:
        input("Блуждаем...")

initGame(3, 5, 1)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(3, 5, 1)
        else:
            break