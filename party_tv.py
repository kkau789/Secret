import sys
import os
import time

# Tell Python where your MP4Reader repo is
sys.path.append("/data/data/com.termux/files/home/MP4Reader")

from mp4reader.player import play

VIDEO_FOLDER = os.path.expanduser("~")

def get_mp4_files(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(".mp4")]

def party_tv_loop():
    mp4_files = get_mp4_files(VIDEO_FOLDER)

    if not mp4_files:
        print("No MP4 files found in Termux home.")
        return

    print(f"Found {len(mp4_files)} MP4 files.")
    while True:
        for video in mp4_files:
            print("Now playing:", video)
            play(video)
            time.sleep(1)

if __name__ == "__main__":
    party_tv_loop()
