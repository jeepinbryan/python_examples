import os
import pydot
from IPython.display import Image, display

rootDir = "/Users/v120564/Documents/SRC/d3_force_graph_examples"

G = pydot.Dot(graph_type="digraph")

node = pydot.Node(rootDir.split('/')[-1], style="filled", fillcolor="green")
G.add_node(node)


for root, dirs, files in os.walk(rootDir):

    for subdir in dirs:
        node = pydot.Node(subdir, style="filled", fillcolor="yellow")
        G.add_node(node)
        edge = pydot.Edge(root.split('/')[-1], subdir)
        G.add_edge(edge)
        #print ("subdir = " + subdir)
        #print (G)

    for file in files:
        node = pydot.Node(file, style="filled", fillcolor="orange")
        G.add_node(node)
        edge = pydot.Edge(root.split('/')[-1], file)
        G.add_edge(edge)

print(G)

#im = Image(G.create_png())

#display(im)
