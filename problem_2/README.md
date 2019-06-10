# 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

```python
digits_to_letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}
```

## Example
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

## Note

Although the above answer is in lexicographical order, your answer could be in any order you want.

## Communication Steps
* What do you still need to clarify about: inputs, outputs, etc?
    1. Should I return a list of strings representing the results?
    2. If there are duplicates, should I add them to the results?
* What are some reasonable assumptions about each?
    1. I should return a list of strings.
    2. I should not return duplicates.
* Assuming your assumptions are good, what are some good examples to test your finished algorithm against?
    1. Input: "23"  
       Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    2. Input: "92"  
       Output: ["wa", "wb", "wc", "xa", "xb", "xc", "ya", "yb", "yc", "za", "zb", "zc"]
    3. Input: "2"  
       Output: ["a", "b", "c"]
* Psuedocode
    1. define a dictionary of digits_to_letters for mapping which digit maps to a list of letters
    2. define an empty result list
    3. create a helper function that takes a current memoization of a result string (starting as "") as the first argument and a string of digits as the second argument
    4. inside the function, the function will add the first argument to the result list if the second argument is empty
    5. otherwise, loop over characters in the digits_to_letter at the key of the first digit in the digits (second argument)
    6. each iteration, recursively call the function with the first argument as the current first argument + current loop character and the second argument as the second argument excluding the first element