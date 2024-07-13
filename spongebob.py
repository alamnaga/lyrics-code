import time
import sys

lyrics = [
    ("\nDrum tak bisa dipetik", 0.16),
    ("Gitar tak bisa digebuk", 0.17),
    ("Bukan karena tak bisa", 0.17),
    ("Tapi tak pantas", 0.12),
    ("Seperti aku dan kamu", 0.17),
    ("Bukanya aku tak mau", 0.20),
    ("Kuanggap dirimu emas", 0.18),
    ("Aku tak pantas.....", 0.19),
]

delays = [1.5, 2.8, 2.8, 5.0, 2.1, 2.8, 2.8, 2.8]

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
