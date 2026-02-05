nums = [1, 1, 1, 1]
#Output = 6

def pars(nums):
    Npars = 0
    i = 0
    j = len(nums) - 1

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                Npars += 1
                print(f'({i}, {j})')
            j-= 1
        i+= 1
    return Npars

print(pars(nums))