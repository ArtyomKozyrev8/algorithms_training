min_coins = None  # global variable, the minimum number of coins we need to exchange a certain sum of money
global_steps = []  # to remember possible to step to exchange sum of money


def exchange_coins(money_sum: int, coins: list, used_coins_n: int, steps: str):
    """
    Is used to find minimum number of coins to exchange money_sum
    :param money_sum: a certain sum of money
    :param coins: list of possible coins values - list of ints
    :param used_coins_n: initially should be zero number of coins we need to exchange money_sum
    :param steps: initially should be empty string coins which were taken
    :return: not used
    """
    assert isinstance(money_sum, int), "money sum should be integer"
    assert isinstance(coins, list), "coins should be list"
    assert len([i for i in coins if isinstance(i, int)]) == len(coins), "coins should be list of integers"
    assert isinstance(used_coins_n, int), "used_coins_n should be integers"
    global min_coins
    global global_steps
    if money_sum == 0:  # exit from recursion
        if not min_coins:  # any solution was found
            min_coins = used_coins_n
        else:
            if used_coins_n < min_coins:  # better solution was found
                min_coins = used_coins_n
        steps = sorted(steps.split("-"))
        if steps not in global_steps:
            global_steps.append(steps)
        return 0

    choices = []  # storage for possible ways to exchange money
    for c in coins:

        if money_sum - c > 0:
            choices.append(exchange_coins(money_sum - c, coins, used_coins_n + 1, steps + str(c) + "-"))
        elif money_sum - c == 0:
            choices.append(exchange_coins(money_sum - c, coins, used_coins_n + 1, steps + str(c)))
        else:
            pass

    return sum(choices)


if __name__ == '__main__':
    exchange_coins(40, [2, 5, 4], 0, "")
    print(f"MIN COINS: {min_coins}")
    for i in global_steps:
        print(f"STEPS: {i}")
