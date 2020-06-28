exchange_storage = {0: 0}  # to exchange money = 0 you need no coins
last_taken_coin_storage = {}
def dynamic_coin_change_number_with_step_history(coins: list, money: int) -> (int, list):
    """
    Calculates the minimum number of coins to exchange the required su on money
    exchange_storage - table about number of coins to exchange smaller sum of money
    last_taken_coin_storage - table to store data about last coin taken to exchange the sum of money
    :param coins: list of coins - positive integers
    :param money: sum of money to exchange
    :return: (number of coins, list of steps)
    """
    for cur_money in range(money + 1):
        min_number_of_coins = cur_money  # money / 1  money since coins have [1, .... ]
        last_coin = 0  # no coin was taken
        for c in coins:
            if cur_money - c >= 0:
                temp = 1 + exchange_storage[cur_money - c]
                if temp < min_number_of_coins:
                    min_number_of_coins = temp
                    last_coin = c
        last_taken_coin_storage[cur_money] = last_coin  # memorise last coin
        exchange_storage[cur_money] = min_number_of_coins

    steps = []
    temp_money = money
    while temp_money:
        c = last_taken_coin_storage[temp_money]  # take last taken coin to reach the point
        steps.append(c)
        temp_money -= c

    return exchange_storage[money], steps


if __name__ == '__main__':
    print(dynamic_coin_change_number_with_step_history([1, 21, 5, 10, 15, 25], 12))
    print(help(dynamic_coin_change_number_with_step_history))
