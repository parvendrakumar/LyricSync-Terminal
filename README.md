🎵 LyricSync Terminal — Real-Time Lyrics in Your Command Line

LyricSync Terminal is a sleek Python-based CLI tool that transforms your terminal into a live lyrics display system.
Just enter a song name, and watch the lyrics appear line-by-line in sync — like a mini karaoke right inside your terminal!
✨ Key Features

🔍 Smart Lyrics Fetching — Retrieves accurate lyrics using the Google Custom Search API (AZLyrics, Genius, etc.).

⏱️ Real-Time Display — Displays each line with smooth timed animation for a karaoke-like feel.

💻 Terminal-First Experience — Lightweight and compatible across Windows, macOS, and Linux.

⚙️ Fully Configurable Speed — Adjust display timing to match song rhythm.

🧠 Clean and Minimal Interface — Focused purely on lyrics, distraction-free.

🌍 Multi-Source Support — Pulls lyrics from multiple trusted sources to ensure reliability.
🚀 How It Works

You run the program in your terminal.

Enter any song name — e.g., Tum Ho Toh or Enna Sona.

The script fetches lyrics automatically using the Google Custom Search API.

Lyrics are shown gradually, line by line, with smooth delay timing.

You sing along or just enjoy watching — it’s your own CLI karaoke! 🎤

⚙️ Tech Stack

Language: Python 3.x

Libraries:

requests — for fetching lyric pages

beautifulsoup4 — for parsing HTML content

google-api-python-client — for Google Search integration

time, sys, os — for terminal display & control

🧩 Example Usage
$ python lyricsync.py
===========================================
🎧  LYRICSYNC TERMINAL - CLI KARAOKE
===========================================

Enter Song Name: Tum Ho Toh

<img width="1289" height="705" alt="image" src="https://github.com/user-attachments/assets/12fbff15-7609-4b81-b62c-bd8668ac0b57" />

#🧠 Configuration

You can easily change the display speed in the code:DISPLAY_SPEED = 0.35  # Lower = faster, Higher = slower
📦 Installation
git clone https://github.com/parvendrakumar/lyricsync-terminal.git
cd lyricsync-terminal
pip install -r requirements.txt
python lyricsync.py
🛠️ Future Plans

🎚️ Beat-based auto-sync

🎨 Colored terminal text effects

🔊 Background music playback

🎙️ Voice-command song search
📜 License

This project is licensed under the MIT License — free for use, modification, and sharing.

💬 Author

Developed with ❤️ by @erbloggerboy

Crafted for coders who love music, rhythm, and clean code. 🎧
