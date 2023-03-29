from console import *
from mathFunctions import *

value: float = getValueFromConsole()
currency: str = getCurrencyFromConsole()
result: float = convertCurrency(value, currency)

printToConsole(result)