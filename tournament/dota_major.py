"""
Program aims to showcase the chances each dota 2 team has in getting a direct invite to "TI" by points.
"""

from itertools import permutations
import time

teams_2022 = {
    "thunder": 1540,
    "lgd": 1500,
    "tsm": 1380,
    "og": 1340,
    "beastcoast": 1295,
    "tundra": 1212,
    "gladiators": 1130,
    "boom": 1122.5,
    "EG": 1052.5,
    "fnatic": 1020,
    "spirit": 990,
    "aster": 940,
    "liquid": 890,
    "rng": 738.42,
    "outsiders": 660.05,
    "quincy": 582.49,
    "navi": 341.67,
    "talon": 300,
    "entity": 100
}

teams_2023 = {
        "liquid": 1600,
        "gladiators": 1540,
        "eg": 1470,
        "shopify": 1170,
        "tundra": 1160,
        "talon": 1120,
        "9pandas": 1096,
        "spirit": 1020,
        "tsm": 900,
        "lgd": 884,
        "beastcoast": 800,
        "betboom": 760,
        "execration": 740,
        "aster": 608,
        "nouns": 580,
        "bleed": 500,
        "ig": 460,
        "blacklist": 380,
        "quest": 232,
        "azure": 100
        }



major_teams_2023 = ["beastcoast", "blacklist", "execration", "ig", "shopify", "aster", "liquid", "spirit", "tundra",
                    "9pandas", "azure", "betboom", "bleed", "eg", "gladiators", "nouns", "lgd", "quest"]

major_teams_2022 = ["tundra", "og", "liquid", "entity", "spirit", "navi", "outsiders", "rng", "aster", "lgd",
               "boom", "talon", "fnatic", "EG", "quincy", "thunder", "beastcoast"]

A = ["beastcoast", "blacklist", "execration", "ig", "shopify", "aster", "liquid", "spirit", "tundra"]
B = ["9pandas", "azure", "betboom", "bleed", "eg", "gladiators", "nouns", "lgd", "quest"]


major_points_2022 = [820, 740, 670, 590, 515, 515, 360, 360]
major_points_2023 = [600, 550, 500, 450, 400, 400, 300, 300]


major_2022 = {"global_teams": teams_2022, "major_teams": major_teams_2022, "points": major_points_2022}
major_2023 = {"global_teams": teams_2023, "major_teams": major_teams_2023, "points": major_points_2023}
current_major = major_2023

teams = current_major["global_teams"]
major_teams = current_major["major_teams"]
major_points = current_major["points"]  # points for places from 1-8 5/6 and 7/8 have the same value in the input data





def direct_TI():
    """
    Get list of 12 teams that will be directly invited to TI
    :return list of 12 best teams, contains dictionary elements? TODO verify with debugger:
    """
    def team_score(team):
        """ Method for sort function"""
        return teams[team]
    top_12 = []
    for team in teams:
        top_12.append(team)
    top_12.sort(reverse=True, key=team_score)
    top_12 = top_12[:12]
    return top_12
    #print(top_12)


def permutation():
    """
    Creation of every possible results state. Then comparing number occurrences of being in top 12 by a team
    :return:
    """
    print(time.ctime())
    global teams
    teams_copy = teams.copy()
    perm_list = permutations(major_teams, 8)
    leng = 0
    rankings = {}
    for team in teams:
        rankings[team] = 0
    for perm in perm_list:
        leng += 1

        if leng % 1000000 == 0:  # DEBUG
            progress = leng / 980179200  # TODO fix magic number, it's a value of total possible combinations from 2022
            print("{:2.2%}".format(progress), end="   ")
            print(time.ctime())

        for i, team in enumerate(perm):
            teams[team] += major_points[i]
        top = direct_TI()
        for team in top:
            rankings[team] += 1

        teams = teams_copy.copy()
    print(rankings)

def what_team_needs(team_name="liquid"):
    """
    After providing team name, program provides the user with teams placements needed to get invite

    Contains bugs beascoast score is not correct
    :return:
    """
    for team_name in major_teams:
        print("\n")
        print(team_name)
        if team_name == "boom":
            print()
        points = [major_points[x] for x in [7, 5, 3, 2, 1, 0]]
        points.insert(0, 0)  # first position in array represent not getting points

        for place, team_placement in enumerate(points):  # 0 first place 5 "5-6" 7 "7-8"
            score = teams[team_name] + team_placement
            stronger_teams = []
            for enemy_team in teams:
                min_place = None
                if enemy_team in ["thunder", "lgd", "tsm", "og", "entity"]:
                    continue

                for i, enemy_result in enumerate(points):
                    if (i == place and i != 0) and i not in [5, 7]:  # don't calculate the same placements
                        continue
                    enemy_score = teams[enemy_team] + enemy_result
                    if enemy_score > score:
                        stronger_teams.append([enemy_team, i])
                        break

            # LIST IS FINISHED
            sum_of_placements = {6: 1, 5: 2, 4: 3, 3: 4, 2: 6, 1: 8}
            wrong_teams = []
            for id, better_team in enumerate(stronger_teams):
                if better_team[1] in sum_of_placements.keys():
                    for spot in range(better_team[1], 0, -1):
                        if sum_of_placements[spot] == 0:
                            wrong_teams.append(better_team)
                            break
                        sum_of_placements[spot] -= 1


            number_of_any_teams = 0
            for team in stronger_teams:
                if team[1] == 0:
                    number_of_any_teams += 1

            # OUTPUT
            placement_translator = ["any", "TOP-8", "TOP-6", "TOP-4", "TOP-3", "TOP-2", "TOP-1"]
            if number_of_any_teams >= 8:
                print(placement_translator[place], "defeat")
            elif len(stronger_teams) - len(wrong_teams) > 8:
                print(placement_translator[place], end=" ")
                for team in stronger_teams:

                    print("|", team[0],"_", placement_translator[team[1]], sep="", end="|  ")
                print()
            else:
                print(placement_translator[place], "success")
                break

