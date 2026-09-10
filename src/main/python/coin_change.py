# # A Dynamic Programming based Python3 program to
# # find minimum of coins to make a given change V
# import sys
#
# # m is size of coins array (number of
# # different coins)
# def minCoins(coins, m, V):
#
#     # table[i] will be storing the minimum
#     # number of coins required for i value.
#     # So table[V] will have result
#     table = [0 for i in range(V + 1)]
#     print (table)
#
#     # Base case (If given value V is 0)
#     table[0] = 0
#
#     # Initialize all table values as Infinite
#     for i in range(1, V + 1):
#         table[i] = sys.maxsize
#     print (table)
#     # Compute minimum coins required
#     # for all values from 1 to V
#     for i in range(1, V + 1):
#
#         # Go through all coins smaller than i
#         for j in range(m):
#             if (coins[j] <= i):
#                 sub_res = table[i - coins[j]]
#                 print ("sub_res :"+str(sub_res))
#                 if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
#                     table[i] = sub_res + 1
#                     print (table)
#     print (table)
#     if table[V] == sys.maxsize:
#         return -1
#
#     return table[V]
#
# # Driver Codeb x
# if __name__ == "__main__":
#
#     coins = [9, 6, 5, 1]
#     m = len(coins)
#     V = 11
#     print("Minimum coins required is ",
#                  minCoins(coins, m, V))


# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Example 3:
#
# Input: coins = [1], amount = 0
# Output: 0
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)  # Initialize DP table with infinity
    print (dp)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    print (dp)
    for coin in coins:
        print ("coin:"+ str(coin))
        print ("amount:"+ str(amount+1))
        for i in range(coin, amount + 1):
            print ("i:"+ str(i))
            print (dp[i], dp[i - coin] + 1)
            dp[i] = min(dp[i], dp[i - coin] + 1)
            print (dp)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example test cases
print(coinChange([1, 2, 5], 11))  # Output: 3
# print(coinChange([2], 3))         # Output: -1
# print(coinChange([1], 0))         # Output: 0
