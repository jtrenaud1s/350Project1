from main import findNode


class Node:
  def __init__(self, letter, location,):
    self.letter = letter
    self.location = location

  def __str__(self):
    return (str(self.letter) +": " +  str(self.location[0]) + "," + str(self.location[1]))

def findNode(graph, Node):
    for item in graph.keys():
        if item == Node:
            return item 

def createGraph(mat):
  graph = {}
  for line in range(len(mat)):
    for char in range(len(mat[line])):
      if (str.isalpha(mat[line][char])):
        letter = mat[line][char]
        node  = Node(letter, (line, char))        

        if( not (findNode(graph, node))):
          graph[node] = []
        else:
          node = findNode(graph, node)

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
              if (dir != "U" and dir != "D"):
                letter = mat[line + data[0]][char + data[1]]
                temp = Node(letter, (line+data[0], char+data[1]))
                graph[node].append( (temp, (line+data[2], char +data[3]), '-'))
                graph[temp] = []
              elif (dir == "U"):
                if (mat[line-1][char] != '-'):
                  letter = mat[line + data[0]][char + data[1]]
                  temp = Node(letter, (line+data[0], char+data[1]))
                  graph[node].append((temp, (line+data[2], char +data[3]), '|'))
              elif (dir == "D"):
                if (mat[line+1][char] != '-'):
                  letter = mat[line + data[0]][char + data[1]]
                  temp = Node(letter, (line+data[0], char+data[1]))
                  graph[node].append(    (temp, (line+data[2], char +data[3]), '|')     )
          except:
            pass

  return graph

def get_connection(graph, first, second):

  candidate = [g for g in graph[first] if g[0] is second]

  if candidate:
    return candidate[0]

  return None