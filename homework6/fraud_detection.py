import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line


def ones_and_tens_digit_histogram(numbers):
    '''
    Input:
        a list of numbers.
    Returns:
        a list where the value at index i is the frequency in which digit i
        appeared in the ones place OR the tens place in the input list. This
        returned list will always have 10 numbers (representing the frequency
        of digits 0 - 9).

    For example, given the input list
        [127, 426, 28, 9, 90]
    This function will return
        [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]

    That is, the digit 0 occurred in 20% of the one and tens places; 2 in 30%
    of them; 6, 7, and 8 each in 10% of the ones and tens, and 9 occurred in
    20% of the ones and tens.

    See fraud_detection_tests.py for additional cases.
    '''
    histogram = [0] * 10

    # first fill histogram with counts
    for i in numbers:
        # 1's place
        histogram[i % 10] += 1

        # 10's place
        histogram[i // 10 % 10] += 1

    # normalize over total counts
    for i in range(len(histogram)):
        histogram[i] /= len(numbers) * 2

    return histogram

# Your Set of Functions for this assignment goes in here


# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.

    raise NotImplementedError("Delete this line and start writing code")


if __name__ == "__main__":
    main()
