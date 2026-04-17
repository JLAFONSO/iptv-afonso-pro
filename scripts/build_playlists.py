import requests
import os

BASE = "https://iptv-org.github.io/iptv"

countries = {
    "portugal": "countries/pt.m3u",
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

os.makedirs("playlists", exist_ok=True)

def download(name, path):
    url = f"{BASE}/{path}"
    print(f"Downloading {name}...")
    data = requests.get(url).text
    
    with open(f"playlists/{name}.m3u", "w", encoding="utf-8") as f:
        f.write(data)

# países
for name, path in countries.items():
    download(name, path)

# categorias
for name, path in categories.items():
    download(name, path)

print("Playlists organizadas criadas!")
