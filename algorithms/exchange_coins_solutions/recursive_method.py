COINS = [1, 5, 10, 50, 100]


def exchange_recursive(number: int, coins: list[int] | None = None) -> tuple[int, str]:
    """Recursive method to exchange a certain number."""
    if coins is None:
        coins = COINS

    cache = {}
    used_coins = []

    def inner_exchange_recursive(number_: int, coins_: list[int]) -> tuple[int, str]:
        min_number = float("inf")

        if number_ == 0:
            return 0

        for coin in coins_:
            if number_ >= coin:
                used_coins.append(coin)
                if number_ in cache:
                    min_number_cur = cache[number_]
                else:
                    min_number_cur = 1 + inner_exchange_recursive(number_ - coin, coins_)

                if min_number >= min_number_cur:
                    min_number = min_number_cur

        cache[number_] = min_number
        return min_number

    return inner_exchange_recursive(number, coins)


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
        assert exchange_recursive(item[0]) == item[1]
