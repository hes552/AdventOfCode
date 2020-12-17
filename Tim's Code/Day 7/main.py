class Node:
  def __init__(self, id):
    self.id = id
    self.adjacent = {}

  def __str__(self):
    return f'{self.id}: {self.adjecent}'

  def addAdjacent(self, other, weight):
    self.adjacent[other] = weight

  def getParents(self):
    parents = {}
    for i in self.adjacent.keys():
      if self.adjacent[i] < 0:
        parents[i] = self.adjacent[i]
    return parents

  def getChildren(self):
    children = {}
    for i in self.adjacent.keys():
      if self.adjacent[i] > 0:
        children[i] = self.adjacent[i]
    return children

  def getEdge(self, other):
    return self.adjacent[other]

class Graph:
  def __init__(self):
    self.nodes = {}

  def addNode(self, id):
  if id not in self.nodes.keys():
    self.nodes[id] = Node(id)

  def getNode(self, id):
    return self.node[id] if id in self.nodes.keys() else None

  def addEdge(self, parent, child, weight):
    weight = abs(weight)
    if parent not in self.nodes.keys():
      self.addNode(parent)
    if child not in self.nodes.keys():
      self.addNode(child)

    self.nodes[parent].addAdjacent(child, weight)
    self.nodes[child].addAdjacent(parent, -weight)