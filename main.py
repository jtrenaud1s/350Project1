

from search import bfs, dfs
from graph import createGraph
from maze import createMatrix, get_maze, getStartEnd


mat1 = createMatrix('input/maze_1.txt')
mat2 = createMatrix('input/maze_2.txt')
mat3 = createMatrix('input/maze_3.txt')

s1, e1 = getStartEnd(mat1)
s2, e2 = getStartEnd(mat2)
s3, e3 = getStartEnd(mat3)

graph1 = createGraph(mat1)
graph2 = createGraph(mat2)
graph3 = createGraph(mat3)


print("DFS MAZE 1")
result_dfs = dfs(graph1, 'A', 'U', get_maze, mat1, "output/dfs1.txt")


print("BFS MAZE 1")
result_bfs = bfs(graph1, 'A', 'U', get_maze, mat1, "output/bfs1.txt")


print("DFS MAZE 2")
result_dfs = dfs(graph2, 'E', 'P', get_maze, mat2, "output/dfs2.txt")


print("BFS MAZE 2")
result_bfs = bfs(graph2, 'E', 'P', get_maze, mat2, "output/bfs2.txt")


print("DFS MAZE 3")
result_dfs = dfs(graph3, 'K', 'X', get_maze, mat3, "output/dfs3.txt")


print("BFS MAZE 3")
result_bfs = bfs(graph3, 'K', 'X', get_maze, mat3, "output/bfs3.txt")

