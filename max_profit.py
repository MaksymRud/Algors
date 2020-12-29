#####
#
#   Say you have an array for which the ith element is the price of a given stock on day i.
#   If you were only permitted to complete at most one transaction 
#   (i.e., buy one and sell one share of the stock), 
#   design an algorithm to find the maximum profit.
#    Note that you cannot sell a stock before you buy one.
#
#####

def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices) == 1):
            return 0
    
        profit = 0   
        low_pr = 0
        for high_pr in range(0, len(prices)):
            curr_profit = prices[high_pr] - prices[low_pr]
            if(curr_profit < 0):
                low_pr += 1
                continue
            profit = max(curr_profit, profit)
        return profit 

print(maxProfit([1, 2]))