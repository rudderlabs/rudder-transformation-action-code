def getPrice(finance):
  return int(finance.get("price", 0))

def getRevenue(finance):
  return int(finance.get("revenue", 0))

def getProfit(finance):
  return getPrice(finance) - getRevenue(finance)