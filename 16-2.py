from itertools import product

rules, my_ticket, tickets = open('16.txt').read().split('\n\n')

rules = {x.split(': ')[0]: {tuple(map(int, y.split('-'))) for y in x.split(': ')[1].split(' or ')} for x in rules.split('\n')}

def check_rules(v):
    for rule in rules.values():
        if any(rang[0] <= v <= rang[1] for rang in rule):
            return True
    return False

my_ticket = [*map(int, my_ticket.split('\n')[1].split(','))]
tickets = [[*map(int, x.split(','))] for x in tickets.split('\n')[1:]]

valid_tickets = []

for ticket in tickets:
    if all(check_rules(v) for v in ticket):
        valid_tickets.append(ticket)
            
from collections import defaultdict

rules_pos = defaultdict(set)

for i in range(len(valid_tickets[0])):
    for rule_name, rule in rules.items():
        if all(any(rang[0] <= ticket[i] <= rang[1] for rang in rule) for ticket in valid_tickets):
            rules_pos[i].add(rule_name)
            continue

locked_in_rules_pos = {}

while len(locked_in_rules_pos) < len(rules_pos):
    found = None

    for i, rule_names in rules_pos.items():
        if len(rule_names) == 1:
            found = rule_names.pop()
            locked_in_rules_pos[i] = found
            break

    for i, rule_names in rules_pos.items():
        rule_names -= {found}

total = 1

for v in [my_ticket[i] for i, rule_name in locked_in_rules_pos.items() if rule_name.startswith('departure')]:
    total *= v

print(total)
