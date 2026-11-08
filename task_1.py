import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    """Пошук монет жадібним алгоритмом."""
    result = {}

    for coin in COINS:
        count, amount = divmod(amount, coin)
        if count > 0:
            result[coin] = count

    return result


def find_min_coins(amount):
    """Пошук мінімальної кількості монет методом динамічного програмування."""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


if __name__ == "__main__":
    amount = 113

    print("Жадібний алгоритм:", find_coins_greedy(amount))
    print("Динамічне програмування:", find_min_coins(amount))

    print("\nПорівняння часу виконання:")
    print(f"{'Сума':>10} | {'Greedy (с)':>15} | {'DP (с)':>15}")

    for amount in [113, 1000, 10000, 100000, 1000000]:
        greedy_time = (
            timeit.timeit(lambda amount=amount: find_coins_greedy(amount), number=1000)
            / 1000
        )

        dp_time = timeit.timeit(lambda amount=amount: find_min_coins(amount), number=1)

        print(f"{amount:>10} | {greedy_time:>15.8f} | {dp_time:>15.8f}")
