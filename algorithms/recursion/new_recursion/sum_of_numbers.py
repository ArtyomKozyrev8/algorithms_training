def sum_of_numbers(x: list) -> float:
    """recursive function to find sum of numbers in the list"""
    if not x:
        return 0
    if len(x) == 1:
        return x[0]
    return x[0] + sum_of_numbers(x[1:])


if __name__ == '__main__':
    print(sum_of_numbers([1, 2, 3, 5, 9, 12]))
    print(sum_of_numbers([]))
    print(sum_of_numbers([4]))
