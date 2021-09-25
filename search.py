import copy

def dfs(graph, start_node, end_node, step):

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
  stack = [start_node, [start_node]]

  # While there are still nodes to look at
  while len(stack):
    [current, path] = stack.pop()

    # run the step function with the current path
    step(copy.deepcopy(path))
    if current not in seen:
      if current == end_node:
        return path
      
      seen.append(current)
      # Get all available connections and sort them alphabetically by node ID
      available = sorted(graph[start_node], key=lambda x: x[0])

      # Get a list of all available candidate nodes that haven't been seen yet
      candidates = [candidate[0] for candidate in available if candidate[0] not in seen]
      for candidate in candidates:
        stack.append([current, path + [candidate]])

 
def bfs(graph, start_node, end_node, step):

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

  # Push the first path into the queue
  paths_queue.append([start_node])

  # While there are paths to check
  while paths_queue:
    # Dequeue the next available path into a variable
    current_path = paths_queue.pop(0)
    # Get the last node in the current path
    current_node = current_path[-1]

    # Do some output with the path
    step(copy.deepcopy(current_path))

    # path found
    if current_node == end_node:
        return current_path
    
    # Create a new path for each of the candidate nodes and append those paths to the queue
    for candidate in graph[current_node]:
      new_path = current_path + [candidate]
      paths_queue.append(new_path)