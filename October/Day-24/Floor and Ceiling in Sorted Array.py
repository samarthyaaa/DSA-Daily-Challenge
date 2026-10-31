def floorCeil(nums, target):
    floor = -1
    ceil = -1
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return [target, target]

        elif nums[mid] < target:
            floor = nums[mid]
            l = mid + 1

        else:
            ceil = nums[mid]
            r = mid - 1

    return [floor, ceil]
