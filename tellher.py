import time
import sys

lyrics = [
    ("Girl, please tell me what to do", 0.11),
    ("Everything seems right", 0.12),
    ("Whenever I'm with you", 0.12),
    ("So girl, won't you tell me", 0.12),
    ("How to tell her about you?", 0.12),
]

delays = [5.7, 2.6, 7.6, 4.4, 2.5]

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
