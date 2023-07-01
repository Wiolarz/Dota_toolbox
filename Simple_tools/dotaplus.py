def test():
    """
    In dotaplus update they added option to spend shard to buy additional avoid player slots.
    This code check how much slots you can buy
    :return:
    """
    last_value = 25
    for millions in range(1, 21):
        money = 1000000 * millions
        cost = 10000
        incr = 5000
        slots = 25
        while money >= cost:
            money -= cost
            cost += incr
            slots += 1

        perc = 1 - (last_value / slots)

        print(millions, ": ", slots, end=" +", sep="")
        print("{:2.2%}".format(perc))
        last_value = slots


if __name__ == '__main__':
    test()