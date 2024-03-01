#!/usr/bin/python3
def makeChange(coins, total):
    max_val = float('inf')
    table = [[max_val for _ in range(total + 1)] for _ in range(len(coins))]

    for i in range(len(coins)):
        for j in range(total + 1):
            if j == 0:
                table[i][j] = 0
            elif coins[i] <= j:
                if i == 0:
                    table[i][j] = table[i][j - coins[i]] + \
                        1 if j % coins[i] == 0 else max_val
                else:
                    table[i][j] = min(
                        table[i - 1][j], table[i][j - coins[i]] + 1)
            else:
                if i > 0:
                    table[i][j] = table[i - 1][j]
    return table[-1][-1] if table[-1][-1] != float('inf') else -1
