storage_one = []
def change_money_one(coins: list, money: int, coin_num: int) -> None:
    """
    Is used to fill support the support outer structure storage_one with possible
    number of coins to exchange the requested sum of money
    :param coins: list of coin types
    :param money: sum of money we would like to exchange
    :param coin_num: number of coins we need to exchange the money, equal to 0 at the beginning
    :return: None
    """
    if money == 0:
        storage_one.append(coin_num)

    for c in coins:
        if money - c >= 0:
            change_money_one(coins, money - c, coin_num + 1)


storage_two = {}
def change_money_two(coins: list, money: int) -> int:
    """
    Returns the minimum number of coins we need to exchange the certain sum of money
    storage_two is used to keep recursion results
    :param coins: list of coin types
    :param money: sum of money we would to exchange
    :return: min number of coins we need to exchange the sum of money
    """
    min_number_of_coins = money  # we can do so, since the smallest coin is one, money/1 = money
    for c in coins:
        if money - c == 0:
            if money - c in storage_two.keys():
                return storage_two[money - c]
            else:
                storage_two[money - c] = 1
                return storage_two[money - c]
        else:
            if money - c > 0:
                # temp is the way we can store result of recursion without returning anything
                if money - c in storage_two.keys():
                    temp = storage_two[money - c]
                else:
                    storage_two[money - c] = 1 + change_money_two(coins, money - c)
                    temp = storage_two[money - c]
                if temp < min_number_of_coins:
                    min_number_of_coins = temp
    return min_number_of_coins


if __name__ == '__main__':
    change_money_one([1, 5, 10, 25], 24, 0)
    print(set(storage_one))
    if storage_one:
        print(min(storage_one))

    print(change_money_two([1, 5, 10, 25], 157))

