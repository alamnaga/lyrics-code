import time
import sys


lyrics = [
    ("\nEmang lagi tamvan", 0.09),
    ("Ku memang lagi tamvan 😍", 0.10),
    ("Tamvan tamvan gini", 0.10),
    ("kamu masih tak mau 😣", 0.11),
    ("Emang kamu syantik, kau benar-benar syantik 🤗", 0.10),
]

delays = [1.5, 1.1, 1.1, 1.1, 1.1]

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
