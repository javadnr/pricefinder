# crypto_scraper/currencies.py

from .exchanges.nobitex import NobitexScraper
from .exceptions import ScraperException

class CurrencyScraperFacade:
    """Use Nobitex as default source specify the source if you want to use another source
    """
    def __init__(self, proxy: str = None, timeout: int = 10):
        self.proxy = proxy
        self.timeout = timeout
        self.sources = {
            "nobitex": NobitexScraper(proxy=proxy, timeout=timeout),
        }
        self.default_source = "nobitex"

    def get_price(self, symbol: str, source: str = None, dstCurrency : str = "usdt") -> float:
        """symbol is the currency to get it's price 
        and source is the source to get price from
        and dstCurrency is the price that you want to return as like usdt or rls for IRR Rial"""
        source = source or self.default_source
        if source not in self.sources:
            raise ScraperException(f"Unknown source '{source}'")
        return self.sources[source].get_price(symbol, dstCurrency)

    async def aget_price(self, symbol: str, source: str = None, dstCurrency : str = "usdt") -> float:
        """symbol is the currency to get it's price
        and source is the source to get price from
        and dstCurrency is the price that you want to return as like usdt or rls for IRR Rial"""
        source = source or self.default_source
        if source not in self.sources:
            raise ScraperException(f"Unknown source '{source}'")
        return await self.sources[source].aget_price(symbol, dstCurrency)
