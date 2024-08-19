import time
import sys

lyrics = [
    ("I loved you from the start", 0.11),
    ("So it breaks my heart", 0.08),
    ("When you say I'm just a friend to you", 0.08),
    ("Cause friends don't do the things we do", 0.08),
    ("Everybody knows you love me too", 0.15),
]

delays = [3.0, 3.0, 2.1, 2.2, 2.5]

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
