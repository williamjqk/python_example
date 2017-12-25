#!/usr/bin/env python
#
# reference links
# http://www.jianshu.com/p/a2497a33390f
# https://stackoverflow.com/questions/18804254/creating-neo4j-graph-database-from-csv-file-using-py2neo
# import csv
# from py2neo import Graph, Node
# # from py2neo import neo4j, cypher
# # from py2neo import node,  rel
# from py2neo import authenticate
# authenticate("localhost:7474", "neo4j", "train")
# # calls database service of Neo4j
# #
# test_graph = Graph("http://localhost:7474/db/data/", password="train")
#
# test_node_1 = Node(label = "Person",name = "test_node_1")
# test_node_2 = Node(label = "Person",name = "test_node_2")
# test_graph.create(test_node_1)
# test_graph.create(test_node_2)
#
# for person in test_graph.find("Person"):
#     print(person)

# http://py2neo.org/v3/database.html
from py2neo import Graph, Node, Relationship
g = Graph()
tx = g.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()
g.exists(ab)
for x in g.find("Person"):
    print(x)
