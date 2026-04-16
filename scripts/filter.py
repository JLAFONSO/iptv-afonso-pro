import re

INPUT = "playlists/full.m3u"
OUTPUT = "playlists/filtered.m3u"

# palavras-chave para filtrar
KEYWORDS = [
    "news", "sport", "movie", "music",
    "portugal", "brazil", "africa",
    "france", "spain", "uk", "usa"
]

with open(INPUT, encoding="utf-8") as f:
    lines = f.readlines()

filtered = []

for i in range(len(lines)):
    line = lines[i].lower()

    if any(k in line for k in KEYWORDS):
        filtered.append(lines[i])
        if i + 1 < len(lines):
            filtered.append(lines[i + 1])

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    f.writelines(filtered)

print("Playlist filtrada criada!")
