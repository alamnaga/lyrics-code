import time
import sys

lyrics = [
    ("Aku bukanlah Superman", 0.15),
    ("Aku juga bisa nangis", 0.12),
    ("Jika kekasih hatiku", 0.15),
    ("Pergi meninggalkan aku", 0.12),
]

delays = [4.0, 3.5, 3.8, 3.8]

def animate_text(text, char_delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    for i, (text, char_delay) in enumerate(lyrics):
        animate_text(text, char_delay)
        if i < len(lyrics) - 1:
            next_line_delay = max(0, delays[i] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()
