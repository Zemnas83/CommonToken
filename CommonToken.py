import nltk, sys
from nltk.tokenize import TweetTokenizer
import string
from collections import Counter

def tokenize_and_count(filename):  # Renamed this function
    tokenizer = TweetTokenizer()
    
    with open(filename, 'r') as fn:
        content = fn.read().lower()
        
        tokens = [token for token in tokenizer.tokenize(content) if token not in string.punctuation]
        word_freq = Counter(tokens)
    
    return word_freq


def main():
    if len(sys.argv) != 2:
        print("Usage: python CommonToken.py <filename.txt>")
        return
    
    filename = sys.argv[1]
    word_freq = tokenize_and_count(filename)  # This call matches the function name now
    
    # Print word frequencies in decreasing order
    for word, freq in word_freq.most_common():
        print(f"{word}    {freq}")

if __name__ == "__main__":
    main()
