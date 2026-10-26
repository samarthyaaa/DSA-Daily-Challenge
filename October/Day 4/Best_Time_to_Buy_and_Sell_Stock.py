brute force:
class Solutions:
    def best_time(self, price):
        maxi = 0
        n = len(price)

        for i in range(n):
            for j in range(i + 1, n):
                profit = price[j] - price[i]

                if profit > maxi:
                    maxi = profit

        return maxi

optimal solution:
nums = [7, 8, 4, 6, 9]
s = Solutions()
print(s.best_time(nums))
class solutions:
  def best_time(self,price):
    mini=price[0]
    max=0
    for i in price:
      profit = i - mini
      if profit > max:
        max=profit
      if mini > i:
        mini=i
    return max
        
nums=[7,8,4,6,9]
s=solutions()
print(s.best_time(nums))
