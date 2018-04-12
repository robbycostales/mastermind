from __future__ import print_function
from __future__ import division  # this ensures the / operation give floats by default
import itertools


def evaluate_guess(guess):
    '''
    This function compares a guess and a code and returns (numCorrect,numTransposed)
    which correspond to the number of black and white pegs returned in Mastermind.
    The code is a global variable, which the KnuthFive() function cannot use.
    '''
    global code

	# Get the length n of the guess and the code.
    assert(len(guess) == len(code))
    n = len(guess)

    # Determine the correct and incorrect positions.
    correct_positions = [i for i in list(range(n)) if guess[i] == code[i]]
    incorrect_positions = [i for i in list(range(n)) if guess[i] != code[i]]
    num_correct = len(correct_positions)

    # Reduce the guess and the code by removing the correct positions.
    # Create the set values that are common between the two reduced lists.
    reduced_guess = [guess[i] for i in incorrect_positions]
    reduced_code = [code[i] for i in incorrect_positions]
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
    guess = (1,1,2,2)
    guessList = [guess]
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
    print("average: %d" % (totalGuesses/totalSolved))
    print("total unsolved: %d" % totalUnsolved)
