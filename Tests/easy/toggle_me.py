"""
Problem Statement
Cody is very irritating child. He always change the characters in his homework, he has a trick. He change all small letter to capital and viceversa. His frinds gave him the title "The Toggle dude".One day his friends gave him some words, but he wasn't feeling well, so you have to help him converting the given Strings to Special String. The String after applying Cody's trick is called Special String.

Input
Input is a String S

Output
Print the Special String of the given String.

Constraints
1<=S length<=15

Sample Input
Dcoder123

Sample Output

dCODER123
"""

import sys

def swap_case():
    s = input()

    try:
        s = str(s)
    except:
        sys.exit(0)

    swapped = []

    for char in s:
        if char.islower():
            swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)

    print(''.join(swapped))

swap_case()