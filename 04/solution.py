import re

card_adj_list = {}
cards_total_copies = {}

def string_to_list(num_string):
    return [int(x) for x in re.findall(r'(\d+)',num_string)]

def parse_file(input_file):
    games = []
    with open(input_file) as f:
        for line in [x.strip() for x in f.readlines()]:
            card_id , card_nums = line.split(':')
            card_id = card_id[4:]
            winners, scratched = [string_to_list(x) for x in card_nums.split('|')]
            games.append((int(card_id),winners,scratched))
    return games

def get_game_score(game):
    _, winners, scratched = game
    score = 0.5
    for i in winners:
        if i in scratched:
            score *= 2
    if score == 0.5:
        return 0
    return score

def get_card_copies(game):
    id, winners, scratched = game
    copies = 0
    for i in winners:
        if i in scratched:
            copies += 1
    return [i for i in range(id+1,id+copies+1)]

def get_total_points(games):
    total = 0
    for game in games:
        total += get_game_score(game)
    return total

def get_total_card_copies(card_id):
    if card_id in cards_total_copies:
        return cards_total_copies[card_id]
    else:
        total = 1
        for card in card_adj_list[card_id]:
            total += get_total_card_copies(card)
        cards_total_copies[card_id] = total
        return total

def get_total_cards(games):
    for i in range(len(games)):
        card_adj_list[games[i][0]] = (get_card_copies(games[i]))
    print(card_adj_list)
    total_cards = 0
    for i in range(len(games)) :
        total_cards += get_total_card_copies(games[i][0])
    return total_cards

games = parse_file('puzzle_input')
# print(get_total_points(games))
print(get_total_cards(games))

