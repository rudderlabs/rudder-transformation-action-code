def getPrice(finance):
  return float(finance.get("price", 0))

def getRevenue(finance):
  return float(finance.get("revenue", 0))

def getProfit(finance):
  return getPrice(finance) - getRevenue(finance)