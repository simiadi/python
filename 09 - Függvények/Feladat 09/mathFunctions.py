from forex_python.converter import CurrencyRates

c = CurrencyRates()

huf: float = c.get_rate('HUF', 'EUR')
jpy: float = 0.75
usd: float = 0.8
chf: float = 0.55

def convertCurrency(value: float, currency: str) -> float:
    result: float = None

    if(currency == "JPY"):
        result = (value * huf) * jpy
    elif(currency == "USD"):
        result = (value * huf) * usd
    else:
        result = (value * huf) * chf

    return result