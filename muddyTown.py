import random
import networkx as nx
import matplotlib.pyplot as plt

def read_map(mapName="MiniTown.dat"):
    with open(mapName) as f:
        lines = f.read().replace('"', '').splitlines()
    
    map = {'name': lines[0], 'edges': {}, 'nodes': {}, 'paving_plan': set(), 'connected': True}

    for line in lines[1:]:
        words = line.split(',')
        map["edges"][(words[1], words[2])] = int(words[0])
        map['nodes'].setdefault(words[1], set())
        map['nodes'].setdefault(words[2], set())

    for a, b in map['edges']:
        map['nodes'][a].add((map['edges'][(a, b)], b))
        map['nodes'][b].add((map['edges'][(a, b)], a))

    return map

def write_map(map, filename):
    with open(filename, "w") as f:
        text = ['"{}"\n'.format(map["name"])]
        text.extend('{},"{}","{}"\n'.format(map["edges"][(a, b)], a, b) for a, b in map['edges'])
        f.write(''.join(text))

def write_paving_map(map, filename):
    with open(filename, "w") as f:
        text = ['"{}"\n'.format(map["name"])]
        text.extend('"{}","{}"\n'.format(a, b) for a, b in map['edges'])
        f.write(''.join(text))

def create_town(buildings, streets):
    map = {'edges': {}, 'nodes': {}, 'paving_plan': set(), 'connected': True}

    with open("StreetNamesCleaner.txt") as f:
        all_street_names = f.read().splitlines()

    street_names = random.sample(all_street_names, min(max(1, int(min(buildings / 5, streets))), len(all_street_names)))

    while len(map['nodes']) < buildings:
        building_name = '{} {}'.format(str(int(random.random() * 10000) + 1), random.choice(street_names))
        map['nodes'].setdefault(building_name, set())

    while len(map['edges']) < streets:
        two_buildings = random.sample(list(map['nodes']), 2)
        new_edge = (two_buildings[0], two_buildings[1])
        opposite_edge = (two_buildings[1], two_buildings[0])

        if new_edge not in map['edges'] and opposite_edge not in map['edges']:
            map['edges'][new_edge] = int(random.random() * 50) + 1

        for a, b in map['edges']:
            map['nodes'][a].add((map['edges'][(a, b)], b))
            map['
