class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        
        max_price =0

        for price in prices:
            profit = price-min_price
            min_price = min(min_price,price)
            max_price = max(max_price,profit)

        return max_price



        # l,r=0,1
        # maxP=0
        # while r<len(prices):
        #     if prices[r]>prices[l]:
        #         profit = prices[r]-prices[l]
        #         maxP=max(maxP,profit)
        #     else: 
        #         l=r
        #     r+=1
        # return maxP
        