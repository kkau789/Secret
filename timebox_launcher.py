import os
import time
import webbrowser

# ===== Config =====
BOOT_VIDEO = "party_video.mp4"  # your MP4 in Termux home
BOOT_DURATION = 10  # seconds to play boot video (Timebox style)
APPS = {
    "1": ("YouTube", "https://youtube.com"),
    "2": ("Roblox", "https://roblox.com"),
    "3": ("WhatsApp Web", "https://web.whatsapp.com"),
    "4": ("Spotify", "https://spotify.com"),
    "5": ("Instagram", "https://instagram.com")
}

# ===== Functions =====
def play_boot_video():
    """Play MP4 using Termux Media Player for a fixed duration."""
    print(f"🎬 Playing boot video for {BOOT_DURATION} seconds...")
    os.system(f"termux-media-player play {BOOT_VIDEO}")
    time.sleep(BOOT_DURATION)  # wait for the timebox duration
    os.system("termux-media-player stop")
    print("Boot video finished.\n")

def show_menu():
    """Display menu and get user selection."""
    print("=== Party TV Menu ===")
    for key, (name, _) in APPS.items():
        print(f"{key}. {name}")
    choice = input("Select an app by number: ").strip()
    return APPS.get(choice)

def open_app(url):
    """Open URL in Android browser."""
    webbrowser.open(url)

# ===== Main Launcher =====
def main():
    play_boot_video()
    while True:
        option = show_menu()
        if option:
            name, url = option
            print(f"Opening {name}...\n")
            open_app(url)
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
