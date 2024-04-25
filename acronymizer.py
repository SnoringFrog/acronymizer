#/usr/bin/python3

# TODO: 
# Could this be a Haskell thing?
# Bash version might get around Swisslog comp's weird lag with python
# Retina version would be cool, though options might be difficult
#   Could use a controller program to handle options?
#
# Accept input from stdin or from file 
#
# There are probably issues with punctuation, esp words that contain dots/hyphens/etc
#
# Flags for capitalization
#   - All caps
#   - All lowercase
#   - Preserve from input
#   - Alternate? Randomize?
#
# Attempt to convert digits to words?
#   - Issue might be determining how many words per number
#       - E.g., 1000 = two words; 45 = one word; 452 = three words

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input string to be acronymized")
args = parser.parse_args()

input_string = args.input

# Filter input. Remove punctuation, handle digits, etc
def filter(input_string):
    # TODO: Replace any whitespace with just a space? And replace multiple spaces with one space?

    # Filter out punctuation
    filtered = re.sub(r'[^A-Za-z0-9\s]', '', input_string)
    return filtered

def acronymize(filtered_input_string):
    # Replace words with just their first letter
    output = re.sub(r'([A-Za-z])[A-Za-z]*\s*', r'\1', filtered_input_string)

    # Replace numbers with just their first digit
    # Yes, this could easily be in the first regex, but separating it now is probably
    #   better for extra number handling down the line
    output = re.sub(r'([0-9])[0-9]*\s*', r'\1', output)

    # TODO:
    # For now, just hardcode capitalization
    # In the future, this should be a function that considers program options
    output = output.upper()

    return output

# Main program 
print(acronymize(filter(input_string)))
