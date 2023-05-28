from getFinanceDataPy import getRevenue, getPrice, getProfit
from getUserAddressPy import getCity, getCountry, getStreet

def transformEvent(event, metadata):
  return {
    "revenue": getRevenue(event.get("properties", {})),
    "price": getPrice(event.get("properties", {})),
    "profit": getProfit(event.get("properties", {})),
    "city": getCity(event.get("context", {}).get("address", {})),
    "country": getCountry(event.get("context", {}).get("address", {})),
    "street": getStreet(event.get("context", {}).get("address", {}))
  }