import requests

url = "https://iptv-org.github.io/iptv/index.m3u"

print("A descarregar playlist...")

data = requests.get(url).text

with open("playlists/full.m3u", "w", encoding="utf-8") as f:
    f.write(data)

print("Playlist gerada com sucesso!")
