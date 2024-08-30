import time
import sys


lyrics = [
    ("\nIf the world was ending, I'd wanna be next to you...", 0.10),
    ("If the party was over, And our time on Earth was through", 0.12),
    ("I'd wanna hold you just for a while...... And die with a smile....", 0.11),
    ("If the world was ending, I'd wanna be next to you...", 0.13),
]

delays = [8.8, 8.8, 8.1, 6.1]

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
            # Calculate the time until the next line should start
            next_line_delay = max(0, delays[i] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()
