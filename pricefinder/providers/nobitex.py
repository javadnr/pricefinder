from ..cores.req_handler import RequestHandler
from ..cores.exceptions import GetPriceException

class Nobitex(RequestHandler):
    def get_price(self, symbol: str = "btc", dst_currency: str = "usdt") -> float:
        """
        Synchronous price fetch
        """
        try:
            url = "https://api.nobitex.ir/market/stats"
            payload = {"srcCurrency": symbol.lower(), "dst_currency": dst_currency.lower()}
            response = self._post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            price = float(data['stats'][f"{symbol.lower()}-{dst_currency}"]['bestBuy'])
            return price
        except Exception as e:
            raise GetPriceException(f"Nobitex get_price failed: {e}")

    async def aget_price(self, symbol: str = "btc", dst_currency: str = "usdt") -> float:
        """
        Asynchronous price fetch
        """
        try:
            url = "https://api.nobitex.ir/market/stats"
            payload = {"srcCurrency": symbol.lower(), "dst_currency": dst_currency.lower()}
            response = await self._apost(url, json=payload)
            response.raise_for_status()
            data = response.json()
            price = float(data['stats'][f"{symbol.lower()}-{dst_currency}"]['bestBuy'])
            return price
        except Exception as e:
            raise GetPriceException(f"Async Nobitex get_price failed: {e}")
