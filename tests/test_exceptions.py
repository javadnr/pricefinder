from pricefinder.cores.exceptions import GetPriceException

def test_get_price_exception_without_source():
    message = "Error occurred while fetching price"
    exception = GetPriceException(message)

    assert str(exception) == message
    assert exception.source is None  

def test_get_price_exception_with_source():
    message = "Error occurred while fetching price"
    source = "Nobitex API"
    exception = GetPriceException(message, source)

    assert str(exception) == f"[{source}] {message}"
    assert exception.source == source 

def test_get_price_exception_message_only():
    message = "Price fetch failed"
    exception = GetPriceException(message)
    assert str(exception) == message  
    assert exception.source is None 
