""" This is an updated version of my dota items calculator, it's mostly only a refactor"""

import copy  # TODO check why this import exists

def data():
    """statistics of an DK hero
        [Sila, Zrecznosc, sredni base attack, BAT basic attack time, IAS initial attack speed]
        #s 19 - 118 3.4 per lvl
        #z 19 - 77 2.0 per lvl
        hero can have a level from a range of 1 - 30 so his statistics may be updated even 29 times

        #   53
        """
    dk = {"MAIN": "STR", "STR": 118 + 25, "INT": 0, "ZR": 77, "ATK": 53 + 30, "BAT": 1.7, "IAS": 100}  # dmg

    """
    Data base for items doesn't contain:
    spell amplification, gold cost, effects, health and mana changes
    this is a very old dota items data sets so some items and their balance changes are not present
    """

    itemy = [{"value": 25, "type": "int"},  # mystic staff
             # {"value": 140, "type": "spd"}, #moonshard
             {"value": 20, "type": "spd"},  # gloves of haste
             # {"value": 330, "type": "dmg"},  #divine
             {"value": 24, "type": "dmg"},  # mithril hammer
             {"value": 10, "type": "dmg", "value2": 10, "type": "spd"},  # quaterstaff
             {"value": 60, "type": "dmg"},  # sacred relic
             {"value": 42, "type": "dmg"},  # demon edge
             {"value": 25, "type": "str"},  # reaver
             {"value": 25, "type": "zr"},  # eagle song
             {"value": 55, "type": "spd"},  # hyperstone
             {"value": 10, "type": "str", "value2": 10, "type2": "zr", "value3": 10, "type3": "int"},  # ultimate orb
             {"value": 12, "type": "str", "value2": 12, "type2": "zr", },  # dragon lnace
             {"value": 16, "type": "str"},  # sange
             {"value": 16, "type": "zr", "value2": 12, "type2": "spd"},  # yasha
             # {"value": 16, "type": "int"}, #kaya
             {"value": 16, "type": "str", "value2": 16, "type2": "zr", "value3": 12, "type3": "spd"},  # sange and yasha
             {"value": 16, "type": "str", "value2": 16, "type2": "int"},  # sange and kaya
             {"value": 16, "type": "zr", "value2": 12, "type2": "spd", "value3": 16, "type3": "int"},  # yasha and kaya
             {"value": 15, "type": "dmg", "value2": 12, "type2": "str", "value3": 10, "type3": "int", "value4": 10,
              "type4": "spd"},  # echo sabre
             {"value": 24, "type": "dmg"},  # mealstorm
             {"value": 24, "type": "dmg", "value2": 65, "type2": "spd"},  # mjolnir
             {"value": 25, "type": "dmg", "value2": 25, "type2": "str"},  # satanic
             {"value": 25, "type": "str", "value2": 25, "type2": "zr", "value3": 25, "type3": "int"},  # eye of skadi
             {"value": 60, "type": "dmg", "value2": 8, "type2": "armour"},  # desolator
             {"value": 2, "type": "armour"},  # blight stone
             {"value": 20, "type": "str"},  # halbarda
             {"value": 20, "type": "zr", "value2": 10, "type2": "int"},
             {"value": 34, "type": "dmg"},  # crystalys
             {"value": 46, "type": "dmg", "value2": 25, "type2": "str", "value3": 25, "type3": "spd"},  # armlet
             {"value": 12, "type": "str", "value2": 12, "type2": "int"},  # meteor
             {"value": 27, "type": "dmg", "value2": 30, "type2": "spd"},  # shadowblade
             {"value": 25, "type": "dmg", "value2": 10, "type2": "str"},  # basher
             {"value": 60, "type": "dmg"},  # battle fury
             {"value": 40, "type": "zr", "value2": 10, "type2": "str", "value3": 10, "type3": "int"},  # eblade
             {"value": 60, "type": "dmg"},  # radi
             {"value": 88, "type": "dmg"},  # dedalus
             {"value": 30, "type": "zr", "value2": 25, "type2": "dmg", "value3": 30, "type3": "spd"},  # butterfly
             {"value": 45, "type": "dmg", "value2": 30, "type2": "spd", "value3": 15, "type3": "str", "value4": 15,
              "type4": "zr", "value5": 15, "type5": "int"},  # silver edge
             {"value": 10, "type": "str", "value2": 25, "type2": "dmg"},  # abysal
             {"value": 25, "type": "int", "value2": 85, "type2": "spd", "value3": 30, "type3": "dmg"},  # bloddthorn
             {"value": 55, "type": "spd", "value2": 5, "type2": "str", "value3": 5, "type3": "zr", "value4": 5,
              "type4": "armour"},  # assault
             {"value": 45, "type": "str"},  # hart
             {"value": 12, "type": "spd", "value2": 10, "type2": "str", "value3": 26, "type3": "zr", "value4": 10,
              "type4": "int"},  # manta
             {"value": 14, "type": "str", "value2": 14, "type2": "zr", "value3": 14, "type3": "int"},  # linken
             {"value": 15, "type": "str", "value2": 20, "type2": "zr", "value3": 13, "type3": "int"},  # huracane
             {"value": 24, "type": "dmg", "value2": 10, "type2": "str"},  # bkb
             {"value": 3, "type": "str", "value2": 3, "type2": "zr", "value3": 3, "type3": "int"},  # crimson guard
             {"value": 28, "type": "dmg", "value2": 8, "type2": "int"},  # blademail
             {"value": 9, "type": "str", "value2": 9, "type2": "zr", "value3": 9, "type3": "int"},  # veil
             {"value": 20, "type": "spd"},  # glimer
             {"value": 25, "type": "dmg", "value2": 25, "type2": "str"},  # satanic
             {"value": 10, "type": "str", "value2": 10, "type2": "zr", "value3": 10, "type3": "int", "value4": 8,
              "type4": "armour"},  # solarcrest
             {"value": 30, "type": "dmg", "value2": 30, "type2": "spd", "value3": 25, "type3": "int"},  # orchid
             {"value": 5, "type": "str", "value2": 5, "type2": "zr", "value3": 5, "type3": "int"},  # grave
             {"value": 10, "type": "str"},  # ogre
             {"value": 10, "type": "zr"},  # blade
             {"value": 80, "type": "dmg"}]  # nulifiler

    itemyyyyy = [{"value": 25, "type": "int"},  # mystic staff
                 {"value": 140, "type": "spd"},  # moonshard
                 {"value": 20, "type": "spd"},  # gloves of haste
                 {"value": 330, "type": "dmg"},  # divine
                 {"value": 16, "type": "dmg"},  # broadsword
                 {"value": 24, "type": "dmg"},  # mithril hammer
                 {"value": 9, "type": "dmg"},  # blades of attack
                 {"value": 21, "type": "dmg"},  # claymore
                 {"value": 10, "type": "dmg", "value2": 10, "type": "spd"},  # quaterstaff
                 {"value": 60, "type": "dmg"},  # sacred relic
                 {"value": 42, "type": "dmg"},  # demon edge
                 {"value": 25, "type": "str"},  # reaver
                 {"value": 25, "type": "zr"},  # eagle song
                 {"value": 55, "type": "spd"},  # hyperstone
                 {"value": 10, "type": "str", "value2": 10, "type2": "zr", "value3": 10, "type3": "int"},
                 # ultimate orb
                 {"value": 12, "type": "str", "value2": 12, "type2": "zr", },  # dragon lnace
                 {"value": 16, "type": "str"},  # sange
                 {"value": 16, "type": "zr", "value2": 12, "type2": "spd"},  # yasha
                 # {"value": 16, "type": "int"}, #kaya
                 {"value": 16, "type": "str", "value2": 16, "type2": "zr", "value3": 12, "type3": "spd"},
                 # sange and yasha
                 {"value": 16, "type": "str", "value2": 16, "type2": "int"},  # sange and kaya
                 {"value": 16, "type": "zr", "value2": 12, "type2": "spd", "value3": 16, "type3": "int"},
                 # yasha and kaya
                 {"value": 15, "type": "dmg", "value2": 12, "type2": "str", "value3": 10, "type3": "int", "value4": 10,
                  "type4": "spd"},  # echo sabre
                 {"value": 24, "type": "dmg"},  # mealstorm
                 {"value": 24, "type": "dmg", "value2": 65, "type2": "spd"},  # mjolnir
                 {"value": 25, "type": "dmg", "value2": 25, "type2": "str"},  # satanic
                 {"value": 25, "type": "str", "value2": 25, "type2": "zr", "value3": 25, "type3": "int"},
                 # eye of skadi
                 {"value": 60, "type": "dmg", "value2": 8, "type2": "armour"},  # desolator
                 {"value": 2, "type": "armour"},  # blight stone
                 {"value": 20, "type": "str"},  # halbarda
                 {"value": 20, "type": "zr", "value2": 10, "type2": "int"},
                 {"value": 34, "type": "dmg"},  # crystalys
                 {"value": 46, "type": "dmg", "value2": 25, "type2": "str", "value3": 25, "type3": "spd"},  # armlet
                 {"value": 12, "type": "str", "value2": 12, "type2": "int"},  # meteor
                 {"value": 27, "type": "dmg", "value2": 30, "type2": "spd"},  # shadowblade
                 {"value": 25, "type": "dmg", "value2": 10, "type2": "str"},  # basher
                 {"value": 60, "type": "dmg"},  # battle fury
                 {"value": 40, "type": "zr", "value2": 10, "type2": "str", "value3": 10, "type3": "int"},  # eblade
                 {"value": 60, "type": "dmg"},  # radi
                 {"value": 88, "type": "dmg"},  # dedalus
                 {"value": 30, "type": "zr", "value2": 25, "type2": "dmg", "value3": 30, "type3": "spd"},  # butterfly
                 {"value": 45, "type": "dmg", "value2": 30, "type2": "spd", "value3": 15, "type3": "str", "value4": 15,
                  "type4": "zr", "value5": 15, "type5": "int"},  # silver edge
                 {"value": 10, "type": "str", "value2": 25, "type2": "dmg"},  # abysal
                 {"value": 25, "type": "int", "value2": 85, "type2": "spd", "value3": 30, "type3": "dmg"},  # bloddthorn
                 {"value": 30, "type": "spd", "value2": 5, "type2": "str", "value3": 5, "type3": "zr", "value4": 5,
                  "type4": "int"},  # assault
                 {"value": 45, "type": "str"},  # hart
                 {"value": 12, "type": "spd", "value2": 10, "type2": "str", "value3": 26, "type3": "zr", "value4": 10,
                  "type4": "int"},  # manta
                 # {"value": 16, "type": "int"},  #bloddstone
                 {"value": 14, "type": "str", "value2": 14, "type2": "zr", "value3": 14, "type3": "int"},  # linken
                 {"value": 15, "type": "str", "value2": 20, "type2": "zr", "value3": 13, "type3": "int"},  # huracane
                 # {"value": 30, "type": "int"}, #shiva
                 {"value": 24, "type": "dmg", "value2": 10, "type2": "str"},  # bkb
                 {"value": 3, "type": "str", "value2": 3, "type2": "zr", "value3": 3, "type3": "int"},  # crimson guard
                 {"value": 28, "type": "dmg", "value2": 8, "type2": "int"},  # blademail
                 {"value": 9, "type": "str", "value2": 9, "type2": "zr", "value3": 9, "type3": "int"},  # veil
                 {"value": 20, "type": "spd"},  # glimer
                 # {"value": 10, "type": "int"},  # forcestaff
                 # {"value": 10, "type": "int"},  # eul
                 {"value": 25, "type": "dmg", "value2": 25, "type2": "str"},  # satanic
                 {"value": 10, "type": "str", "value2": 10, "type2": "zr", "value3": 10, "type3": "int"},  # solarcrest
                 {"value": 10, "type": "str", "value2": 10, "type2": "zr", "value3": 20, "type3": "int"},  # atos
                 {"value": 30, "type": "dmg", "value2": 30, "type2": "spd", "value3": 25, "type3": "int"},  # orchid
                 {"value": 10, "type": "str", "value2": 10, "type2": "zr", "value3": 20, "type3": "int"},  # aganim
                 {"value": 10, "type": "str", "value2": 10, "type2": "zr", "value3": 35, "type3": "int"},  # scythe
                 {"value": 5, "type": "str", "value2": 5, "type2": "zr", "value3": 5, "type3": "int"},  # graves
                 {"value": 5, "type": "str", "value2": 5, "type2": "zr", "value3": 5, "type3": "int"},  # ghost scepter
                 {"value": 5, "type": "str", "value2": 5, "type2": "zr", "value3": 5, "type3": "int"},  # vladek
                 {"value": 3, "type": "str", "value2": 3, "type2": "zr", "value3": 3, "type3": "int"},  # holylocket
                 {"value": 3, "type": "str", "value2": 3, "type2": "zr", "value3": 3, "type3": "int"},  # magic wand
                 {"value": 2, "type": "str", "value2": 2, "type2": "zr", "value3": 2, "type3": "int"},  # spiritvessel
                 {"value": 2, "type": "str", "value2": 2, "type2": "zr", "value3": 2, "type3": "int"},  # urna
                 {"value": 4, "type": "str", "value2": 4, "type2": "zr", "value3": 4, "type3": "int"},  # mekanism
                 {"value": 4, "type": "str", "value2": 4, "type2": "zr", "value3": 4, "type3": "int"},  # drumy
                 {"value": 1, "type": "str", "value2": 1, "type2": "zr", "value3": 1, "type3": "int"},  # tree
                 {"value": 2, "type": "str", "value2": 2, "type2": "zr", "value3": 2, "type3": "int"},  # cirlet
                 {"value": 4, "type": "str", "value2": 4, "type2": "zr", "value3": 4, "type3": "int"},  # crown
                 {"value": 3, "type": "str"},  # gaountler
                 {"value": 3, "type": "zr"},  # sliper
                 # {"value": 3, "type": "int"}, #mantle
                 {"value": 6, "type": "str"},  # belt
                 {"value": 6, "type": "zr"},  # sliper
                 # {"value": 6, "type": "int"}, #robe
                 {"value": 10, "type": "str"},  # ogre
                 {"value": 10, "type": "zr"},  # blade
                 # {"value": 10, "type": "int"}, #staff
                 {"value": 80, "type": "dmg"}]  # nulifiler
    # {"value": 25, "type": "int"}] #octarine
    return dk, itemy, itemyyyyy


