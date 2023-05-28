def getPrice(finance):
  return finance.get("price", 0)

def getRevenue(finance):
  return finance.get("revenue", 0)

def getProfit(finance):
  return getPrice(finance) - getRevenue(finance)