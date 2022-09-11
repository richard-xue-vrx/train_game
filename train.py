
def main():
    nums = [int(n) for n in input("Enter your numbers: ").split()]
    ans = []
    target = int(input("Input your target: "))

    def backtrack(curr, ops, i):
        if len(ops) == len(nums) - 1:
            if (curr == target):
                ans.append(ops)
            return
        else:
            v = nums[i]

            for o in ['+', '-', '*', '/']:
                if o == '+':
                    backtrack(curr + v, ops + ['+'], i + 1)
                elif o == '-':
                    backtrack(curr - v, ops + ['-'], i + 1)
                elif o == '*':
                    backtrack(curr * v, ops + ['*'], i + 1)
                elif o == '/':
                    backtrack(round(curr / v), ops + ['/'], i + 1)

    # for n in nums:
        #backtrack(n, [], 1)
    backtrack(nums[0], [], 1)
    print(ans)
    for a in ans:
        v = []
        for i in range(len(a)):
            v += [nums[i]]
            v += [a[i]]
        v += [nums[len(a)]]
        print(v)


if __name__ == "__main__":
    main()
