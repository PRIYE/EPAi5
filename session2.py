# KINDLY GO THROUGH TEST FILE TO UNDERSTAND WHAT TO DO IN THIS CODE

from typing import List
import time
from hashlib import sha256
import sys

# Here in this code we will be leaking memory because we are creating cyclic reference.
# Find that we are indeed making cyclic references.
# Eventually memory will be released, but that is currently not happening immediately.
# We have added a function called "clear_memory" but it is not able to do it's job. Fix it.
# Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that
# This code is sub-optimal.

class something(object):

    def __init__(self):
        super().__init__()
        self.something_new = None


class somethingNew(object):

    def __init__(self, i: int = 0, something: something = None):
        super().__init__()
        self.i = i
        self.something = something



def add_something(collection: List[something], i: int):
    something = something()
    something.something_new = somethingNew(i, something)
    collection.append(something)

def reserved_Function():
    # to be used in future if required
    pass

def clear_memory(collection: List[somethingNew]):
    """Clears the memory by breaking the cyclic references.

    Iterates through the collection and sets the 'something_new' attribute
    of each 'Something' object to None. This breaks the reference cycle
    allowing garbage collection to reclaim the memory.
    """
    for item in collection:
        item.something_new = None
    collection.clear()


def critical_function():
    collection = list()
    for i in range(1, 1024 * 128):
        add_something(collection, i)
    clear_memory(collection)


# Here we are sub-optimally testing whether two strings are exactly same or not
# After that we are trying to see if we have a particular character in that string or not
# Currently the code is suboptimal. Write it in such a way that it takes 1/10 the current time

# DO NOT CHANGE THIS PROGRAM
def compare_strings_old(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass
    char_list = list(a)
    for i in range(n):
        if 'd' in char_list:
            pass

# YOU NEED TO CHANGE THIS PROGRAM
def compare_strings_new(n):
    """
    This code defines a function compare_strings that takes two strings as input and returns True if the strings are equal, False otherwise. 
    The function uses the sha256 hashing algorithm to create a unique hash for each string. 
    The hash is a fixed-length hexadecimal string that represents the string's content.
    If the two strings are identical, their hashes will also be identical.

    To find character 'd' in list optimal way, the string is convert into set 
    """
    a = sys.intern('a long string that is not intered' * 200)
    b = sys.intern('a long string that is not intered' * 200)
    for i in range(n):
        if a is b:
            pass
    char_list = list(set(a))
    if 'd' in char_list:
        pass
    #time.sleep(6) # remove this line, this is just to simulate your "slow" code
