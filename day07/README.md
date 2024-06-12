This program searches the NCBI website for nucleotide sequences of organisms and saves them.

Input:

- Initial letters of the file name as they appear on NCBI.
- Desired number of the first files found by the web.

Output:

- Each file is saved separately in the directory "data_ncbi".
- The search details are recorded as a line in the CSV file "searches.csv" in the format:
date, term, max, total