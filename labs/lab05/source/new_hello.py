from termcolor import colored
import time


def colorful_print(text):
    colors = ["green", "red", "blue", "magenta", "yellow"]

    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(colored(char, color, force_color=True), end="", flush=True)
        time.sleep(0.15)

    print()


if __name__ == "__main__":
    colorful_print("h3ll0 mY app-$ec w0rld...")
