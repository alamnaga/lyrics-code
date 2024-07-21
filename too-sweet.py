import time
import sys

lyrics = [
    ("My coffee black and my bed at three", 0.11),
    ("You're too sweet for me", 0.14),
    ("You're too sweet for me", 0.14),
    ("I take my whiskey neat", 0.14),
    ("My coffee black and my bed at three", 0.12),
    ("You're too sweet for me", 0.12),
    ("You're too sweet for me", 0.12),
]

delays = [4.0, 4.0, 4.0, 4.0, 1.5, 4.0, 1.5]

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
