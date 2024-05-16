#!/usr/bin/python3

# TODO: 
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

parser = argparse.ArgumentParser(description="Make acronymns/initialisms from input")
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
    # Replace numbers with just their first digit
    # Yes, this could easily be in the other regex, but separating it now is probably
    #   better for extra number handling down the line
    output = re.sub(r'([0-9])[0-9]*\s*', r'\1', filtered_input_string)

    # Replace words with just their first letter
    output = re.sub(r'([A-Za-z])[A-Za-z]*\s*', replace, output)
    #output = re.sub(r'([A-Za-z])[A-Za-z]*\s*', lambda x: x.group(1).upper(), filtered_input_string)

    return output

def replace(match):
    # TODO:
    # For now, just hardcode capitalization
    # In the future, handle this properly with options 
    the_case = "upper"

    if the_case == "upper":
        return match.group(1).upper() 
    elif the_case == "lower":
        return match.group(1).lower()
    else:
        return match.group(1)

# Main program 
print(acronymize(filter(input_string)))
