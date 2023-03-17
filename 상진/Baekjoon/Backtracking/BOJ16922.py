N = int(input())
nums = [1,5,10,50]

total_ans = set()
ans = []

def dfs(idx):
    if len(ans) == N:
        total_ans.add(sum(ans))
        return
    for i in range(idx,4):
        ans.append(nums[i])
        dfs(i)
        ans.pop()

dfs(0)
print(len(total_ans))