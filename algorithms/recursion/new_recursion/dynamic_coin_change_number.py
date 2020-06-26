storage = {0: 0}
def dynamic_exchange(coins: list, money: int) -> int:
    """
    The idea of the procedure is that we start from the smallest task we can solve.
    You need 0 coins to exchange money = 0. Also we can add 1: 1, one coin to exchange
    money = 1.
    Them we start to grow our table and when we check a bigger money, we check prev
    solutions in our table.
    :param coins: list of coins types
    :param money: money to exchange
    :return: min number of coins to exchange money
    """
    for cur_money in range(0, money + 1):  # build table from small to large
        min_coins = cur_money  # the worst case money/1 = mney
        for c in coins:  # check all possible alternatives
            if cur_money - c >= 0:
                # exactly the coin we tool and data from memory
                coin_number = 1 + storage[cur_money - c]
                if coin_number < min_coins:
                    min_coins = coin_number  # if it is better than worse case - take it
        storage[cur_money] = min_coins # memorise data
    return storage[money]


if __name__ == '__main__':
    x = dynamic_exchange([1, 5, 10, 21, 25], 121)
    print(storage)
    print(x)
