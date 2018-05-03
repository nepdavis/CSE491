This program should be run with Python 3.xx -- dependencies are on sys and time modules.


To run, use the following command:

python hirschberg.py <file one> <file two> <match value> <mismatch value> <gap value>

all on the same line.



This file outputs the optimal score and run time. This algorithm takes O(mn) time
and O(min(m, n)) space (linear space).


It achieves linear space by only using the previous row to create a new row, and then
re-initializes the previous row as the new row, and moves on to the next iteration of the loop.
This keeps track of two full rows at maximum, and returns the previous row for the Hirschberg search.



For running, e.g.:

python hirschberg.py t1.txt s1.txt 2 -1 -1