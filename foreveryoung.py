import time
import sys

lyrics = [
    ("Forever young", 0.12),
    ("I want to be forever young", 0.11),
    ("Do you really want to live forever", 0.11),
    ("Forever", 0.12),
    ("Or never?", 0.12),
]

delays = [2.8, 4.1, 2.6, 1.4, 2.5]

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
