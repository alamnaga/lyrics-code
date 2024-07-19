import time
import sys

lyrics = [
    ("And I, I cannot lose you again", 0.13),
    ("There's something so special about you", 0.10),
    ("And I can't shake this great feeling", 0.10),
    ("I don't wanna lose 😢", 0.04),
    ("I don't wanna leave 😢", 0.04),
    ("Tell me everything 🗣️", 0.04),
    ("we could be 💭", 0.05),
    ("I just want somebody 👫", 0.05),
    ("that'll love me ❤️", 0.05),
    ("Baby, tell me everything 🗣️", 0.04),
    ("we can see 🌟", 0.05),
]

delay = [1.5, 0.9, 5.1, 0.5, 0.5, 0.8, 0.5, 0.5, 0.5, 0.5]

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
            next_line_delay = max(0, delay[i % len(delay)] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()
