from itertools import permutations

def all_permutations(s):
    perm_list = permutations(s)
    for perm in perm_list:
        print("".join(perm))

s = input("Enter a string:")
all_permutations(s)