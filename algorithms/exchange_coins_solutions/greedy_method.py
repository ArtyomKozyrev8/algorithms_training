from typing import Optional, List, Tuple


COINS = [1, 5, 10, 50, 100]


def exchange_greedy(
        number: int,
        coins: Optional[List[int]] = None,
) -> Tuple[int, List[int]]:
    """Greedy method to exchange a certain number."""
    used_coins = []
    if coins is None:
        coins = COINS

    coins = sorted(coins, reverse=True)
    coins_num = 0

    for coin in coins:
        while number >= coin:
            coins_num += 1
            number -= coin
            used_coins.append(coin)

    return coins_num, sorted(used_coins)


if __name__ == '__main__':
    # structure of inputs items: (number, coins_num_to_exchange_the_sum, coins_used)
    inputs = (
        (333, 9, [1, 1, 1, 10, 10, 10, 100, 100, 100]),
        (101, 2, [1, 100]),
        (0, 0, []),
        (99, 10, [1, 1, 1, 1, 5, 10, 10, 10, 10, 50]),
        (1, 1, [1]),
        (2, 2, [1, 1]),
        (7, 3, [1, 1, 5]),
        (10, 1, [10]),
        (21, 3, [1, 10, 10]),
        (33, 6, [1, 1, 1, 10, 10, 10]),
        (53, 4, [1, 1, 1, 50]),
        (161, 4, [1, 10, 50, 100]),
    )

    for item in inputs:
        assert exchange_greedy(item[0]) == (item[1], item[2])
