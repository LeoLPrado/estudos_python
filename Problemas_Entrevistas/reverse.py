nums = [1, 2, 3, 4, 5, 6, 7]
k = -3

def rotate(nums, k) -> list:
    new_list = []
    nums = nums.copy()

    if k > 0:
        for i in range(k):
                last_num = nums.pop()
                new_list.append(last_num)
        new_list.reverse()
        final_list = new_list + nums
        return final_list
    
    elif k < 0:
        for i in range(k * -1):
            first_num = nums.pop(0)
            new_list.append(first_num)
        final_list = nums + new_list
        return final_list
    
    else:
        return nums

print(rotate(nums, k))
print(nums)