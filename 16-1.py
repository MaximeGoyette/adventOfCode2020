from itertools import product

rules, my_ticket, tickets = open('16.txt').read().split('\n\n')

rules = {x.split(': ')[0]: {tuple(map(int, y.split('-'))) for y in x.split(': ')[1].split(' or ')} for x in rules.split('\n')}

def check_rules(v):
    for rule in rules.values():
        if any(rang[0] <= v <= rang[1] for rang in rule):
            return True
    return False

my_ticket = {*map(int, my_ticket.split('\n')[1].split(','))}
tickets = [{*map(int, x.split(','))} for x in tickets.split('\n')[1:]]

error = 0

for ticket in tickets:
    for v in ticket:
        if not check_rules(v):
            error += v

print(error)
