import argparse
import re
from Bio import  SeqIO

parser = argparse.ArgumentParser()

parser.add_argument('sequence_file', help="AA|AGC..",type=str)
parser.add_argument('--duplicate', action='store_true', help='Execute the longest duplicate sequence function')
parser.add_argument('--letter_duplicate', type=str, help="G|A|T|C")

args = parser.parse_args()
sequence_file = args.sequence_file 
duplicate = args.duplicate
letter_duplicate = args.letter_duplicate

def duplicate_function(sequence_file):
    sequence = ''
    file_type = "genbank"
    for seq_record in SeqIO.parse(sequence_file, file_type):
        sequence = sequence + str((seq_record.seq))   # The full sequence

    length = 0
    while True :
        length = length + 1
        match = re.search(r'([GATC]{' + str(length) +r'}).*\1', sequence)
        if match:
            word = match.groups()
        else :
            print('duplicate_function: ')
            print(f'Length of repeated part= {length-1}')
            print(f'Sequence part = {word}')
            break

def letter_duplicate_function(sequence_file, letter_duplicate):
    sequence = ''
    file_type = "genbank"
    for seq_record in SeqIO.parse(sequence_file, file_type):
        sequence = sequence + str((seq_record.seq))   # The full sequence

    length = 0
    while True :
        length = length + 1
        match = re.search(r'([' + re.escape(letter_duplicate) + r']{' + str(length) +r'})', sequence)
        if match:
            word = match.groups()
        else :
            print('letter_duplicate_function: ')
            print(f'Length of the repeted letter sequence = {length-1}')
            print(f'Repeted letter sequence part = {word}')
            break


if duplicate :
    duplicate_function(sequence_file)

if letter_duplicate :
    letter_duplicate_function(sequence_file,letter_duplicate)

print(" ")

print("Thank you for using the app- 'the app that search things in DNA sequences' of Shaked Levy")

exit()