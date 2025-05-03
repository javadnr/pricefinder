class ScraperException(Exception):
    """Custom exception raised for errors during scraping operations."""
    def __init__(self, message: str, source: str = None):
        self.source = source
        self.message = message
        full_message = f"[{source}] {message}" if source else message
        super().__init__(full_message)
