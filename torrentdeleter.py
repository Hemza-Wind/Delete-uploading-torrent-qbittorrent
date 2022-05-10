import qbittorrentapi
import time
from qbittorrentapi import Client

client = Client(
    host="localhost:8080", username="admin", password="<insert your password here>"
)

print("checking for torrents that are uploading")
print("torrents that are deleted:")

try:
    while True:
        for torrent in client.torrents_info():
            # check if torrent is uploading
            if torrent.state_enum.is_uploading:
                client.torrents_delete(delete_files=False, torrent_hashes=torrent.hash)
                print(f"{torrent.name} is deleted...")
        # decide how long to wait for next check in seconds
        time.sleep(10)

except KeyboardInterrupt:
    pass
