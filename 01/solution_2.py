import re

def is_num_re(input):
    matches = []
    start = 0
    query = re.compile(r"(zero|one|two|three|four|five|six|seven|eight|nine|[0123456789])")
    while query.search(input, start):
        result = query.search(input,start)
        matches.append(input[result.start(1):result.end(1)])
        start = result.start(1) + 1
        print(start)

    first = is_num(matches[0]) 
    last = is_num(matches[-1]) 
    if first and last:
        return int(is_num(first) + is_num(last))
    else:
        print("ran in to weird ness")
        return 0


def is_num(input):
    if input in '1234567890':
        return input
    spelled_numbers = [
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            ]
    for i,n in enumerate(spelled_numbers):
        if n in input:
            return repr(i)
    print("also got some weird in is num")
    return "0"
        
"puzzle_input_2"
with open("puzzle_input_2", 'r') as f:
    total = 0
    for line in f.readlines():
        val = is_num_re(line)
        print(val)
        total += val
    print(total)


