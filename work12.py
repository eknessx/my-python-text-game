import random
import emoji

def random_emoji():
    # Generate a random emoji from the Unicode range for emojis
    return emoji.emojize(chr(random.randrange(0x1F600, 0x1F64F)))

def random_words():
    # Generates a random list of words that can be turned into a random sentence
    
    return random.choices(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], k=5)

# Print a random emoji to the terminal
if __name__ == "__main__":
    print(random_words())
    print(random_emoji())
