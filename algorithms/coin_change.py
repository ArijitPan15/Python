"""Unbounded minimum-coin dynamic programming."""
def min_coins(coins, amount):
    coins = tuple(coins)
    if amount < 0 or any(not isinstance(c, int) or c <= 0 for c in coins):
        raise ValueError("invalid amount or denomination")
    best = [amount + 1] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                best[value] = min(best[value], best[value - coin] + 1)
    return -1 if best[amount] > amount else best[amount]
