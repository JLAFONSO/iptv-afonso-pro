import requests
import os

BASE = "https://iptv-org.github.io/iptv"

countries = {
    "portugal": "countries/pt.m3u",
    "angola": "countries/ao.m3u",
    "brazil": "countries/br.m3u",
    "usa": "countries/us.m3u",
    "uk": "countries/uk.m3u",
    "france": "countries/fr.m3u",
    "spain": "countries/es.m3u"
}

categories = {
    "news": "categories/news.m3u",
    "sports": "categories/sports.m3u",
    "movies": "categories/movies.m3u"
}

# 🔧 garantir caminho correto
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PLAYLIST_DIR = os.path.join(BASE_DIR, "playlists")

os.makedirs(PLAYLIST_DIR, exist_ok=True)

def download(name, path):
    url = f"{BASE}/{path}"
    print(f"👉 Downloading {name} from {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        file_path = os.path.join(PLAYLIST_DIR, f"{name}.m3u")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"✅ Saved: {file_path}")

    except Exception as e:
        print(f"❌ Error downloading {name}: {e}")

# países
for name, path in countries.items():
    download(name, path)

# categorias
for name, path in categories.items():
    download(name, path)

print("\n🎯 Playlists organizadas criadas!")
