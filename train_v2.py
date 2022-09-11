import itertools


def main():
    nums = [int(n) for n in input("Enter your numbers: ").split()]
    ans = []
    target = int(input("Input your target: "))

    def backtrack(perm, curr, ops, i):
        if len(ops) == len(nums):
            if (curr == target):
                ans.append(ops)
            return
        else:
            v = perm[i]

            for o in ['+', '-', '*', '/']:
                if o == '+':
                    backtrack(perm, curr + v, ops + [f" + {v}"], i + 1)
                elif o == '-':
                    backtrack(perm, curr - v, ops + [f" - {v}"], i + 1)
                elif o == '*':
                    backtrack(perm, curr * v, ops + [f" * {v}"], i + 1)
                elif o == '/':
                    backtrack(perm, curr / v, ops + [f" / {v}"], i + 1)

    # Generate all permutations of the nums.

    perms = list(itertools.permutations(nums))
    for p in perms:
        backtrack(p, p[0], [p[0]], 1)

    if len(ans) > 0:
        for a in set([''.join(str(a)) for a in ans]):
            print(a)
    else:
        print("There are no valid solutions :(")


if __name__ == "__main__":
    main()
