All three outputs for the problem 1 parts are included. It can be run on arctic using the command python. For example:

python problem_1_A.py counts1.txt
python problem_1_B.py params.txt counts2.txt
python problem_1_C.py counts3.txt

(python3 should not be used as the command -- I tested for python and it worked fine!)


For the EM:

* I use numpy random to initialize parameters. I then set my max iteration to 30 and my threshold to 0.01
* I transform counts to log space and add up the probabilities for each roll for a parameter, and then divide by the total probability for actual parameters. I do the same for the parameters for each die. 
* I add these to my lists and compute a new loglikelihood. 
* If the absolute difference between my old loglik (originally 0) and my new is less than or equal to my threshold, I have converged and break the algorithm. 


Thanks for a great semester! (I got help about EM from this site http://www.cs.cmu.edu/~bhiksha/courses/mlsp.fall2016/www/slides/Lecture15.expectationmaximization.CMU.pdf)