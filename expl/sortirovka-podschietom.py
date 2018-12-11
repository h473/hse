nList = list(map(int, input().split()))
nums = [0] * 101
for now in nList:
    nums[now] += 1
for num in range(len(nums)):
    for i in range(nums[num]):
        print(num, end=" ")
