"""
showcase the possible results of the playoff ladder

TODO:
add regions value to each team, to show possible scenarios of regional qualifiers
create a biased mode based on total team dpc points to base their chance of victory of
"""



# DPC points global scoreboard
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

teams = teams_2023


def generator_first_upper_bracket(group_a, group_b):
    """
    
    :param group_a: len has to be even, and a multiplier of 4
    :param group_b: has to be the same len as :param group_a
    :return:
    """
    bracket = []
    for i in range(len(group_a)):
        bracket.append([group_a[i], group_b[-(i + 1)]])


def direct_ti():
    """Get list of 12 teams that will be directly invited to TI"""
    def team_score(team_name):
        return teams[team_name]
    # lambda_team_score = lambda team_name: teams[team_name]
    top_12 = []
    for team in teams:
        top_12.append(team)
    top_12.sort(reverse=True, key=team_score)  # TODO lambda warning
    top_12 = top_12[:12]
    return top_12


def ladder():
    """
    # TODO create documentaion
    #
    :return:
    """
    def decimal_to_binary(n):
        return bin(n).replace("0b", "")

    general_setting = [0, 1]  # setting for how dropping from upper bracket works

    # old_major_points = [820, 740, 670, 590, 515, 360]
    major_points = [600, 550, 500, 450, 400, 300]
    # old_major_points2 = [0, 0, 0, 0, 360, 360, 515, 515, 590, 670, 740, 820]
    major_points2 = [0, 0, 0, 0, 300, 300, 400, 400, 450, 500, 550, 600]
    global teams
    teams_copy = teams.copy()
    rankings = {}
    for team in teams:
        rankings[team] = 0
    # 2022 possible permutations 262144  # while it should be this number? 19958400 # TODO how I achieved this combination
    # 2023 1764322560
    number_of_scores = 1764322560
    for score_combination in range(number_of_scores):
        score = [False for _ in range(18)]
        scores = decimal_to_binary(score_combination)
        for i, result in enumerate(scores[::-1]):
            if result == "1":
                score[i] = True

        concluded_matches_wins = [0, 3, 8, 9, 10]
        concluded_matches_defeats = [1, 2, 7]
        non_true_scenario = False
        # excluding scenarios that cannot happen anymore
        for defeat in concluded_matches_defeats:
            if not score[defeat]:
                non_true_scenario = True
                break
        for win in concluded_matches_wins:
            if score[win]:
                non_true_scenario = True
                break

        if non_true_scenario:
            number_of_scores -= 1
            continue

        old_A = ["lgd", "outsiders", "og", "fnatic", "rng", "liquid"]
        old_B = ["aster", "entity", "spirit", "boom", "EG", "beastcoast"]

        # groups split during Bali Major
        A = ["beastcoast", "blacklist", "execration", "ig", "shopify", "aster", "liquid", "spirit", "tundra"]
        B = ["9pandas", "azure", "betboom", "bleed", "eg", "gladiators", "nouns", "lgd", "quest"]

        def swap(pair):  # TODO try to create lambda here
            pair[0], pair[1] = pair[1], pair[0]
            return pair

        u1r = [[A[0], B[3]], [A[2], B[1]], [A[1], B[2]], [A[3], B[0]]]  # u1r = upper_first_round
        '''for i in [0, 1, 2, 3]:
            if score[i]:
                swap(u1r[i])
        '''

        lower_bracket = []
        # UPPER BRACKET
        matches = u1r
        score_value = 0
        while True:
            new_round = []
            new_match = []
            for match in matches:
                if score[score_value]:
                    match = swap(match)
                score_value += 1

            for match in matches:
                new_match.append(match[0])
                lower_bracket.append(match[1])
                if len(new_match) == 2:
                    new_round.append(new_match)
                    new_match = []
            matches = new_round

            if len(new_match) == 1:
                final = [new_match[0]]
                break

        # LOWER BRACKET
        matches = [[lower_bracket[3], B[5]], [lower_bracket[2], A[4]], [lower_bracket[1], B[4]], [lower_bracket[0], A[5]]]
        drops_from_upper = 0
        upper_slot = 4
        points = 0
        while True:
            new_round = []
            new_match = []
            for match in matches:
                if score[score_value]:
                    match = swap(match)
                teams[match[1]] += major_points2[points]
                points += 1
                score_value += 1

            drops_from_upper += 1

            for match in matches:
                new_match.append(match[0])
                if drops_from_upper == 2:
                    new_match.append(lower_bracket[upper_slot])
                    upper_slot += 1

                if len(new_match) == 2:
                    new_round.append(new_match)
                    new_match = []
            matches = new_round

            if len(new_match) == 1:
                final.append(new_match[0])
                break
        # final
        '''
        u2r = [[u1r[0][0], u1r[1][0]], [u1r[2][0], u1r[3][0]]]  # u2r = upper_second_round
        # logic
        for i, j in enumerate([4, 5]):
            if score[j]:
                swap(u2r[i])

        u3r = [u2r[0][0], u2r[1][0]]  # u3r = upper_third_round
        # logic
        if score[6]:
            swap(u3r)

        l1r = [[u1r[3][1], B[5]], [u1r[2][1], A[4]], [u1r[1][1], B[4]], [u1r[0][1], A[5]]]  # l1r = lower_first_round
        # logic
        for i, j in enumerate([7, 8, 9, 10]):
            if score[j]:
                swap(l1r[i])

        l2r = [[l1r[0][0], l1r[1][0]], [l1r[2][0], l1r[3][0]]]  # l2r = lower_second_round
        # logic
        for i, j in enumerate([11, 12]):
            if score[j]:
                swap(l2r[i])

        teams[l2r[0][1]] += major_points[5]
        teams[l2r[1][1]] += major_points[5]

        l3r = [[u2r[general_setting[0]][1], l2r[0][0]], [u2r[general_setting[1]][1], l2r[1][0]]]  # l3r = lower_third_round

        # logic
        for i, j in enumerate([13, 14]):
            if score[j]:
                l3r[i] = swap(l3r[i])

        teams[l3r[0][1]] += major_points[4]
        teams[l3r[1][1]] += major_points[4]

        l4r = [l3r[0][0], l3r[1][0]]  # l4r = lower_fourth_round
        # logic
        if score[15]:
            l4r = swap(l4r)

        teams[l4r[1]] += major_points[3]

        l5r = [u3r[1], l4r[0]]  # l5r = lower_fifth_round
        if score[16]:
            l5r = swap(l5r)

        teams[l5r[1]] += major_points[2]

        # FINAL
        final = [u3r[0], l5r[0]]
        '''
        if score[17]:
            final = swap(final)

        teams[final[1]] += major_points[1]
        teams[final[0]] += major_points[0]

        top = direct_ti()
        for team in top:
            rankings[team] += 1

        teams = teams_copy.copy()
    print(rankings)
    print(number_of_scores)
    return [rankings, number_of_scores]


def final_score(games_result):
    """first 6 places get points

    :param games_result:
    :return:
    """

    '''old_score = {'thunder': 262144, 'lgd': 262144, 'tsm': 262144, 'og': 262144, 'beastcoast': 262144, 'tundra': 254464,
             'gladiators': 194560, 'boom': 225280, 'EG': 172032, 'fnatic': 196608, 'spirit': 196608, 'aster': 196608,
             'liquid': 131072, 'rng': 98304, 'outsiders': 169472, 'entity': 0}
    number_of_games = 
    '''
    number_of_games = games_result[1]
    score = games_result[0]

    for team in score.keys():
        # percentage = "{:.2f}%".format(score[team] / 1764322560)
        # percentage = "{:.2f}%".format(score[team] / 1764322560 * 100)
        percentage = "{:.2f}%".format(score[team] / number_of_games * 100)
        print(team, percentage)


if __name__ == '__main__':
    print("start")

    ladder_result = ladder()

    final_score(ladder_result)
