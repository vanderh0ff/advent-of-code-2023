import re

def is_engine_number(left_bound, right_bound, upper_bound, lower_bound, engine_map):
    for i in range(upper_bound,lower_bound+1):
        for c in engine_map[i][left_bound:right_bound]:
            if c not in '.0123456789':
                return True
    return False

def possible_gear(left_bound, right_bound, upper_bound, lower_bound, engine_map):
    for i in range(upper_bound,lower_bound+1):
        if '*' in engine_map[i][left_bound:right_bound]:
            return (engine_map[i][left_bound:right_bound].index('*')+left_bound, i)
    return None

def find_num_spans(line):
    number_finder = re.compile(r'(\d+)')
    start = 0
    spans = []
    m = number_finder.search(line,start)
    while m:
        spans.append(m.span())
        start = m.span()[1]
        m = number_finder.search(line,start)
    return spans

def get_bounds(span, index, max_w, max_h):
    return {
    "left" : max(0,span[0]-1),
    "right" : min(span[1]+1,max_w),
    "upper" : max(0,index-1),
    "lower" : min(index+1, max_h),
    }


def solve(input_file):
    with open(input_file) as f:
        engine_map = [line.strip() for line in f.readlines()]
        total = 0
        for index, line in enumerate(engine_map):
            for span in find_num_spans(line):
                bounds = get_bounds(span, index, len(line), len(engine_map)-1)
                if is_engine_number(bounds['left'],bounds['right'], bounds['upper'],bounds['lower'], engine_map):
                    print(f' found {engine_map[index][span[0]:span[1]]} at {index, span}')
                    for i in range(bounds['upper'],bounds['lower']+1):
                        print(engine_map[i][bounds['left']:bounds['right']])
                    total += int(engine_map[index][span[0]:span[1]])
        return total

def find_possible_gears(engine_map):
        possible = []
        for index, line in enumerate(engine_map):
            for span in find_num_spans(line):
                bounds = get_bounds(span, index, len(line), len(engine_map)-1)
                gear_pos = possible_gear(bounds['left'],bounds['right'], bounds['upper'],bounds['lower'], engine_map)
                if gear_pos:
                    possible.append((gear_pos,int(engine_map[index][span[0]:span[1]])))
        possible.sort()
        return possible

def solve_2(input_file):
    with open(input_file) as f:
        engine_map = [line.strip() for line in f.readlines()]
        total = 0
        possible = find_possible_gears(engine_map)
        current = possible[0]
        possible = possible[1:]
        while possible:
            for gear in possible:
                if current[0] == gear[0]:
                    total += current[1] * gear[1]
                    possible.remove(gear)
                    break
                if current[0][0] != gear[0][0]:
                    break
            if possible:
                current = possible[0]
                possible = possible[1:]
        return total

print(solve_2('puzzle_input'))
