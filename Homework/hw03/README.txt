This program should be run with Python 3.xx -- dependencies are on sys and time modules.
It does not compute the suffix array, and the suffix array of T must be inputted. 


To run, use the following command:

python bwt_testing.py <pattern txt file> <T txt file> <suffix array txt file>

all on the same line. The pattern file must come first. This program writes the running
time to a file called runtime.txt. Example output of the file is below:



BWT: T G G A C ... G T G C A

C: {'A': 1, 'C': 75245, 'G': 149853, 'T': 224902, '$': 0} 

OCC: 0 0 0 0 0 ... 75098 75099 75099 75099 75099

Total: 1:  1388




For running, e.g.:

python bwt_testing.py P1.txt T1.txt T1_suffix_array.txt
