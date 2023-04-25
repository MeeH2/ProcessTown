from os import write
import random
import networkx as nx

def read_map(mapName="MiniTown.dat"):
  f = open(mapName)
  text = f.read()
  f.close()
  #print(text)
  lines = text.replace('"','').splitlines( )
  map = {'name':lines[0], 'edges':{}, 'nodes': {}, 'paving_plan':set(),'connected':True}

  for line in lines[1:]:
    words = line.split(',')
    map["edges"][(words[1],words[2])] = int(words[0])
    #map['nodes'].update(words[1:])
    map['nodes'][words[1]] = set()
    map['nodes'][words[2]] = set()

    for a,b in map['edges'].keys():
      map['nodes'][a].add((map['edges'][(a,b)],b))
      map['nodes'][b].add((map['edges'][(a,b)],a))

  return map

def write_map(map):
  f = open(f"{map['name'].replace(' ','')}.dat", "w")
  text = f'"{map["name"]}"\n'
  for a,b in map['edges'].keys():
    text += (f'{map["edges"][(a,b)]},"{a}","{b}"\n')
  f.write(text)
  f.close()

def write_paving_map(map):
  f = open(f"{map['name'].replace(' ','')}PavingPlan.dat", "w")
  text = f'"{map["name"]}"\n'
  for a,b in map['edges'].keys():
    text += (f'"{a}","{b}"\n')
  f.write(text)
  f.close()

print("read map")
map = read_map()
print("write map")
write_map(map)
print("write paving map")
write_paving_map(map)


G = nx.Graph()

G.add_weighted_edges_from([(a,b,map["edges"][(a,b)]) for a,b in map["edges"].keys()])

print(G)

class Random_lcg:

  def __init__(self,seed = 25173):
    self.seed_num = seed
    self.multiplier = 13849
    self.increment = 11
    self.modulus = 32768
    self.num_base = self.seed_num

  def lcg(self,unit=1):
    numbers = []
    for i in range(unit):
        self.num_base = (self.multiplier * self.num_base + self.increment) % self.modulus
        numbers.append(self.num_base)
    return numbers if unit > 1 else numbers[0]

'''import re
f = open("StreetNamesDirty.txt")
text = f.read()
f.close()
cleanerList = [name for name in text.splitlines( ) if not (re.search("[0-9]", name) or '-' in name)]
f = open("StreetNamesCleaner.txt","w")
f.write('\n'.join(cleanerList))
f.close()'''

'''import re
import numpy as np
f = open("StreetNamesCleaner.txt")
text = f.read()
f.close()
cleanerList = text.replace("W ",'').replace("S ",'').replace("N ",'').replace("E ",'')
cleanerList = cleanerList.replace(' Ct','').replace(' St','').replace(' Cir','')\
.replace(' Pl','').replace(' Way','').replace(' Rd','').replace(' Blvd','')\
.replace(' Dr','').replace(' Ln','').replace(' Pkwy','').replace(' Ave','')\
.replace(' N','').replace(' S','').replace(" Boulevard",'').replace(' E','')\
.replace(' W','').replace(' Pvt',"").replace(' A\n','').replace(' B\n','')
cleanerList = np.unique(cleanerList.splitlines())
f = open("StreetNamesClean.txt","w")
f.write('\n'.join(cleanerList))
f.close()'''

def create_town(buildings,streets):
  #assert streets > buildings-1, f"too few streets for the number of buildings"
  assert streets <= buildings*(buildings-1)/2, f"too many streets for the number of buildings"

  map = {'edges':{}, 'nodes': {}, 'paving_plan':set(),'connected':True}


  rng = Random_lcg()

  f = open("StreetNamesClean.txt")
  all_street_names = f.read().splitlines()
  f.close()

  unique_streets = min(max(1,int(min(buildings/5,streets))),len(all_street_names))
  street_names = random.sample(all_street_names,unique_streets)
  
  # TO-DO maybe make unique check
  while len(map['nodes']) < buildings:
    building_number = str(rng.lcg())#str(int(random.random()*10000)+1)
    street_name = random.choice(street_names)
    building_name = f'{building_number} {street_name}'
    map['nodes'][building_name] = set()

  not_connected = list(map['nodes'])

  while len(map['edges']) < streets:
    if len(not_connected) >= 2:
      two_buildings = [not_connected.pop(),not_connected.pop()]
    elif len(not_connected) == 1:
      two_buildings = [not_connected.pop(),random.choice(list(map['nodes']))]
    else:
      two_buildings = random.sample(list(map['nodes']),2)
    new_edge = (two_buildings[0],two_buildings[1])
    opposite_edge = (two_buildings[1],two_buildings[0])
    if not (new_edge in map['edges'].keys() or opposite_edge in map['edges'].keys() ):
      map['edges'][new_edge] = int(random.random()*50)+1

    for a,b in map['edges'].keys():
      map['nodes'][a].add((map['edges'][(a,b)],b))
      map['nodes'][b].add((map['edges'][(a,b)],a))

  return map

map = create_town(34,50)
map['name'] = "Test"
print(map)
write_map(map)

def primAlg(map,start_node=None):

  all_nodes = list(map['nodes'].keys())
  print(len(all_nodes))
  frontier = [(0,all_nodes[0],None)]
  connected = set()
  connected.add(all_nodes[0])

  paving_cost = 0

  while len(connected) < len(all_nodes):
    if not frontier:
      map["connected"] = False
      extra_nodes = [i for i in all_nodes if i not in map["paving_plan"]]
      frontier = [(0,extra_nodes[0],None)]

    frontier = sorted(frontier)
    path = frontier.pop(0)
    connected.add(path[1])
    if path[2]:
      map["paving_plan"].add((path[2],path[1]))
      paving_cost += path[0]
    neightbours = list(map['nodes'][path[1]])
    new_nodes = [(weight,node,path[1]) for weight,node in neightbours if node not in connected]
    frontier += new_nodes

  map["paving_plan_cost"] = paving_cost

map = create_town(34,50)
print("map",map)
primAlg(map)
print("paving",map["paving_plan"])
print("paving_plan_cost",map["paving_plan_cost"])

G = nx.Graph()

G.add_weighted_edges_from([(a,b,map["edges"][(a,b)]) for a,b in map["edges"].keys()])
G.add_nodes_from(map["nodes"])

nx.draw(G)
print(nx.is_connected(G))
