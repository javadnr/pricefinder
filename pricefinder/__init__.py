from .providers.nobitex import Nobitex
from .cores.exceptions import GetPriceException

class PriceFinder:
    """
    PriceFinder class is used to get price of a currency from a source.\n
    It requests to a source and returns the price of the currency.\n
    Specify proxy if you want to use a proxy for requests.
    Specify timeout if you want to set a timeout for requests.
    """
    
    def __init__(self, proxy: str = None, timeout: int = 10):
        self.proxy = proxy
        self.timeout = timeout
        self.sources = {
            "nobitex": Nobitex(proxy=proxy, timeout=timeout),
        }
        self.default_source = "nobitex"

    def get_price(self, currency: str, source: str = None, dst_currency : str = "usdt") -> float:
        """
        Uses Nobitex as default source specify the source if you want to use another source\n
        sources:nobitex, binance, kucoin\n
        currency is the currency to get it's price.\n
        source is the source to get price from it.\n
        dst_currency is the price that you want to be returned as like usdt or rls for IRR Rial.
        """
        
        source = source or self.default_source
        if source not in self.sources:
            raise GetPriceException(f"Unknown source '{source}'")
        return self.sources[source].get_price(currency, dst_currency)

    async def aget_price(self, currency: str, source: str = None, dst_currency : str = "usdt") -> float:
        """
        Uses Nobitex as default source specify the source if you want to use another source\n
        sources:nobitex, binance, kucoin\n
        currency is the currency to get it's price.\n
        source is the source to get price from it.\n
        dst_currency is the price that you want to be returned as like usdt or rls for IRR Rial.
        """
        
        source = source or self.default_source
        if source not in self.sources:
            raise GetPriceException(f"Unknown source '{source}'")
        return await self.sources[source].aget_price(currency, dst_currency)
