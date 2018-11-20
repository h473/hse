import math
price = float(input())
pricerub = math.floor(price)
pricekop = round((price - pricerub) * 100)
print(pricerub, int(pricekop))
