import itertools as it

'''
These are the solutions for the n queens problem on Coursera course for 'What is a Proof?'
'''


# Brute force solution
def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True


for brute_perm in it.permutations(range(10)):
    if is_solution(brute_perm):
        print(brute_perm)
        break


# Backtracking solution
def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()


extend([], 10)




