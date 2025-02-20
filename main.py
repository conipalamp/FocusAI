import subprocess
import datetime
import pytz  # type: ignore
import requests  # type: ignore

# 🔹 API KEYS (NO COMPARTIR EN CÓDIGO PÚBLICO)
OPENWEATHER_API_KEY = "6a690a1e54333f15b6458bdf35642807"
GOOGLE_API_KEY = "AIzaSyDx5lzvHtHqh4m_85xrxHv13GdTnx0BI3s"
GOOGLE_CX_ID = "3250000551de8493e"

# 🔹 OBTENER CLIMA DESDE OPENWEATHER
def obtener_clima(ciudad):
    """Consulta el clima en OpenWeather y devuelve una respuesta formateada."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            descripcion = data["weather"][0]["description"]
            humedad = data["main"]["humidity"]
            viento = data["wind"]["speed"]
            
            return (f"🌤️ **Clima en {ciudad}:** {descripcion.capitalize()}\n"
                    f"🌡️ Temperatura: {temp}°C\n"
                    f"💧 Humedad: {humedad}%\n"
                    f"💨 Viento: {viento} m/s")
        else:
            return f"⚠️ No se pudo obtener el clima de {ciudad}. Verifica el nombre o la API Key."
    except Exception as e:
        return f"❌ Error al consultar el clima: {e}"

# 🔹 OBTENER PRECIO DE CRIPTOMONEDAS DESDE COINGECKO
def obtener_precio(cripto):
    """Consulta el precio de una criptomoneda en CoinGecko y devuelve el valor en USD."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies=usd"

    try:
        response = requests.get(url)
        data = response.json()

        if cripto in data:
            precio = data[cripto]["usd"]
            return f"💰 **Precio de {cripto.capitalize()}:** ${precio} USD"
        else:
            return f"⚠️ No se encontró información sobre '{cripto}'. Asegúrate de escribir el nombre correcto (ej: bitcoin, ethereum)."
    except Exception as e:
        return f"❌ Error al obtener el precio de la criptomoneda: {e}"

# 🔹 BÚSQUEDA EN GOOGLE
def buscar_en_google(consulta):
    """Realiza una búsqueda en Google y devuelve los primeros 3 resultados."""
    url = f"https://www.googleapis.com/customsearch/v1?q={consulta}&key={GOOGLE_API_KEY}&cx={GOOGLE_CX_ID}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if "items" in data:
            resultados = data["items"][:3]  # Tomar los 3 primeros resultados
            texto = "\n🔎 **Resultados de búsqueda:**\n"
            for i, item in enumerate(resultados, start=1):
                texto += f"\n{i}. **{item['title']}**\n{item['snippet']}\n🔗 {item['link']}\n"
            return texto
        else:
            return "No se encontraron resultados en la web."
    
    except Exception as e:
        return f"❌ Error en la búsqueda de Google: {e}"

# 🔹 CHAT CON IA
def chat_with_ai(prompt):
    """Responde preguntas sobre clima, criptomonedas, hora en Chile o realiza búsquedas en Google."""
    prompt_lower = prompt.lower()

    # 🔹 Pregunta sobre el clima
    if "clima" in prompt_lower or "temperatura" in prompt_lower or "lluvia" in prompt_lower:
        palabras = prompt_lower.split()
        ciudad = palabras[-1]  # Toma la última palabra como ciudad
        return obtener_clima(ciudad)

    # 🔹 Pregunta sobre criptomonedas
    if "precio de" in prompt_lower:
        palabras = prompt_lower.split()
        cripto = palabras[-1]  # Toma la última palabra como criptomoneda
        return obtener_precio(cripto)

    # 🔹 Pregunta sobre la hora en Chile
    if "qué hora es en chile" in prompt_lower or "que hora es en chile" in prompt_lower:
        chile_tz = pytz.timezone("America/Santiago")
        hora_actual = datetime.datetime.now(chile_tz).strftime("%H:%M")
        return f"🕒 La hora actual en Chile es {hora_actual}."

    # 🔹 Buscar en Google
    return buscar_en_google(prompt)

# 🔹 MENÚ PRINCIPAL
def main():
    """Menú principal de FocusAI"""
    while True:
        print("\n📌 FocusAI - Gestor de Tareas")
        print("1️⃣ Agregar tarea")
        print("2️⃣ Ver tareas")
        print("3️⃣ Completar tarea")
        print("4️⃣ Eliminar tarea")
        print("5️⃣ Preguntar a la IA 🤖")
        print("6️⃣ Consultar precio de criptomonedas 💰")
        print("7️⃣ Salir")

        opcion = input("Selecciona una opción: ").strip()

        # 🔹 Si la entrada no es un número, se asume que es una pregunta para la IA
        if not opcion.isdigit():
            print(f"🤖 IA: {chat_with_ai(opcion)}")
            continue

        opcion = int(opcion)

        if opcion == 5:
            pregunta = input("¿Qué quieres preguntar a la IA? ")
            respuesta = chat_with_ai(pregunta)
            print(f"🤖 IA: {respuesta}")

        elif opcion == 6:
            cripto = input("💰 ¿De qué criptomoneda quieres conocer el precio? ").strip().lower()
            print(f"🤖 {obtener_precio(cripto)}")

        elif opcion == 7:
            print("👋 Saliendo de FocusAI...")
            break

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
from config import actualizar_precio_continuo

def main():
    print("📢 Iniciando actualización de precios de criptomonedas...")
    actualizar_precio_continuo("bitcoin", "usd", 30)  # Actualiza Bitcoin cada 30 segundos

    while True:
        opcion = input("Presiona 'q' para salir: ").strip()
        if opcion.lower() == "q":
            print("👋 Saliendo de FocusAI...")
            break

if __name__ == "__main__":
    main()
from modules.finance import obtener_precio_accion, obtener_precio_cripto, obtener_tasa_cambio

print(obtener_precio_accion("TSLA"))  # Precio de Tesla
print(obtener_precio_cripto("ETH", "USD"))  # Precio de Ethereum en USD
print(obtener_tasa_cambio("CLP", "USD"))  # Tasa de cambio Peso Chileno a Dólar
