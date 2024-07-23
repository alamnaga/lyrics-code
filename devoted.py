import time
import sys

lyrics = [
    ("There's nowhere to hide", 0.12),
    ("Since you pushed my love aside", 0.11),
    ("I'm out of my head", 0.12),
    ("Hopelessly devoted", 0.12),
    ("to you........", 0.16),
]

delays = [3.3, 3.1, 3.3, 3.4, 3.5]

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
