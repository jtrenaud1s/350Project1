import copy
from graph import get_connection

def createMatrix(file):
    file = open(file, 'r')
    lines = file.readlines()

    mat = []

    for line in lines:
        mat.append([c for c in line])
    
    return mat

def getStartEnd(mat, graph):
    for line in range(len(mat)):
        for char in range(len(mat[line])):
            character = mat[line][char]
            
            if(character == '>'):
                if (char == 0):
                    start = (line, char+2)
                else:
                    end = (line,char-2)

    for item in graph:
        if item.location == start:
            start = item
        elif item.location == end:
            end = item


    return start, end 


def get_maze_str(maze):
    lines = [''.join(line) for line in maze]
    return ''.join(lines)

def get_maze(path, graph, maze):
    maze = copy.deepcopy(maze)
    output = ' -> '.join([p.letter for p in path]) + "\n"
    while len(path) > 1:
        second = path.pop()
        first = path[-1]

        print("YO: ", [first])
        print("YO: 2nd", [second])

        connection = get_connection(graph, first, second)

        (y, x) = connection[1]
        character = connection[2]

        maze[y][x] = character
    
    return output + get_maze_str(maze) + "\n\n"
    
def write(filename, out):
  with open(filename, "w") as fp:
    fp.write(out)
