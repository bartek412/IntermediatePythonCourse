import itertools as it

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
for notes_permutation in it.permutationsg(notes, 4):
    print(notes_permutation)