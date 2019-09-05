# python3
import networkx as nx

#G = nx.graph()
#D = nx.DiGraph()

debug=0

D=nx.read_weighted_edgelist('nodes.txt',create_using=nx.DiGraph())

if (debug==1):
	print(len(D.nodes()),len(D.edges()))
	print ("Nodes\n")
	print(D.nodes())
	print ("Edges\n")
	print(D.edges())

nx.write_gexf(D, "test.gexf")
