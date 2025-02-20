from geopy.geocoders import Nominatim  # type: ignore
import requests  # type: ignore
import folium  # type: ignore

# 🔹 Configurar geocodificador Nominatim
geolocator = Nominatim(user_agent="FocusAI")

def obtener_coordenadas(direccion):
    """Convierte una dirección en coordenadas (latitud, longitud) usando Nominatim."""
    try:
        ubicacion = geolocator.geocode(direccion)
        if ubicacion:
            return ubicacion.latitude, ubicacion.longitude
        return None
    except Exception as e:
        return f"⚠️ Error en obtener_coordenadas: {e}"

def obtener_direccion(lat, lon):
    """Convierte coordenadas en dirección usando Nominatim."""
    try:
        ubicacion = geolocator.reverse((lat, lon))
        if ubicacion:
            return ubicacion.address
        return None
    except Exception as e:
        return f"⚠️ Error en obtener_direccion: {e}"

def geocode_xyz(direccion):
    """Usa Geocode.xyz para obtener coordenadas desde una dirección."""
    url = f"https://geocode.xyz/{direccion}?json=1"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si hay un problema HTTP
        datos = respuesta.json()
        if "latt" in datos and "longt" in datos:
            return float(datos["latt"]), float(datos["longt"])
        return None
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error en Geocode.xyz: {e}"

def generar_mapa(lat, lon, nombre_archivo="mapa.html"):
    """Crea un mapa con OpenStreetMap y guarda el archivo HTML."""
    try:
        mapa = folium.Map(location=[lat, lon], zoom_start=14)
        folium.Marker([lat, lon], popup="Ubicación").add_to(mapa)
        mapa.save(nombre_archivo)
        return f"✅ Mapa guardado como {nombre_archivo}"
    except Exception as e:
        return f"⚠️ Error en generar_mapa: {e}"

# 🔹 Configuración de APIs
GRAPHOPPER_API_KEY = "TU_API_KEY_AQUI"
HERE_API_KEY = "TU_API_KEY_AQUI"

def obtener_ruta(origen, destino):
    """Calcula la mejor ruta entre dos puntos con GraphHopper."""
    url = f"https://graphhopper.com/api/1/route?point={origen}&point={destino}&vehicle=car&key={GRAPHOPPER_API_KEY}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        if "paths" in datos:
            distancia = datos["paths"][0]["distance"] / 1000  # Convertir a km
            duracion = datos["paths"][0]["time"] / 60000  # Convertir a minutos
            return f"🚗 Distancia: {distancia:.2f} km, ⏳ Duración: {duracion:.2f} min"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error en GraphHopper: {e}"
    return "⚠️ No se pudo obtener la ruta."

def obtener_ruta_osrm(origen, destino):
    """Usa OSRM para calcular rutas."""
    url = f"http://router.project-osrm.org/route/v1/driving/{origen};{destino}?overview=false"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        if "routes" in datos:
            distancia = datos["routes"][0]["distance"] / 1000  # Convertir a km
            duracion = datos["routes"][0]["duration"] / 60  # Convertir a minutos
            return f"🛣️ Ruta: {distancia:.2f} km, ⏳ Tiempo: {duracion:.2f} min"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error en OSRM: {e}"
    return "⚠️ No se encontró una ruta."

def obtener_trafico_here(origen, destino):
    """Usa HERE Maps para obtener rutas con tráfico."""
    url = f"https://router.hereapi.com/v8/routes?transportMode=car&origin={origen}&destination={destino}&return=summary&apiKey={HERE_API_KEY}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        if "routes" in datos:
            distancia = datos["routes"][0]["sections"][0]["summary"]["length"] / 1000
            duracion = datos["routes"][0]["sections"][0]["summary"]["baseDuration"] / 60
            return f"🚦 Distancia: {distancia:.2f} km, ⏳ Duración con tráfico: {duracion:.2f} min"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error en HERE Maps: {e}"
    return "⚠️ No se pudo calcular la ruta."

# 📌 Ejemplo de uso:
print(obtener_ruta("-36.8201,-73.0443", "-33.4489,-70.6693"))  # De Concepción a Santiago
print(obtener_ruta_osrm("-36.8201,-73.0443", "-33.4489,-70.6693"))
print(obtener_trafico_here("-36.8201,-73.0443", "-33.4489,-70.6693"))
