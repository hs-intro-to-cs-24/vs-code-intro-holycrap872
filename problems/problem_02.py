#!/usr/bin/env python3


def first_and_last_letter(word):
    """
    This function returns the first and last letter of a word. Note: if the
    word is too short, the the function returns "too short".

    :param word: The word to slice
    """
    # Replace the code below with your own code
    if len(word) < 2:
        return "too short"

    return word[0] + word[-1]

# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
total_wrong = 0

# Test 1
ret = first_and_last_letter("y")
if ret != "too short":
    print('Test 1: Uh oh, "y" returned', ret)
    total_wrong = total_wrong + 1


# Test 2
ret = first_and_last_letter("")
if ret != "too short":
    print('Test 2: Uh oh, "" returned', ret)
    total_wrong = total_wrong + 1


# Test 3
ret = first_and_last_letter("umbrella")
if ret != "ua":
    print('Test 3: Uh oh, "umbrella" returned', ret)
    total_wrong = total_wrong + 1


# Test 4
ret = first_and_last_letter("yolo")
if ret != "yo":
    print('Test 4: Uh oh, "yolo" returned', ret)
    total_wrong = total_wrong + 1


if total_wrong == 0:
    print("Overall: Woohoo! All tests have been passed for Problem 2!")
else:
    print("Overall: There's still work to do!")
