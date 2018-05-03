This is a program to read in .fa files and ouput overlap alignments for each pair of sequences.

The program should be run in Python3

Example input:

    python olc.py <.fa> <length> <score> <mask (0/1)>
    
    
    
The output would then be each pair of sequence titles and their number of edges from the alignment. If mask of 1 is inputted, then the pairs will also have the actual overlap alignment sequences printed with the edges between them.