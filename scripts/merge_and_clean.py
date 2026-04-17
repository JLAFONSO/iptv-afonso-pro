import os

PLAYLIST_DIR = "playlists"
OUTPUT = "playlists/final.m3u"

channels_seen = set()
final_lines = ["#EXTM3U\n"]

def is_valid_channel(info_line, url_line):
    text = info_line.lower()

    # ❌ remover geo-block / inválidos
    if "geo" in text:
        return False
    if "xxx" in text:  # opcional, podes remover se quiseres manter adultos
        return True

    # ❌ remover formatos problemáticos
    if ".mpd" in url_line:
        return False

    return True

for file in os.listdir(PLAYLIST_DIR):
    if not file.endswith(".m3u"):
        continue

    path = os.path.join(PLAYLIST_DIR, file)

    with open(path, encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].startswith("#EXTINF"):
            info = lines[i]
            url = lines[i + 1] if i + 1 < len(lines) else ""

            if url in channels_seen:
                continue

            if is_valid_channel(info, url):
                final_lines.append(info)
                final_lines.append(url)
                channels_seen.add(url)

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.writelines(final_lines)

print("Playlist final criada!")
