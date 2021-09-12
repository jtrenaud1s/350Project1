# 350Project1

ideas:

make a matrix out of the maze (all of it, walls, spaces, letters, corners, doorways)
```
maze = [[' ', '*', '-', '-', '-', '-', '-', '-', '-', '*', ' '],
        ['>', '|', 'A', ' ', 'B', ' ', 'C', ' ', 'D', '|', ' '],
        [' ', '|', '-', '-', '-', '-', ' ', '-', '-', '|', ' '],
        [' ', '|', 'E', ' ', 'F', ' ', 'G', ' ', 'H', '|', ' '],
        [' ', '|', '-', '-', ' ', '-', '-', '-', '-', '|', ' '],
        [' ', '|', 'I', ' ', 'J', ' ', 'K', ' ', 'L', '|', ' '],
        [' ', '|', '-', '-', '-', '-', ' ', '-', '-', '|', ' '],
        [' ', '|', 'M', ' ', 'N', ' ', 'O', ' ', 'P', '|', '>'],
        [' ', '*', '-', '-', '-', '-', '-', '-', '-', '*', ' ']]
```
this matrix will be what is printed for output between each step as it is modified with the path taken

differentiate the two `>` arrows by knowing for a fact that the entrypoint is `in the first column` and the exit `is in the last column` of the matrix

traverse the matrix `until we find the coords of the starting point`, then skip `2` items to the right to find the actual starting node for the graph.

Now, we traverse the "maze" looking for rooms and connections, starting at the coords for the first room, in our case: `maze[1][2]`


check each direction. 
  if it is a wall, ignore
  if it is a space, check the next character in that direction, and create the connection both directions in the adjacency matrix for the graph

go to next node (just move to the right until you find a letter OR you hit a wall, where you just go to the next row and loop again

repeat the process until there is nothing left to traverse in the maze matrix

Now we do DFS and BFS search with the newly built graph to do these things:

- Find a path from the start to the exit
- edit the maze matrix as the search runs to reflect our current path (add lines between connected nodes on our current path)
- maybe store these matrix outputs into a list of their own to represent the state of the maze after each step so we can save it to the file
- make confetti when we win
