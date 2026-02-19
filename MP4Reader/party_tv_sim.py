import time
import os

# Simulated video names (pretend these are MP4 files)
SIMULATED_VIDEOS = [
    "party_video1.mp4",
    "party_video2.mp4",
    "party_video3.mp4"
]

def play(video):
    """Simulate playing a video"""
    print(f"Playing {video}... 🎉")
    time.sleep(2)  # Simulate 2 seconds of playback

def party_tv_loop():
    """Loop through simulated videos like a party TV"""
    print(f"Found {len(SIMULATED_VIDEOS)} videos. Starting party TV!")
    while True:
        for video in SIMULATED_VIDEOS:
            play(video)

if __name__ == "__main__":
    party_tv_loop()
