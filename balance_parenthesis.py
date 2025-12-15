
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
from node_stack import Stack #Changed method names in the node_stack.py file itself because .push() wasn't working (Nvm its not working anyways, I don't know why its not working)

#This should work hopefully, I wasn't able to test because the stack module wouldnt work

def balance_parenthesis(a_string):
    nstack = Stack
    i = 0
    for letter in a_string:
        if letter == "(" or letter == ")":
            nstack.pu(letter)
            i += 1
    
    x = 0
    lastparenthesis = 0
    for n in range(i):
        p = nstack.po()
        if p == "(":
            x += 1
        if p == ")":
            x -= 1
            lastparenthesis = i-(n+1)
    if x == 0:
        return 0
    elif x > 0:
        return lastparenthesis
    elif x < 0:
        return -1
    



def main():
    balance_parenthesis("()----)")

if __name__ == "__main__":    main()