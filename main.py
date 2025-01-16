import random
import time

# List of words for the typing game
data = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xylophone", "yellow", "zucchini", "animal", "bird", "cat", "dog", "elephant", "fox",
    "giraffe", "horse", "iguana", "jaguar", "kangaroo", "lion", "monkey", "newt", "ostrich", "penguin",
    "quail", "rabbit", "snake", "tiger", "urchin", "vulture", "whale", "xerus", "yak", "zebra",
    "book", "chair", "desk", "eraser", "folder", "glue", "highlighter", "ink", "journal", "keyboard",
    "lamp", "monitor", "notebook", "organizer", "pen", "quill", "ruler", "stapler", "tape", "umbrella",
    "vase", "wallet", "xylograph", "yarn", "zipper", "astronomy", "biology", "chemistry", "drama", "economics",
    "finance", "geography", "history", "informatics", "judo", "karate", "linguistics", "mathematics", "nutrition", "oceanography",
    "philosophy", "quantum", "robotics", "sociology", "technology", "urbanism", "virology", "writing", "xenobiology", "yoga", "zoology"]

# Function to calculate words per minute
def calculate_wpm(typed_text, elapsed_time):
    num_words = len(typed_text.split())
    wpm = (num_words / elapsed_time) * 60
    return round(wpm)

# Function to calculate accuracy
def calculate_accuracy(quote, typed_text):
    correct_chars = sum(1 for i, j in zip(quote, typed_text) if i == j)
    accuracy = (correct_chars / len(quote)) * 100 if len(quote) > 0 else 0
    return round(accuracy)

# Main function for the typing game
def monkeytype():
    print('''

 ███▄ ▄███▓ ▒█████   ███▄    █  ██ ▄█▀▓█████▓██   ██▓▄▄▄█████▓▓██   ██▓ ██▓███  ▓█████
▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █  ██▄█▒ ▓█   ▀ ▒██  ██▒▓  ██▒ ▓▒ ▒██  ██▒▓██░  ██▒▓█   ▀
▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒▓███▄░ ▒███    ▒██ ██░▒ ▓██░ ▒░  ▒██ ██░▓██░ ██▓▒▒███
▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒▓██ █▄ ▒▓█  ▄  ░ ▐██▓░░ ▓██▓ ░   ░ ▐██▓░▒██▄█▓▒ ▒▒▓█  ▄
▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░▒██▒ █▄░▒████▒ ░ ██▒▓░  ▒██▒ ░   ░ ██▒▓░▒██▒ ░  ░░▒████▒
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒   ▒ ░░      ██▒▒▒ ▒▓▒░ ░  ░░░ ▒░ ░
░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒ ▒░ ░ ░  ░▓██ ░▒░     ░     ▓██ ░▒░ ░▒ ░      ░ ░  ░
░      ░   ░ ░ ░ ▒     ░   ░ ░ ░  ░      ░   ▒ ▒ ░░    ░       ▒ ▒ ░░  ░░          ░
       ░       ░ ░           ░ ░  ░      ░  ░░ ░               ░ ░                 ░  ░
                                             ░ ░               ░ ░
''')
    print("Type as fast as you can. Type 'quit' to stop the game.")

    total_accuracy = 0
    total_wpm = 0
    total_words = 0
    word_count = 0

    for _ in range(30):
        quote = random.choice(data)
        print(quote)

        start_time = time.time()
        typed_text = input()
        end_time = time.time()
        elapsed_time = end_time - start_time

        if typed_text.lower() == 'quit':
            break

        accuracy = calculate_accuracy(quote, typed_text)
        wpm = calculate_wpm(typed_text, elapsed_time)

        print("next word: ")

        total_accuracy += accuracy
        total_wpm += wpm
        total_words += 1
        word_count += 1

    if total_words > 0:
        average_accuracy = total_accuracy / total_words
        average_wpm = total_wpm / total_words
        print(f"Statistics after {word_count} words:")
        print(f"Average accuracy: {average_accuracy}%")
        print(f"Average words per minute: {average_wpm}")
    else:
        print("No words typed. Please try again.")

if __name__ == "__main__":
    monkeytype()
