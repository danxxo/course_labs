import sys
import time


def colorful_print(text):
    colors = ["\033[92m", "\033[91m", "\033[94m", "\033[95m", "\033[93m"]
    reset = "\033[0m"
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(0.4)
    print()


if __name__ == "__main__":
    colorful_print("hello appsec world")