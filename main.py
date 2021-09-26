

from search import bfs, dfs
from graph import createGraph
from maze import createMatrix, get_maze, getStartEnd
import pprint

def run_maze(filename):
    matrix = createMatrix('input/' + filename)
    graph = createGraph(matrix)

    for node, children in graph.items():
        print(node, ": ", repr(children))
    start, end = getStartEnd(matrix, graph)

    print("Start: " + str(start))
    print("DFS", filename)
    result_dfs = dfs(graph, start, end, get_maze, matrix, "output/dfs-" + filename)
    print("BFS", filename)
    result_bfs = bfs(graph, start, end, get_maze, matrix, "output/bfs-" + filename)

mazes = ["maze_1.txt", "maze_2.txt", "maze_3.txt"]

[run_maze(m) for m in mazes]



# mat1 = createMatrix('input/' + 'maze_2.txt')

# g1 = createGraph(mat1)

# for item in g1:
#     print(str(item) + ": " + str(g1[item]))