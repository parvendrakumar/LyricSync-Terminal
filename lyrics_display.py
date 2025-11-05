import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import time
import sys
import os
import threading

# ==============================
# 🔧 CONFIGURATION
# ==============================
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"   # Google API Key
SEARCH_ENGINE_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"                 # Search Engine ID
DISPLAY_SPEED = 0.35  # ⏱️ Delay (seconds) between lines (adjust to match song)
PLAY_MUSIC = False     # 🎵 Set to True if you want to play mp3 with lyrics

# ==============================
# 🎶 FUNCTION: FETCH LYRICS
# ==============================
def get_lyrics(song_name):
    """Fetch lyrics using Google Custom Search + scraping."""
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        res = service.cse().list(
            q=f"{song_name} site:azlyrics.com OR site:genius.com",
            cx=SEARCH_ENGINE_ID,
        ).execute()

        if "items" not in res:
            return None

        link = res["items"][0]["link"]
        print(f"\n🔗 Found source: {link}\n")

        page = requests.get(link)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, "html.parser")

        lyrics = None
        if "genius.com" in link:
            divs = soup.find_all("div", {"data-lyrics-container": "true"})
            if divs:
                lyrics = "\n".join(div.get_text(separator="\n") for div in divs)
        elif "azlyrics.com" in link:
            divs = soup.find_all("div", class_=None)
            for div in divs:
                if div.text.strip() and "Submit Corrections" not in div.text:
                    lyrics = div.text.strip()
                    break

        return lyrics

    except Exception as e:
        return f"❌ Error: {e}"

# ==============================
# 🎧 FUNCTION: PLAY SONG
# ==============================
def play_music(song_path):
    """Play MP3 file in background."""
    try:
        from playsound import playsound
        playsound(song_path)
    except Exception as e:
        print(f"⚠️ Unable to play song: {e}")

# ==============================
# 💫 FUNCTION: DISPLAY LYRICS WITH DYNAMIC TIMING
# ==============================
def display_lyrics_timed(lyrics):
    """Display lyrics line by line with timing to match song pace."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎤  Now Playing... Enjoy the Lyrics!\n")
    time.sleep(1.5)
    
    for line in lyrics.splitlines():
        clean_line = line.strip()
        if not clean_line:
            print("")
            time.sleep(0.2)
            continue
        
        print(f"🎶 {clean_line}")
        
        # ⏱️ Dynamic pauses for special lines
        if "Music" in clean_line or "ooo" in clean_line or "Ooo" in clean_line:
            time.sleep(2.5)
        elif "Enna sona" in clean_line.lower() or "aavan javan" in clean_line.lower():
            time.sleep(1.2)
        else:
            time.sleep(DISPLAY_SPEED)

# ==============================
# 🖥️ MAIN FUNCTION
# ==============================
def main():
    print("=" * 60)
    print("🎧  SONG LYRICS SYNC DISPLAY (Terminal Karaoke Mode)")
    print("=" * 60)
    song_name = input("\nEnter Song Name: ").strip()

    if not song_name:
        print("⚠️ Please enter a valid song name.")
        sys.exit(0)

    print("\n⏳ Fetching lyrics... Please wait...\n")
    lyrics = get_lyrics(song_name)

    if not lyrics:
        print("❌ No lyrics found. Try another song name.")
        return

    # Optional background music
    if PLAY_MUSIC:
        song_path = f"{song_name}.mp3"
        if os.path.exists(song_path):
            threading.Thread(target=lambda: play_music(song_path), daemon=True).start()
        else:
            print(f"⚠️ No MP3 found for {song_name}. Place it in same folder as this script.")

    display_lyrics_timed(lyrics)
    print("\n✅ Song finished! 🎵")

# ==============================
# 🚀 ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()
