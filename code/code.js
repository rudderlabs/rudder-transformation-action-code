import { getRevenue, getPrice, getProfit } from "getFinanceData";
import { getCity, getCountry, getStreet } from "getUserAddress";

export function transformEvent(event, metadata) {
  return {
    revenue: getRevenue(event.properties || {}),
    price: getPrice(event.properties || {}),
    profit: getProfit(event.properties || {}),
    city: getCity(event.context?.address || {}),
    country: getCountry(event.context?.address || {}),
    street: getStreet(event.context?.address || {}),
  };
}