def draw_test():
    """
    Test to check if there could be a draws in points between teams
    :return:
    """
    points = [major_points[x] for x in [0, 1, 2, 3, 4, 5, 7]]

    for team in major_teams:
        for place, score in enumerate(points):
            test_score = teams[team] + score
            for enemy_team in major_teams:

                for i, e_score in enumerate(points):
                    if i == place and i not in [5, 7]:  # don't calculate the same placements
                        continue
                    enemy_score = teams[enemy_team] + e_score
                    if enemy_team == team:
                        continue
                    if test_score == enemy_score:
                        print(test_score, team, place, enemy_team, i)


def final_score():
    ''' first 6 places get points
    score = {'thunder': 13366080, 'lgd': 13366080, 'tsm': 13366080, 'og': 13366080, 'beastcoast': 13366080,
             'tundra': 13366080, 'gladiators': 13302576, 'boom': 12986532, 'EG': 11432640, 'fnatic': 8847160,
             'spirit': 6527736, 'aster': 4870080, 'liquid': 4455360, 'rng': 4378242, 'outsiders': 4166860,
             'quincy': 3687522, 'extreme': 2689268, 'navi': 1615882, 'talon': 1236622, 'entity': 0}
    '''
    ''' before xtreme canceled
    score = {'thunder': 1764322560, 'lgd': 1764322560, 'tsm': 1764322560, 'og': 1764322560, 'beastcoast': 1764207360,
             'tundra': 1760751360, 'gladiators': 1669264848, 'boom': 1595864520, 'EG': 1308097440, 'fnatic': 1045013760,
             'spirit': 893829888, 'aster': 799384320, 'liquid': 783999360, 'rng': 726038592, 'outsiders': 657040032,
             'quincy': 526066704, 'extreme': 305309712, 'navi': 168019416, 'talon': 111693168, 'entity': 0}
    '''
    score_2022 = {'thunder': 980179200, 'lgd': 980179200, 'tsm': 980179200, 'og': 980179200, 'beastcoast': 980064000,
              'tundra': 977698800, 'gladiators': 920985600, 'boom': 882297600, 'EG': 733770240, 'fnatic': 603771840,
              'spirit': 522678240, 'aster': 472147200, 'liquid': 461152800, 'rng': 427680000, 'outsiders': 388970640,
              'quincy': 311105760, 'navi': 96852480, 'talon': 62258400, 'entity': 0}

    score = {
        'liquid': 1764322560, 'gladiators': 1764322560, 'eg': 1764322560, 'shopify': 1764322560, 'tundra': 1764322560,
         'talon': 1764232704, '9pandas': 1762927344, 'spirit': 1737655200, 'tsm': 1133355456, 'lgd': 1119506688,
         'beastcoast': 873824544, 'betboom': 794569536, 'execration': 781801440, 'aster': 730717176, 'nouns': 604852824,
         'bleed': 454468464, 'ig': 384004776, 'blacklist': 195979656, 'quest': 12362112, 'azure': 0

    }

    for team in score.keys():
        #percentage = "{:.2f}%".format(score[team] / 1764322560)
        #percentage = "{:.2f}%".format(score[team] / 1764322560 * 100)
        percentage = "{:.2f}%".format(score[team] / 1764322560 * 100) # 2022: 980179200
        print(team, percentage)

if __name__ == '__main__':
    #what_team_needs()

    #draw_test()

    final_score()
    #permutation()
    pass


""" 2023 results
liquid 100.00%
gladiators 100.00%
eg 100.00%
shopify 100.00%
tundra 100.00%
talon 99.99%
9pandas 99.92%
spirit 98.49%
tsm 64.24%
lgd 63.45%
beastcoast 49.53%
betboom 45.04%
execration 44.31%
aster 41.42%
nouns 34.28%
bleed 25.76%
ig 21.76%
blacklist 11.11%
quest 0.70%
azure 0.00%



"""



''' 2022 results
thunder 100.00%
lgd 100.00%
tsm 100.00%
og 100.00%
beastcoast 99.99%
tundra 99.75%
gladiators 93.96%
boom 90.01%
EG 74.86%
fnatic 61.60%
spirit 53.32%
aster 48.17%
liquid 47.05%
rng 43.63%
outsiders 39.68%
quincy 31.74%
navi 9.88%
talon 6.35%
entity 0.00%'''