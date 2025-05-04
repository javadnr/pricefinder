import requests
import httpx

class RequestHandler:
    """Returns a requests session object for sync requests or send request with httpx for async requests"""
    def __init__(self, proxy: str = None, timeout: int = 10):
        self.session = requests.Session()
        self.timeout = timeout
        self.proxy = proxy

        if proxy:
            self.session.proxies.update({
                'http': proxy,
                'https': proxy,
            })

    def _get(self, url: str, params: dict = None):
        return self.session.get(url, params=params, timeout=self.timeout)

    def _post(self, url: str, json: dict = None):
        return self.session.post(url, json=json, timeout=self.timeout)

    async def _aget(self, url: str, params: dict = None):
        proxies = None
        if self.proxy:
            proxies = {
                "http://": self.proxy,
                "https://": self.proxy,
            }
        async with httpx.AsyncClient(proxies=proxies, timeout=self.timeout) as client:
            return await client.get(url, params=params)

    async def _apost(self, url: str, json: dict = None):
        proxies = None
        if self.proxy:
            proxies = {
                "http://": self.proxy,
                "https://": self.proxy,
            }
        async with httpx.AsyncClient(proxies=proxies, timeout=self.timeout) as client:
            return await client.post(url, json=json)
