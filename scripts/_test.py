import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from pricefinder import PriceFinder

finder = PriceFinder()
btc = finder.get_price("trx")

print(btc)
