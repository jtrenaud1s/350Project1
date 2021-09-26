

from search import bfs, dfs
from graph import createGraph
from maze import createMatrix, get_maze, getStartEnd

def run_maze(filename):
    matrix = createMatrix('input/' + filename)
    graph = createGraph(matrix)
    start, end = getStartEnd(matrix, graph)

    print("Start: " + str(start))
    print("DFS", filename)
    result_dfs = dfs(graph, start, end, get_maze, matrix, "output/dfs-" + filename)
    print("BFS", filename)
    result_bfs = bfs(graph, start, end, get_maze, matrix, "output/bfs-" + filename)

mazes = ["maze_1.txt", "maze_2.txt", "maze_3.txt"]

[run_maze(m) for m in mazes]