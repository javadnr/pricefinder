from ..base_scraper import BaseScraper
from ..exceptions import ScraperException

class NobitexScraper(BaseScraper):
    def get_price(self, symbol: str = "btc", dstCurrency: str = "usdt") -> float:
        """
        Synchronous price fetch
        """
        try:
            url = "https://api.nobitex.ir/market/stats"
            payload = {"srcCurrency": symbol.lower(), "dstCurrency": dstCurrency.lower()}
            response = self._post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            price = float(data['stats'][f"{symbol.lower()}_rls"]['latest'])
            return price
        except Exception as e:
            raise ScraperException(f"Nobitex scraping failed: {e}")

    async def aget_price(self, symbol: str = "btc", dstCurrency: str = "usdt") -> float:
        """
        Asynchronous price fetch
        """
        try:
            url = "https://api.nobitex.ir/market/stats"
            payload = {"srcCurrency": symbol.lower(), "dstCurrency": dstCurrency.lower()}
            response = await self._apost(url, json=payload)
            response.raise_for_status()
            data = response.json()
            price = float(data['stats'][f"{symbol.lower()}_rls"]['latest'])
            return price
        except Exception as e:
            raise ScraperException(f"Async Nobitex scraping failed: {e}")
