import node_stack

"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #4 (25 points)
Filename: even_digits.py

Define a function named "even_digits" that declares a parameter for an 
    integer. The function should return a copy of the integer with the odd
    digits removed. You MUST NOT convert the integer to/from a string, but 
    instead may only use basic arithmetic operators (e.g. %, //, etc.).

    Given Input     Expected Output
    1               0
    2               2
    34              4
    1234567890      24680

For credit your function must use a stack or a queue in a significant way.
    You must not use any other data structures. For full credit, your 
    implementation must run in linear time.
"""

import node_stack as Stack

def even_digits(integer): #Same issue as balance_parenthesis.py, I can't get stack to work but this should work (hopefully) if the stack worked as intended
    i = 0
    nstack = Stack
    nnum = 0
    while integer > 0:
        num = integer%(10**i) #specific number based on position in integer (for 34, it would first be 0, then 4, then 34 (or 30 if you take into account subtraction on next line))
        integer -= num #subtract num number from original (if it was 34, subtract 0 to get 34, then subtract 4 to get 30, then subtract 30 to get 0)
        normnum = int(num/(10**(i-1))) #normalize the number (if it was 4 it would output 4 based on i variable, if it was 30 it would output 3 based on i variable)
        nstack.pu(normnum) #push that number into the stack
        i += 1
    
    ni = 0
    for _ in range(i):
        num = nstack.po() #take the last number (for 34 it would be a stack that looks like [4,3,0])
        if num%2 == 0:
            nnum += num*(10**ni) #add to nnum variable based on ni variable and number from stack (for 34, on the first iteration since its 4 it would pass the if statement, then do 4*10^0 = 4, and add that to nnum for 4 and + 1 on ni. if 3 was an even number, it would then do 3*(10^1) = 30 and add that to nnum for a final answer of 34 (if 3 was even (its not actually even)))
            ni += 1
    
    return nnum

def main():
    even_digits(34)

main()

# wasnt able to do tests because stack didnt work

# several test cases provided for even digits - 1, 2, 34, 1234567890
def test_even_digits_1():
    # setup
    integer = 1
    expected = 0
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_2():
    # setup
    integer = 2
    expected = 2
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_34():
    # setup
    integer = 34
    expected = 4
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_1234567890():
    # setup
    integer = 1234567890
    expected = 24680
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual