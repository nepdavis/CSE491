The hmm_viterbi.py file can be run on arctic using the following command (using example.fa for example):

python hmm_viterbi.py example.fa example.hmm

(You do not need to use python3 command, python works and is what I used)


The output file is named after the data you input. There is an output uploaded for both the example.fa and the mjann.fa.

I found 472 state B's in the example.fa. I found 25 state B's in the mjann.fa (e.g. the tRNA positions!)


***The program takes a few seconds to run on arctic (it is a little slower on the server than it is locally***


This was the closest I could get to the actual states. I tested these outputs against Dr. Ben Langmeads outputs with his file from this link (http://nbviewer.jupyter.org/gist/BenLangmead/7460513), and they were identical. MY CODE IS VERY DIFFERENT THAN HIS AND WAS ALREADY WRITTEN BEFORE I FOUND HIS (his is also much faster). Thanks for a great semester!