def defense(dmg, armour):
    x = 1 - (0.052 * armour) / (0.9 + 0.048 * abs(armour))
    x = dmg * x
    return x

def speed(agility, bat, ias):
    aa = agility + ias
    #print(aa)
    if(aa > 700):
        aa = 700
    x = (aa * 0.01) / bat  #dps
    #z = 0.5 / (1 + ias)
    #y = 1 / x #attack time
    return x

def dmg(mainstat, base):
    x = mainstat + base
    return x

def dps(speed, dmg):
    x = speed * dmg
    return x




def item(numer, postac):
    # 5 types
    typ = numer["type"]
    if(typ == "spd"):
        postac.speed(numer["value"])
    if (typ == "dmg"):
        postac.dmg(numer["value"])
    if (typ == "str"):
        postac.stats(numer["value"], "STR")
    if (typ == "zr"):
        postac.stats(numer["value"], "ZR")
    if (typ == "int"):
        postac.stats(numer["value"], "INT")
    if (typ == "armour"):
        postac.armour(numer["value"])
    if "type2" in numer:
        typ2 = numer["type2"]
        if (typ2 == "spd"):
            postac.speed(numer["value"])
        if (typ2 == "dmg"):
            postac.dmg(numer["value"])
        if (typ2 == "str"):
            postac.stats(numer["value"], "STR")
        if (typ2 == "zr"):
            postac.stats(numer["value"], "ZR")
        if (typ2 == "int"):
            postac.stats(numer["value"], "INT")
        if (typ2 == "armour"):
            postac.armour(numer["value"])
    else:
        return
    if "type3" in numer:
        typ3 = numer["type3"]
        if(typ3 == "spd"):
            postac.speed(numer["value"])
        if (typ3 == "dmg"):
            postac.dmg(numer["value"])
        if (typ3 == "str"):
            postac.stats(numer["value"], "STR")
        if (typ3 == "zr"):
            postac.stats(numer["value"], "ZR")
        if (typ3 == "int"):
            postac.stats(numer["value"], "INT")
        if (typ3 == "armour"):
            postac.armour(numer["value"])
    else:
        return
    if "type4" in numer:
        typ4 = numer["type4"]
        if(typ4 == "spd"):
            postac.speed(numer["value"])
        if (typ4 == "dmg"):
            postac.dmg(numer["value"])
        if (typ4 == "str"):
            postac.stats(numer["value"], "STR")
        if (typ4 == "zr"):
            postac.stats(numer["value"], "ZR")
        if (typ4 == "int"):
            postac.stats(numer["value"], "INT")
        if (typ4 == "armour"):
            postac.armour(numer["value"])
    else:
        return
    if "type5" in numer:
        typ5 = numer["type5"]
        if(typ5 == "spd"):
            postac.speed(numer["value"])
        if (typ5 == "dmg"):
            postac.dmg(numer["value"])
        if (typ5 == "str"):
            postac.stats(numer["value"], "STR")
        if (typ5 == "zr"):
            postac.stats(numer["value"], "ZR")
        if (typ5 == "int"):
            postac.stats(numer["value"], "INT")
        if (typ5 == "armour"):
            postac.armour(numer["value"])


    #if(numer["num"] > 1):



