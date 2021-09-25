import copy
import pprint

def dfs(graph, start_node, end_node, step, args, filename):

  """ Run a DFS search on the maze and run the step function at the end of each iteration. Returns the successful path stack
  :type graph: dict()
  :param graph: The dictionary representation of a graph

  :type start_node: str()
  :param start_node: The ID of the node to start the search from

  :type end_node: str()
  :param end_node: The ID of the node to search for

  :type step: function(list())
  :param step: The function that runs at the end of each step, which passes in the current path stack

  :rtype: list()
  """
  # All the nodes we've already looked at
  seen = []
  # All the nodes that comprise the path we're currently on
  stack = [(start_node, [start_node])]

  output = ""

  # While there are still nodes to look at
  while len(stack):
    (current, path) = stack.pop()
    output += step(copy.deepcopy(path), graph, args)
    if current not in seen:
      if current == end_node:
        write(filename, output)
        return path
      
      seen.append(current)
      # Get all available connections and sort them alphabetically by node ID
      available = sorted(graph[current], key=lambda x: x[0])
      # Get a list of all available candidate nodes that haven't been seen yet
      candidates = [candidate[0] for candidate in available if candidate[0] not in seen]
      for candidate in candidates:
        stack.append((candidate, path + [candidate]))

 
def bfs(graph, start_node, end_node, step, args, filename):

  """ Run a DFS search on the maze and run the step function at the end of each iteration. Returns the successful path stack
  :type graph: dict()
  :param graph: The dictionary representation of a graph

  :type start_node: str()
  :param start_node: The ID of the node to start the search from

  :type end_node: str()
  :param end_node: The ID of the node to search for

  :type step: function(list())
  :param step: The function that runs at the end of each step, which passes in the current path stack

  :rtype: list()
  """
  # This queue holds multiple lists. each list is a path that can be taken
  paths_queue = []
  seen = []

  # Push the first path into the queue
  paths_queue.append([start_node])

  output = ""

  # While there are paths to check
  while paths_queue:
    # Dequeue the next available path into a variable
    current_path = paths_queue.pop(0)
    # Get the last node in the current path
    current_node = current_path[-1]
    seen.append(current_node)

    output += step(copy.deepcopy(current_path), graph, args)
    # path found
    if current_node == end_node:
      write(filename, output)
      return current_path
    
    available = sorted(graph[current_node], key=lambda x: x[0])

    # Get a list of all available candidate nodes
    candidates = [candidate[0] for candidate in available if candidate[0] not in seen]

    # Create a new path for each of the candidate nodes and append those paths to the queue
    for candidate in candidates:
      paths_queue.append(current_path + [candidate])

def write(filename, out):
  with open(filename, "w") as fp:
    fp.write(out)

def get_connection(graph, first, second):
  candidate = [g for g in graph[first] if g[0] == second]

  if candidate:
    return candidate[0]

  return None
