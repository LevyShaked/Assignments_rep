# Input- 
# file
# Output-
# 1. number of cahracters in the file
# 2. number of lines 
# 3. number of words (seperated by a space)

import sys

def main() :
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")
    filename = sys.argv[1]
    counter, total_character, total_lines, total_words = cahracters_counter(filename)
    display_character(counter, total_character, total_lines, total_words)

def cahracters_counter(filename) :
    total_lines = 0
    total_words = 0
    total_character = 0
    counter = {}
    with open(filename) as fh :
        for line in fh :
            line = line.rstrip()
            total_lines += 1
            words_list = line.split(' ')
            total_words += len(words_list)
            for ch in line :
                if ch == ' ' or ch == '  ' :
                    continue
                total_character += 1
                if ch not in counter :
                    counter[ch] = 1
                else :
                    counter[ch] += 1           
    return counter, total_character, total_lines, total_words

def display_character(counter, total_character, total_lines, total_words) :
    print(f"Histogram of Characters: \n\
{counter} \n\
\n\
Total number of Characters: {total_character} \n\
Total number of Lines: {total_lines} \n\
Total number of Words: {total_words} \n")

main()