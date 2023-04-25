from os import write
import random
import sys, getopt

def read_map(mapName="MiniTown.dat"):
  f = open(mapName)
  text = f.read()
  f.close()
  lines = text.replace('"','').splitlines( )
  map = {'name':lines[0], 'edges':{}, 'nodes': {}, 'paving_plan':set(),'connected':True}

  for line in lines[1:]:
    words = line.split(',')
    map["edges"][(words[1],words[2])] = int(words[0])
    map['nodes'][words[1]] = set()
    map['nodes'][words[2]] = set()

    for a,b in map['edges'].keys():
      map['nodes'][a].add((map['edges'][(a,b)],b))
      map['nodes'][b].add((map['edges'][(a,b)],a))

  return map

def write_map(map,filename):
  f = open(filename, "w")
  #f = open(f"{map['name'].replace(' ','')}.dat", "w")
  text = f'"{map["name"]}"\n'
  for a,b in map['edges'].keys():
    text += (f'{map["edges"][(a,b)]},"{a}","{b}"\n')
  f.write(text)
  f.close()

def write_paving_map(map,filename):
  f = open(filename, "w")
  text = f'"{map["name"]}"\n'
  for a,b in map['Paving_Plan']:
    text += (f'"{a}","{b}"\n')
  f.write(text)
  f.close()

"""
# I forgot to do an evaluate function
def evaluate_pp(plan):
  open file
  read text
  skip name line
  read text line by line
  parse line in to 2 words without ""
  nodes A and B , so edges should have either (A,B) or (B,A)
  find edge in map.['edges'] and get the weight
  look for inverse of the 2 nodes as well
  sum up all the weights
  then call primAlg and compare the weights
"""

def main(argv):
   tdatafile = ''
   ppfile = ''
   try:
      opts, args = getopt.getopt(argv,"hr:w:secp")
   except getopt.GetoptError:
      print('muddytown.py -r <tdatafile> -w <tdatafile> -s <ppfile> -e <ppfile> \
      -c <ppfile> -p <ppfile>')
      sys.exit(2)

   map = {}
   for opt, arg in opts:
      if opt == '-h':
        print('muddytown.py -r <tdatafile> -w <tdatafile> -s <ppfile> -e <ppfile> \
              -c <ppfile> -p <ppfile>')  
        sys.exit()    
      elif opt in '-r':
        print("read")
        map = read_map(arg)
        primAlg(map)
      elif opt in '-w':
        write_map(map,arg)
      elif opt in'-s':
        #ToDo -e -c -p

if __name__ == "__main__":
  main(sys.argv[1:])