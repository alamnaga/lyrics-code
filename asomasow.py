import time
import sys


lyrics = [
    ("\nAsomasow", 0.09),
    ("I got me a therapist to tell me", 0.05),
    ("there's other men", 0.05),
    ("I don't want none, I just want you", 0.04),
    ("If I can't have you, no one should", 0.04),
    ("\nI might", 0.09),
    ("I might kill my ex, not the best idea", 0.11),
    ("His new girlfriend's next, how'd I get here?", 0.11),
]


delays = [1.0, 1.0, 1.5, 1.5, 1.8, 1.5, 1.5, 1.2]

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
