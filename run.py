from __future__ import print_function
from __future__ import division  # this ensures the / operation give floats by default
import itertools
import random
from collections import Counter


def evaluate_guess(guess, c=None):
    '''
    This function compares a guess and a code and returns (numCorrect,numTransposed)
    which correspond to the number of black and white pegs returned in Mastermind.
    The code is a global variable, which the KnuthFive() function cannot use.
    '''
    global code

    if c == None:
        c = code

	# Get the length n of the guess and the code.
    assert(len(guess) == len(c))
    n = len(guess)

    # Determine the correct and incorrect positions.
    correct_positions = [i for i in list(range(n)) if guess[i] == c[i]]
    incorrect_positions = [i for i in list(range(n)) if guess[i] != c[i]]
    num_correct = len(correct_positions)

    # Reduce the guess and the code by removing the correct positions.
    # Create the set values that are common between the two reduced lists.
    reduced_guess = [guess[i] for i in incorrect_positions]
    reduced_code = [c[i] for i in incorrect_positions]
    reduced_set = set(reduced_guess) & set(reduced_guess)

    # Determine the number of transposed values.
    num_transposed = 0
    for x in reduced_set:
    	num_transposed += min(reduced_guess.count(x), reduced_code.count(x))

    return num_correct, num_transposed


def KnuthFive():
    '''
    Implement Knuth's algorithm here.
    You cannot use the global variable code.
    '''


    S = [tuple(x) for x in itertools.product(range(1,7), repeat=4)]
    R = [tuple(x) for x in itertools.product(range(1,7), repeat=4)]

    guess = (1,1,2,2)
    R.remove(guess)
    guessList = [guess]
    num_correct, num_transposed = evaluate_guess(guess)

    while num_correct != 4:
        # remove impossible codes
        newS = []
        for s in S:
            if evaluate_guess(guess, s) == (num_correct, num_transposed):
                newS.append(s)
            else:
                continue
        S = newS

        if len(S) == 1:
            guessList.append(S[0])
            break

        # find next guess with maximum score
        # possible guesses
        scores = []
        for r in R:
            r_hits = []
            # code possibilities
            for s in S:
                x = evaluate_guess(r, s)
                r_hits.append(x)

            mode, mode_num = Counter(r_hits).most_common(1)[0]
            score = len(S) - mode_num
            scores.append(score)

        max_score = max(scores)
        guess = R[scores.index(max_score)]
        guessList.append(guess)
        num_correct, num_transposed = evaluate_guess(guess)
    return guessList


if __name__ == "__main__":
    global code
    # Create all 1296 possible Mastermind codes.
    allCodes = [tuple(x) for x in itertools.product(range(1,7), repeat=4)]

    # Initialize statistics.
    totalSolved = 0    # number of the 1296 codes that you solved
    totalUnsolved = 0  # number of the 1296 codes that you didn't solve
    worstCase = 0      # largest number of guesses used to solve a code
    totalGuesses = 0   # total number of guesses used to solve all solved codes

    for code in allCodes:
        print("\n", code)
        guessList = KnuthFive()
        if guessList[-1] == code:
            totalSolved += 1
            numGuesses = len(guessList)
            worstCase = numGuesses if numGuesses > worstCase else worstCase
            totalGuesses += numGuesses
        else:
            totalUnsolved += 1

    print("total solved: %d" % totalSolved)
    print("worst case: %d" % worstCase)
    print("average: {}".format(totalGuesses/totalSolved))
    print("total unsolved: %d" % totalUnsolved)
