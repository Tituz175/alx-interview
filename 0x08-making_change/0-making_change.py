#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    coins = sorted(coins)
    count = 0
    num = total - coins.pop()
    count += 1
    for item in reversed(coins):
        if num % item == 0:
            return (count + (num // item))
    return -1
