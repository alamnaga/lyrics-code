import time
import sys

lyrics = [
    ("Oh bahagia aku saat engkau", 0.20),
    ("Menggenggam kedua tanganku", 0.16),
    ("Berdetak deras jantungku tak berdaya", 0.16),
    ("Lemah semua syaraf nadiku.", 0.16),
]

delays = [3.5, 3.0, 2.5, 2.0]

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
