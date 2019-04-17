"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as corpus:
        first_corpus = corpus.read()

    with open(file_path2) as corpus2:
        second_corpus = corpus2.read()

    return first_corpus + second_corpus


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    text_string = text_string.split()
    # Start with first word, loop from seocond word to end. 
 
    chains = {}
    
    for i in range(len(text_string) - 2):
        current_tuple = (text_string[i], text_string[i + 1])

        if chains.get(current_tuple, 0) == 0:
            chains[current_tuple] = [text_string[i + 2]]
        else:
            chains[current_tuple].append(text_string[i + 2])


    return chains


def make_text(chains):
    """Return text from chains."""
    
    counter = 0
    output_words = []
    # random key from chains
    key_pair = choice(list(chains))
    check_word = key_pair[0]
    while check_word[0].isupper() == False:
        key_pair = choice(list(chains))
        check_word = key_pair[0]

    output_words.append(key_pair[0])
    output_words.append(key_pair[1])
    
    try:
        while True:
            word = choice(chains[key_pair])     
            output_words.append(word)
            key_pair = (key_pair[1], word)
            # if word has punctuation, increase counter
            if word[-1] in ['!', '.', '?']:
                counter += 1
                if counter == 10:
                    break
    except:
        return " ".join(output_words)
    
    return " ".join(output_words)

input_path = sys.argv[1]

input_path2 = sys.argv[2]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path, input_path2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

print(sys.argv[1])

print("Number of arguments: " + str(len(sys.argv)))