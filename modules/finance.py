from config import cg  # Importar la API desde config.py

def obtener_precio(cripto):
    """Obtiene el precio actual de una criptomoneda desde CoinGecko."""
    try:
        datos = cg.get_price(ids=cripto, vs_currencies='usd')
        if cripto in datos:
            precio = datos[cripto]['usd']
            return f"💰 El precio actual de {cripto} es ${precio} USD."
        else:
            return "⚠️ No se encontró la criptomoneda. Intenta con otro nombre."
    except Exception as e:
        return f"❌ Error al obtener el precio: {e}"
import requests  # type: ignore

# Configura tu API Key de Alpha Vantage
ALPHA_VANTAGE_API_KEY = "TU_API_KEY_AQUI"

def obtener_precio_accion(simbolo):
    """Obtiene el precio actual de una acción usando Alpha Vantage."""
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={simbolo}&apikey={ALPHA_VANTAGE_API_KEY}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    if "Global Quote" in datos:
        precio = datos["Global Quote"]["05. price"]
        return f"📈 Precio de {simbolo}: ${precio}"
    return "⚠️ No se pudo obtener el precio de la acción."

def obtener_precio_cripto(moneda_base="BTC", moneda_destino="USD"):
    """Obtiene el precio de una criptomoneda (ej. BTC a USD)."""
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={moneda_base}&to_currency={moneda_destino}&apikey={ALPHA_VANTAGE_API_KEY}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    if "Realtime Currency Exchange Rate" in datos:
        precio = datos["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        return f"💰 1 {moneda_base} = {precio} {moneda_destino}"
    return "⚠️ No se pudo obtener el precio de la criptomoneda."

def obtener_tasa_cambio(divisa_origen="USD", divisa_destino="EUR"):
    """Obtiene la tasa de cambio entre dos monedas (ej. USD a EUR)."""
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={divisa_origen}&to_currency={divisa_destino}&apikey={ALPHA_VANTAGE_API_KEY}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    if "Realtime Currency Exchange Rate" in datos:
        tasa = datos["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        return f"💱 1 {divisa_origen} = {tasa} {divisa_destino}"
    return "⚠️ No se pudo obtener la tasa de cambio."

# 📌 Ejemplo de uso
if __name__ == "__main__":
    print(obtener_precio_accion("AAPL"))  # Precio de Apple
    print(obtener_precio_cripto("BTC", "USD"))  # Precio de Bitcoin en USD
    print(obtener_tasa_cambio("USD", "EUR"))  # Tasa de cambio USD a EUR