class Hero:
    def __init__(self, stats):
        self.statistics = stats
        #self.hp = 5

        if(stats["MAIN"] == "STR"):
            a = stats["STR"]
        elif (stats["MAIN"] == "ZR"):
            a = stats["ZR"]
        elif (stats["MAIN"] == "INT"):
            a = stats["INT"]

        self.reduction = 0

        self.mainstat = a
        self.baseattack = stats["ATK"]

        self.agility = stats["ZR"]
        self.bat = stats["BAT"]
        self.ias = stats["IAS"]

    def dmg(self, dmg):
        self.baseattack += dmg

    def speed(self, speed):
        self.agility += speed
    
    def stats(self, num, type):
        if (self.statistics["MAIN"] == 1 and type == "STR"):
            self.mainstat += num
        if (self.statistics["MAIN"] == 2 and type == "ZR"):
            self.agility += num
            self.mainstat += num
        if (self.statistics["MAIN"] == 3 and type == "INT"):
            self.mainstat += num

    def armour(self, num):
        self.reduction += num


def item_test():
    counter = 0  # debug value

    dk, itemy, itemyyyyy = data()

    # there are 86 items

    z = [0 for x in range(6)]

    max_dps = 0  # biggest dps value

    min_dps = 1000  # smallest dps value

    dragon0 = Hero(dk)

    while True:
        dragon = copy.copy(dragon0)
        for i in range(6):  # podstawiac kolejne przedmioty z listy
            item(itemy[z[i]], dragon)

        a = speed(dragon.agility, dragon.bat, dragon.ias)
        b = dmg(dragon.mainstat, dragon.baseattack)
        # print("speed:", a)
        # print("dmg:", b)
        # print(speed(dragon.agility,dragon.bat, dragon.ias))
        d = dps(a, b)
        if max_dps < d:
            max_dps = d
            maxz = tuple(z)
        if min_dps > d:
            min_dps = d
            minz = tuple(z)

        if counter % 500000 == 0:  # printing live updates of program results
            # z[0] == 0 and z[1] == 0:
            print("\r%2d %2d %2d %2d %2d %2d = min %7.2f" % (
                minz[0], minz[1], minz[2], minz[3], minz[4], minz[5], min_dps), end='')
            print("  %2d %2d %2d %2d %2d %2d = cur %7.2f" % (z[0], z[1], z[2], z[3], z[4], z[5], d), end='')
            print("  %2d %2d %2d %2d %2d %2d = max %7.2f" % (
                maxz[0], maxz[1], maxz[2], maxz[3], maxz[4], maxz[5], max_dps), end='')
        counter += 1

        for i in range(6):
            if z[i] < len(itemy) - 1 - i:
                z[i] += 1
                break
            else:
                if i < 5:
                    for j in range(i + 1):
                        z[j] = z[i + 1] + 1
        else:
            break

    print("\n", "min dps:", min_dps, "max dps:", max_dps, "   end")  # final result

def new_tests():
    for sp in [0, 10, 20, 30, 40, 50]:
        for ag in [0, 10, 20, 30, 40, 50, 60, 70]:
            spd = speed(ag + 53 + sp, 1.7, 100)
            final_dmg = 60 + ag + 53
            final_dps = spd * final_dmg
            print("sp: ", sp, " ag: ", ag, " dps:", final_dps)


if __name__ == '__main__':
    print("start")
    item_test()


