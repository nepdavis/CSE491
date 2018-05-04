This program implements suffix array algorithm for strings -- meant for DNA sequences (uses my own implementations of quick sort and binary search).

This program should be run with Python 3.xx -- dependencies are on sys and time modules.


To run, use the following command:

python suffix_array.py <pattern txt file> <T txt file>

all on the same line. The pattern file must come first. This will output a running time for the array creation - it is sorted using multikey quicksort. It will then output the indices of the text file where there are matches for the pattern. 


e.g.:

python suffix_array.py smallP1.txt smallT1.txt
