def bubble_sort(nums):

    last = len(nums)
    while last > 1:
        for i in range(last - 1):
            a, b = nums[i], nums[i+1]
            if a > b:
                nums[i], nums[i+1] = b, a
        last -= 1

    return nums
