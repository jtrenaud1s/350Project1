class Node:
  def __init__(self, letter, location,):
    self.letter = letter
    self.location = location

  def __str__(self):
    return (str(self.letter) +": " +  str(self.location[0]) + "," + str(self.location[1]))

  __repr__ = __str__

  def __eq__(self, other):
    return self.location == other.location

  def __hash__(self):
    return hash("foo" + str(self))

def findNode(graph, Node):
  for item in graph.keys():
    if item == Node:
      return item
  return None

def findNodeByLocation(graph, location):
  for item in graph.keys():
    if item.location == location:
      return item
  return None

def createGraph(mat):
  graph = {}
  for line in range(len(mat)):
    for char in range(len(mat[line])):
      if (str.isalpha(mat[line][char])):
        letter = mat[line][char]
        node = Node(letter, (line, char))
        search = findNodeByLocation(graph, (line, char))  

        if not search:
          graph[node] = []
        else:
          node = search

        directions = {
          "L": (0, -2, 0, -1),
          "R": (0, 2, 0, 1),
          "U": (-2, 0, -1, 0),
          "D": (2, 0, 1, 0),
          # y change, x change, y for dash, x for dash
        }

        for item in directions:
          dir = item
          data = directions[item]

          try:
            if ( str.isalpha(mat[line + data[0]][char + data[1]] ) ):
              if (dir == "L" or dir == "R"):
                node_location = (line + data[0], char + data[1])
                connection_location = (line + data[2], char + data[3])
                letter = mat[node_location[0]][node_location[1]]

                temp = Node(letter, node_location)

                # if child not already in graph keys
                found = findNodeByLocation(graph, node_location)
                if found:
                  graph[node].append( (found, connection_location, '-'))
                else:
                  graph[node].append( (temp, connection_location, '-'))
                  graph[temp] = []
              elif (dir == "U"):
                if (mat[line-1][char] != '-'):
                  node_location = (line + data[0], char + data[1])
                  connection_location = (line + data[2], char + data[3])
                  letter = mat[node_location[0]][node_location[1]]
                  temp = Node(letter, (line+data[0], char+data[1]))
                  found = findNodeByLocation(graph, node_location)
                  if found:
                    graph[node].append( (found, connection_location, '|'))
                  else:
                    graph[node].append( (temp, connection_location, '|'))
                    graph[temp] = []
              elif (dir == "D"):
                if (mat[line+1][char] != '-'):
                  node_location = (line + data[0], char + data[1])
                  connection_location = (line + data[2], char + data[3])
                  letter = mat[node_location[0]][node_location[1]]
                  temp = Node(letter, node_location)
                  found = findNodeByLocation(graph, node_location)
                  if found:
                    graph[node].append( (found, connection_location, '|'))
                  else:
                    graph[node].append( (temp, connection_location, '|'))
                    graph[temp] = []
          except:
            pass


  return graph

def get_connection(graph, first, second):
  candidate = [g for g in graph[first] if g[0] is second]

  if candidate:
    return candidate[0]

  return None