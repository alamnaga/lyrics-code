import time
import sys

lyrics = [
    ("Waiting to time, will I be better or fall?", 0.12),
    ("Play a lovely melody or nothing at all", 0.12),
    ("Seeking my pride when there else nothing to hide", 0.12),
    ("Let me just waking up together with you", 0.10),
]

delays = [4.5, 4.1, 3.6, 3.4]

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
