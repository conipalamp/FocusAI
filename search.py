import requests # type: ignore

# Usa tus datos actuales
API_KEY = "AIzaSyDx5lzvHtHqh4m_85xrxHv13GdTnx0BI3s"
CX_ID = "3250000551de8493e"

def buscar_google(consulta):
    url = f"https://www.googleapis.com/customsearch/v1?q={consulta}&key={API_KEY}&cx={CX_ID}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        resultados = datos.get("items", [])

        if resultados:
            for i, item in enumerate(resultados[:5], start=1):  # Muestra los primeros 5 resultados
                print(f"{i}. {item['title']}\n{item['snippet']}\n{item['link']}\n")
        else:
            print("No se encontraron resultados.")
    else:
        print("Error:", respuesta.status_code, respuesta.text)

# Prueba con una búsqueda
buscar_google("Independencia de Chile")
