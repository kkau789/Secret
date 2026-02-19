import av
import time
import os
import webbrowser

# ===== Config =====
BOOT_VIDEO = "party_video.mp4"  # Name of your downloaded MP4 in Termux home

MENU_OPTIONS = {
    "1": ("YouTube", "https://youtube.com"),
    "2": ("Roblox", "https://roblox.com"),
    "3": ("WhatsApp Web", "https://web.whatsapp.com"),
    "4": ("Spotify", "https://spotify.com"),
    "5": ("Instagram", "https://instagram.com")
}

# ===== Functions =====
def play_video(file_path):
    """Play video using PyAV (simulated frame playback in terminal)."""
    if not os.path.exists(file_path):
        print(f"Boot video not found: {file_path}")
        return
    try:
        container = av.open(file_path)
        print(f"\n🎬 Playing boot video: {file_path}\n")
        for frame in container.decode(video=0):
            # Terminal simulation; sleep to mimic FPS
            time.sleep(1/30)
    except Exception as e:
        print(f"Error playing video: {e}")

def show_menu():
    """Display main menu and get user choice."""
    print("\n=== Main Menu ===")
    for key, (name, _) in MENU_OPTIONS.items():
        print(f"{key}. {name}")
    choice = input("\nSelect an app by number: ").strip()
    return MENU_OPTIONS.get(choice)

def open_app(url):
    """Open a URL in the real browser using Termux."""
    try:
        os.system(f'xdg-open "{url}"')  # Termux default browser
    except:
        webbrowser.open(url)

# ===== Main Launcher =====
def main():
    play_video(BOOT_VIDEO)
    while True:
        option = show_menu()
        if option:
            name, url = option
            print(f"\nOpening {name}...\n")
            open_app(url)
        else:
            print("\n❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
