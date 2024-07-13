import time
import sys

lyrics = [
    ("\nCause there is something", 0.06),
    ("and there is nothing", 0.09),
    ("and there is nothing", 0.09),
    ("in-between", 0.09),
    ("And in my eyes😢", 0.10),
    ("there is a tiny dancer 💃", 0.12),
    ("watching over me 👀", 0.09),
    ("He's singing, She's a, she's a lady 🎤", 0.12),
    ("and I am just a boy 👦", 0.11),
    ("He's singing, She's a, she's a lady 🎤", 0.12),
    ("and I am just a line without a— 🎵", 0.10),
]

delays = [0.9, 0.9, 0.9, 0.9, 1.2, 1.1, 0.9, 1.2, 1.0, 1.2, 0.9]

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
