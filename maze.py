import copy
from graph import get_connection

def createMatrix(file):
    file = open(file, 'r')
    lines = file.readlines()

    mat = []

    for line in lines:
        mat.append([c for c in line])
    
    return mat

def getStartEnd(mat):
    for line in range(len(mat)):
        for char in range(len(mat[line])):
            character = mat[line][char]
            
            if(character == '>'):
                if (char == 0):
                    start = mat[line][char+2]
                else:
                    end = mat[line][char-2]


    return start, end 


def get_maze_str(maze):
    lines = [''.join(line) for line in maze]
    return ''.join(lines)

def get_maze(path, graph, maze):
    maze = copy.deepcopy(maze)
    output = ' -> '.join(path) + "\n"
    while len(path) > 1:
        second = path.pop()
        first = path[-1]
        connection = get_connection(graph, first, second)

        (y, x) = connection[2]
        character = connection[3]

        maze[y][x] = character
    
    return output + get_maze_str(maze) + "\n\n"
    
def write(filename, out):
  with open(filename, "w") as fp:
    fp.write(out)
