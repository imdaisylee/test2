import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    # Easy to calculate case: 5 numbers, clean percentages.
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])

    # Obscure and hard (by hand) to calculate frequencies
    input = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
             144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    actual = fd.ones_and_tens_digit_histogram(input)
    expected = [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
                0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
                0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
                0.047619047619047616]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])

# write other test functions here


def main():
    test_ones_and_tens_digit_histogram()
    # call other test functions here


if __name__ == "__main__":
    main()
