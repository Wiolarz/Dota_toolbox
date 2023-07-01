"""This is a file to help with picking phase"""
import random

def main():
    #print("write picks a - ally e - enemy s - suggestion")

    characters = []
    hero_number = 0

    # hero [*code*, pos, type str/ag/int, power spike
    hero_names = {"pudge": {"lanes": [4], "stat": "str", "power": 1},
                  "sniper": {"lanes": [2], "stat": "ag", "power": 3},
                  "lion": {"lanes": [4, 5], "stat": "int", "power": 2},
                  "ogre": {"lanes": [4, 5], "stat": "int", "power": 1},
                  "jug": {"lanes": [1], "stat": "ag", "power": 1},
                  "pa": {"lanes": [1], "stat": "ag", "power": 2},
                  "wind": {"lanes": [2, 3, 4], "stat": "int", "power": 2},
                  "slark": {"lanes": [1], "stat": "ag", "power": 2},
                  "legion": {"lanes": [3], "stat": "str", "power": 2},
                  "wk": {"lanes": [1], "stat": "str", "power": 3},
                  "invo": {"lanes": [2], "stat": "int", "power": 2},
                  "void": {"lanes": [1], "stat": "ag", "power": 3},
                  "zeus": {"lanes": [2, 4], "stat": "int", "power": 3},
                  "shaker": {"lanes": [4, 5], "stat": "str", "power": 2},
                  "witch": {"lanes": [4, 5], "stat": "int", "power": 2},
                  "am": {"lanes": [1], "stat": "ag", "power": 3},
                  "bristle": {"lanes": [3], "stat": "str", "power": 1},
                  "qop": {"lanes": [2, 3], "stat": "int", "power": 1},
                  "cm": {"lanes": [5], "stat": "int", "power": 2},
                  "mk": {"lanes": [2], "stat": "ag","power": 1},
                  "mirana": {"lanes": [4], "stat": "ag", "power": 2},
                  "rubick": {"lanes": [4, 5], "stat": "int", "power": 2},
                  "axe": {"lanes": [3], "stat": "str", "power": 1},
                  "jajko": {"lanes": [5], "stat": "str", "power": 2},
                  "sf": {"lanes": [2], "stat": "ag", "power": 2},
                  "drow": {"lanes": [1], "stat": "ag", "power": 3},
                  "ember": {"lanes": [2], "stat": "ag", "power": 3},
                  "ursa": {"lanes": [1], "stat": "ag", "power": 2},
                  "lich": {"lanes": [5], "stat": "int", "power": 2},
                  "shaman": {"lanes": [5], "stat": "int", "power": 1},
                  "lina": {"lanes": [2, 4], "stat": "int", "power": 1},
                  "storm": {"lanes": [2], "stat": "int", "power": 3},
                  "np": {"lanes": [4], "stat": "int", "power": 3},
                  "bounty": {"lanes": [4], "stat": "ag", "power": 2},
                  "dk": {"lanes": [2,3], "stat": "str", "power": 2},
                  "blood": {"lanes": [1], "stat": "ag", "power": 2},
                  "necro": {"lanes": [2], "stat": "int", "power": 2},
                  "morph": {"lanes": [1, 2], "stat": "ag", "power": 2},
                  "distruptor": {"lanes": [5], "stat": "int", "power": 2},
                  "sky": {"lanes": [2, 4], "stat": "int", "power": 2},
                  "spectre": {"lanes": [1], "stat": "ag", "power": 3},
                  "viper": {"lanes": [2], "stat": "ag", "power": 1},
                  "riki": {"lanes": [1], "stat": "ag", "power": 2},
                  "dazzle": {"lanes": [4, 5], "stat": "int", "power": 1},
                  "luna": {"lanes": [1], "stat": "ag", "power": 3},
                  "medusa": {"lanes": [1, 2], "stat": "ag", "power": 3},
                  "pl": {"lanes": [1], "stat": "ag", "power": 3},
                  "grim": {"lanes": [4, 5], "stat": "int", "power": 3},
                  "kunka": {"lanes": [2, 3], "stat": "str", "power": 1},
                  "trol": {"lanes": [1], "stat": "ag", "power": 2},
                  "techies": {"lanes": [4], "stat": "int", "power": 1},
                  "sb": {"lanes": [4], "stat": "str", "power": 1},
                  "slardar": {"lanes": [3], "stat": "str", "power": 1},
                  "kotl": {"lanes": [5], "stat": "int", "power": 3},
                  "weaver": {"lanes": [1], "stat": "ag", "power": 3},
                  "vs": {"lanes": [2], "stat": "int", "power": 2},
                  "silencer": {"lanes": [2, 4], "stat": "int", "power": 2},
                  "aa": {"lanes": [5], "stat": "int", "power": 2},
                  "life": {"lanes": [1], "stat": "str", "power": 3},
                  "veno": {"lanes": [4], "stat": "ag", "power": 2},
                  "alch": {"lanes": [1, 2], "stat": "str", "power": 2},
                  "pango": {"lanes": [3], "stat": "ag", "power": 2},
                  "mars": {"lanes": [3], "stat": "str", "power": 2},
                  "clock": {"lanes": [3], "stat": "str", "power": 2},
                  "tide": {"lanes": [3], "stat": "str", "power": 2},
                  "clinkz": {"lanes": [2], "stat": "ag", "power": 2},
                  "pugna": {"lanes": [2, 4], "stat": "int", "power": 2},
                  "tinker": {"lanes": [2], "stat": "int", "power": 3},
                  "ta": {"lanes": [2], "stat": "ag", "power": 2},
                  "sven": {"lanes": [1], "stat": "str", "power": 3},
                  "tusk": {"lanes": [4, 5], "stat": "str", "power": 1},
                  "snap": {"lanes": [4], "stat": "str", "power": 2},
                  "penix": {"lanes": [4], "stat": "str", "power": 2},
                  "willow": {"lanes": [5], "stat": "int", "power": 2},
                  "underlord": {"lanes": [3], "stat": "str", "power": 2},
                  "warlock": {"lanes": [5], "stat": "int", "power": 3},
                  "sk": {"lanes": [3], "stat": "str", "power": 2},
                  "tiny": {"lanes": [3], "stat": "str", "power": 2},
                  "huskar": {"lanes": [2], "stat": "str", "power": 1},
                  "centaur": {"lanes": [3], "stat": "str", "power": 2},
                  "treant": {"lanes": [5], "stat": "str", "power": 1},
                  "ww": {"lanes": [5], "stat": "int", "power": 3},
                  "timber": {"lanes": [2, 3], "stat": "str", "power": 2},
                  "veng": {"lanes": [5], "stat": "ag", "power": 2},
                  "undying": {"lanes": [5], "stat": "str", "power": 2},
                  "bane": {"lanes": [4], "stat": "int", "power": 2},
                  "druid": {"lanes": [2], "stat": "ag", "power": 2},
                  "stalker": {"lanes": [3], "stat": "str", "power": 2},
                  "puck": {"lanes": [2], "stat": "int", "power": 2},
                  "gyro": {"lanes": [1], "stat": "ag", "power": 2},
                  "razor": {"lanes": [1], "stat": "ag", "power": 2},
                  "abadon": {"lanes": [4], "stat": "str", "power": 2},
                  "ck": {"lanes": [1], "stat": "str", "power": 2},
                  "od": {"lanes": [2], "stat": "int", "power": 2},
                  "beast": {"lanes": [3], "stat": "str", "power": 2},
                  "terror": {"lanes": [1], "stat": "ag", "power": 2},
                  "enchantress": {"lanes": [4], "stat": "int", "power": 2},
                  "demon": {"lanes": [5], "stat": "int", "power": 2},
                  "enigma": {"lanes": [5], "stat": "int", "power": 2},
                  "magnus": {"lanes": [3], "stat": "str", "power": 2},
                  "nyx": {"lanes": [4], "stat": "ag", "power": 2},
                  "doom": {"lanes": [3], "stat": "str", "power": 2},
                  "oracle": {"lanes": [5], "stat": "int", "power": 2},
                  "dp": {"lanes": [2], "stat": "int", "power": 2},
                  "es": {"lanes": [4, 5], "stat": "str", "power": 2},
                  "lycan": {"lanes": [1, 3], "stat": "str", "power": 2},
                  "naga": {"lanes": [1], "stat": "ag", "power": 2},
                  "meppo": {"lanes": [2], "stat": "ag", "power": 2},
                  "io": {"lanes": [5], "stat": "str", "power": 2},
                  "omni": {"lanes": [3, 4, 5], "stat": "str", "power": 2},
                  "bat": {"lanes": [3, 4], "stat": "int", "power": 2},
                  "titan": {"lanes": [5], "stat": "str", "power": 2},
                  "leshrac": {"lanes": [2], "stat": "int", "power": 2},
                  "seer": {"lanes": [5], "stat": "int", "power": 2},
                  "arc": {"lanes": [2], "stat": "ag", "power": 2},
                  "brood": {"lanes": [2], "stat": "ag", "power": 2},
                  "brew": {"lanes": [3], "stat": "str", "power": 2},
                  "visage": {"lanes": [2], "stat": "int", "power": 2},
                  "chen": {"lanes": [5], "stat": "int", "power": 2}}
    names = hero_names.keys()
    names = list(names)
    x = random.randint(0, len(names))
    print(names[x], len(names))


    def analysis(heroes):
        if len(heroes) == 0:
            print("good opening supports:")
            print("cm, phoenix, grim, kotl")
            return 0
        print("")

        # sorting
        ally = []
        enemy = []
        suggestion = []
        for i in heroes:
            if i["type"] == "a":
                ally.append(i)
            elif i["type"] == "e":
                enemy.append(i)
            else:
                suggestion.append(i)


        if len(enemy) > 0:
            print("anal of e")
            enemy_force = [0, 0, 0, 0]
            enemy_stats = [0, 0, 0, 0]

            for i in enemy:

                #print(i["power"])
                if i["power"] == 1:
                    enemy_force[0] += 1
                elif i["power"] == 2:
                    #print("succes")
                    enemy_force[1] += 1
                else:
                    enemy_force[2] += 1
                print(enemy_force)

                if enemy_force[0] > enemy_force[1] and enemy_force[0] > enemy_force[2]:
                    enemy_force[3] = 1
                elif enemy_force[1] > enemy_force[0] and enemy_force[1] > enemy_force[2]:
                    enemy_force[3] = 2
                    #print("succes 2")
                else:
                    enemy_force[3] = 3

                if i["stat"] == "str":
                    enemy_stats[0] += 1
                elif i["stat"] == "ag":
                    enemy_stats[1] += 1
                else:
                    enemy_stats[2] += 1
                if enemy_stats[0] > enemy_stats[1] and enemy_stats[0] > enemy_stats[2]:
                    enemy_stats[3] = 1
                elif enemy_stats[1] > enemy_stats[0] and enemy_stats[0] > enemy_stats[2]:
                    enemy_stats[3] = 2
                else:
                    enemy_stats[3] = 3

            print("enemy stats:", enemy_stats)
            print("enemy force:", enemy_force)

        if len(ally) > 0:
            print("analysis of a")
            ally_force = [0, 0, 0]
            for i in enemy:
                if i["power"] == 1:
                    ally_force[0] += 1
                elif i["power"] == 2:
                    ally_force[1] += 1
                else:
                    ally_force[2] += 1
            print("ally force:", ally_force)



        if len(suggestion) > 0:
            print("analysis of s")

            for i in suggestion:
                print(i["name"], end=" ")
                if i["power"] < enemy_force[3]:
                    print("better early")
                elif i["power"] > enemy_force[3]:
                    print("better late")
                else:  # if i[4] < enemy_force[3]:
                    print("same level")






    #print(hero_names["dk"])
    '''
    while hero_number < 5:
        propername = False
        while not propername:
            print("input hero:")
            hero = input()
            if hero[2:] in hero_names.keys():
                characters.append(hero_names[hero[2:]])
                propername = True
            else:
                print("wrong name:", hero)


        if hero[0] == "a":
            characters[len(characters)-1].update({"type": "a"})
            hero_number += 1
        elif hero[0] == "e":
            characters[len(characters) - 1].update({"type": "e"})
            hero_number += 1
        else:  # hero[0] == "s":
            characters[len(characters) - 1].update({"type": "s"})
        characters[-1].update({"name": hero[2:]})
        analysis(characters)

        for i in characters:
            print(i)
    '''


if __name__ == '__main__':
    main()



