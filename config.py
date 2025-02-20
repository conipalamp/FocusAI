OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2"  # O cambia a "mistral" si prefieres
OLLAMA_MODEL = "mistral"
# 📌 Claves API para servicios externos
GOOGLE_API_KEY = "AIzaSyDx5lzvHtHqh4m_85xrxHv13GdTnx0BI3s"
GOOGLE_CX_ID = "3250000551de8493e"  # Para búsquedas personalizadas

# 🔹 Clima
OPENWEATHER_API_KEY = "6a690a1e54333f15b6458bdf35642807"

# 💰 Finanzas y Trading
ALPHA_VANTAGE_API_KEY = "5BLM2ULVWHCYXQFT"

# 📍 Mapas y Ubicación
GRAPHOPPER_API_KEY = "5de6a4f8-fc85-4ac5-ada6-3c2713486aa2"
HERE_API_KEY = "QOjTN1sFzmaHQkTLIxIbl1t32jKZ12jLQafUQANBevE"

# 📆 Productividad
GOOGLE_CALENDAR_API_KEY = "TU_API_KEY"
TRELLO_API_KEY = "TU_API_KEY"
TRELLO_TOKEN = "TU_TOKEN"

# 💲 Monetización
STRIPE_SECRET_KEY = "TU_SECRET_KEY"
PAYPAL_CLIENT_ID = "TU_CLIENT_ID"
PAYPAL_SECRET = "TU_SECRET"
ADSENSE_API_KEY = "TU_API_KEY"

# 🛍️ Afiliados
AMAZON_AFFILIATE_ID = "TU_AFILIADO_ID"
EBAY_AFFILIATE_ID = "TU_AFILIADO_ID"
from pycoingecko import CoinGeckoAPI # type: ignore

cg = CoinGeckoAPI()  # Inicializar la API de CoinGecko
