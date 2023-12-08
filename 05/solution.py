import heapq


def parse_range(range_lines):
    ranges = []
    for line in range_lines:
        ranges.append([int(x) for x in line.split(' ')])
    return ranges

def prase_seeds(seed_line):
    return [int(x) for x in seed_line[7:].split(' ')]

def parse_seed_range(seeds):
    ranges = []
    for i in range(len(seeds)//2):
        ranges.append((seeds[i*2],seeds[i*2+1]))
    return ranges




    
def parse(file_input):
    with open(file_input) as f:
        lines = [line.strip() for line in f.readlines()]
        breaks = []
        breaks.append(lines.index(""))
        titles = "seeds seeds-to-soil soil-to-fertilizer fertilizer-to-water water-to-light light-to-temp temp-to-humidity humidity-to-location".split(' ')
        maps = {titles[0]:prase_seeds(lines[0])}
        for i in range(6):
            breaks.append(lines.index("",breaks[-1]+1))
            maps[titles[i+1]]=parse_range(lines[breaks[i]+2:breaks[i+1]])
        maps[titles[7]] = parse_range(lines[breaks[-1]+2:])
        return maps

def find_seed_location(seed):
    for mapping in list(maps.keys())[1:]:
        for map_range in maps[mapping]:
            if map_range[1] <= seed < map_range[1] + map_range[2]:
                offset = seed - map_range[1]
                seed = map_range[0] + offset
                break
    return seed


maps = parse('puzzle_input')
heap = []
ranges = parse_seed_range(maps['seeds'])
min_location = 10e10
for seed_start, seed_len in ranges:
    for seed in range(seed_start,seed_start + seed_len):
        min_location = min(min_location,find_seed_location(seed))
        print(min_location)
print(min_location)
