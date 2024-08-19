import time
import sys

lyrics = [
    ("Sayang, apa kabar denganmu?", 0.08),
    ("Di sini ku merindukan kamu", 0.08),
    ("Kuharap cintamu takkan berubah", 0.08),
    ("Kar'na di sini ku tetap untukmu", 0.08),
]

delays = [2.5, 2.5, 2.5, 2.5]

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
