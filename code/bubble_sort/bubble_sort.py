def bubble_sort(nums, asc: bool = True):

    last = len(nums)
    while last > 1:
        [reorder(nums, i) for i in range(last-1)]
        last -= 1
    return nums if asc else nums[::-1]


def reorder(nums: [], i: int) -> None:
    a, b = nums[slice(i, i+2)]
    if a > b:
        nums[i], nums[i+1] = b, a


if __name__ == '__main__':
    my_nums = [5, 2]
    reorder(my_nums, 0)
    print(my_nums)
    