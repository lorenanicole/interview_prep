# https://leetcode.com/problems/coin-change

# Dynamic Programming - Bottom Up
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        # Bottom up / depth first! 
        # Seed initial val with amount + 1 to find,
        # using the coins to iterate and determine the 
        # recurrence relation
        dp_arr = [amount + 1] * (amount + 1)
        dp_arr[0] = 0

        coins.sort()

        for coin in coins:
            for indx in range(1,len(dp_arr)):
                if coin <= indx:
                    # Find the recurrence relation!
                    # equation that defines a sequence by expressing each term 
                    # as a function of one or more preceding terms, essentially 
                    # providing a rule to calculate the next term based on previous 
                    # terms in the sequence; it's a way to describe a sequence 
                    # recursively where each value depends on the values that came 
                    # before it e.g. what is smaller the amount seeded
                    # at the amount indx (amount + 1) or the current 
                    # coin + diff of coin - indx
                    dp_arr[indx] = min(
                        dp_arr[indx],
                        dp_arr[indx - coin] + 1
                    )

        if dp_arr[amount] == amount + 1:
            return -1
        else:
            return dp_arr[amount]

solution = Solution()
print(solution.coinChange([1,2,5], 11) == 3)
print(solution.coinChange([2], 3) == -1)
print(solution.coinChange([1], 0) == 0)
print(solution.coinChange([186,419,83,408], 6249) == 20)