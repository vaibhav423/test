import sys
import requests
import json
api_key = "AIzaSyAUBhuPhw_jHVUAGOTMUWFkA8s5ROor410"
url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={sys.argv[1]}&key={api_key}"

data = requests.get(url).json()["items"][0]["snippet"]
print(json.dumps({
    "pthumb": data["thumbnails"]["medium"]["url"],
    "ptitle": data["title"],
    "plink": f"https://youtube.com/playlist?list={sys.argv[1]}"
}))