import curses
import subprocess
import os
import webbrowser

# Web apps for your Fire TV menu
WEB_APPS = {
    "y": "YouTube",
    "r": "Roblox",
    "s": "Spotify",
    "w": "WhatsApp",
    "i": "Instagram",
    "n": "Snapchat"
}

# Downloads folder path
DOWNLOADS_PATH = "/data/data/com.termux/files/home/storage/downloads"

def find_mp4():
    """Find the first MP4 file in Downloads"""
    for file in os.listdir(DOWNLOADS_PATH):
        if file.lower().endswith(".mp4"):
            return os.path.join(DOWNLOADS_PATH, file)
    return None

def play_video(video_path):
    """Open MP4 in Android's default video player"""
    if video_path and os.path.exists(video_path):
        subprocess.run([
            "am",
            "start",
            "-a", "android.intent.action.VIEW",
            "-d", f"file://{video_path}",
            "-t", "video/mp4"
        ])
    else:
        print("No MP4 file found in Downloads!")

def launch_web_app(key):
    url_map = {
        "y": "https://www.youtube.com",
        "r": "https://www.roblox.com",
        "s": "https://open.spotify.com",
        "w": "https://web.whatsapp.com",
        "i": "https://www.instagram.com",
        "n": "https://web.snapchat.com"
    }
    if key in url_map:
        webbrowser.open(url_map[key])

def menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(0, 0, "🔥 MP4Reader Fire TV Menu 🔥\n")

    row = 2
    stdscr.addstr(row, 0, "V - Play first MP4 in Downloads")
    row += 2
    for key, name in WEB_APPS.items():
        stdscr.addstr(row, 2, f"{key.upper()} - {name}")
        row += 1
    stdscr.addstr(row+1, 0, "Q - Quit")

    stdscr.refresh()

    video_file = find_mp4()

    while True:
        key = stdscr.getkey().lower()
        if key == "v":
            play_video(video_file)
        elif key in WEB_APPS:
            launch_web_app(key)
        elif key == "q":
            break
