# Input- 
# file
# Output-
# 1. number of cahracters in the file
# 2. number of lines 
# 3. number of words (seperated by a space)
import sys
from a5_bus_log import cahracters_counter

def main() :
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]
    counter, total_character, total_lines, total_words = cahracters_counter(filename)
    display_character(counter, total_character, total_lines, total_words)

def display_character(counter, total_character, total_lines, total_words) :
    print(f"Histogram of Characters: \n\
{counter} \n\
\n\
Total number of Characters: {total_character} \n\
Total number of Lines: {total_lines} \n\
Total number of Words: {total_words} \n")

main()