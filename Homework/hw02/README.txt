This program should be run with Python 3.xx


To run, use the following command:

python suffix_array.py <pattern txt file> <T txt file>

all on the same line. The pattern file must come first. This will output a running time for the array creation - it is sorted using multikey quicksort. It will then output the indices of the text file where there are matches for the pattern. 


e.g.:

python suffix_array.py smallP1.txt smallT1.txt
