def letter_combinations(digits):

    # dictionary mapping digits to a list of letters
    letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    # results list
    results = []

    # helper function that will be called recursively to
    # generate combinations/permutations
    def find_permutations(memo, next_digits):

        # base case to stop recuring,
        # no next digits
        if not next_digits:
            results.append(memo)
            return
        else:

            # loop over letters for current digit
            for letter in letters[next_digits[0]]:

                # continue to next digit
                find_permutations(memo+letter, next_digits[1:])

    # find permutations
    find_permutations("", digits)

    # return result list
    return results


## TEST ##
test_cases = [
    ("23",
     ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("92",
     ["wa", "wb", "wc", "xa", "xb", "xc", "ya", "yb", "yc", "za", "zb", "zc"]),
    ("2",
     ["a", "b", "c"])
]
for case in test_cases:
    print("\nInput: {}".format(case[0]))
    print("Expected Output: {}".format(case[1]))
    print("Actual Output: {}\n".format(letter_combinations(case[0])))
