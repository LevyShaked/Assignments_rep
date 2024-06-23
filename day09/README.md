This program excepts a file from ncbi
find its sequence part

and analyze it by 2 optional tools:

1. "duplicate": The longest sequence that repeate itself, and its length
2. "letter dulicate": The longest sequence constructed from only one chosen letter A|C|T|G and its length

input :

`python3 analyze.py data_from_ncbi_file --duplicate --letter_duplicate A|C|T|G

exaple: 

python3 analyze.py ID_NM_001410955.1.data --duplicate --letter_duplicate A