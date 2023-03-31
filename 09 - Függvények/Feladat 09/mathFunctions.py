from forex_python.converter import CurrencyRates

c = CurrencyRates()

eur: float = c.get_rate('EUR', 'HUF')
huf: float = c.get_rate('HUF', 'EUR')
jpy: float = 0.75
usd: float = 0.8
chf: float = 0.55

def convertCurrency(value: float, currency: str) -> float:
    result: float = None

    if(currency == "JPY"):
        result = (value / eur) * jpy
    elif(currency == "USD"):
        result = (value / eur) * usd
    elif(currency == "CHF"):
        result = (value / eur) * chf
    else:
        result = (value / eur)

    return result