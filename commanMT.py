def main(argv):
    map = {}
    try:
        opts, args = getopt.getopt(argv,"hr:w:wp:t:pv")
    except getopt.GetoptError:
        print('muddytown.py -r <mapfile> -w <mapfile> -wp <pavingplanfile> -t <buildings> <streets> -p -v')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('muddytown.py -r <mapfile> -w <mapfile> -wp <pavingplanfile> -t <buildings> <streets> -p -v')
            sys.exit()
        elif opt == '-r':
            map = read_map(arg)
        elif opt == '-w':
            write_map(map, arg)
        elif opt == '-wp':
            write_paving_map(map, arg)
        elif opt == '-t':
            num_buildings, num_streets = map(int, arg.split())
            map = create_town(num_buildings, num_streets)
            map['name'] = "Arbitrary Town"
        elif opt == '-p':
            primAlg(map)
            print("paving", map["paving_plan"])
            print("paving_plan_cost", map["paving_plan_cost"])
        elif opt == '-v':
            G = nx.Graph()
            G.add_weighted_edges_from([(a,b,map["edges"][(a,b)]) for a,b in map["edges"].keys()])
            G.add_nodes_from(map["nodes"])
            nx.draw(G)
            plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
