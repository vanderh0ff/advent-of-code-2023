with open('puzzel_input', 'r') as f:
    total = 0
    for line in f.readlines():
        nums = [x for x in line if x.isdigit()]
        val = int(nums[0]+nums[-1])
        total += val
    print(total)


