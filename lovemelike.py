import time
import sys

lyrics = [
    ("\nSo..... love me like there's no tomorrow ♥", 0.12),
    ("Hold me in your arms, tell me you mean it 🤝", 0.12),
    ("This is our last goodbye", 0.12),
    ("and very soon it will be over", 0.10),
    ("But today just love me like there's no tomorrow 😊", 0.0965),
]

delays = [7.5, 5.1, 3.6, 2.4, 2.5]

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
