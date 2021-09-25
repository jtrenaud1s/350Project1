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
    
def createGraph(mat):
    graph = {}
    for line in range(len(mat)):
        for char in range(len(mat[line])):
            if (str.isalpha(mat[line][char])):
                node  = mat[line][char]

                if node not in graph:
                    graph[node] = []


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
                                graph[node].append(     (mat[line + data[0] ][char + data[1] ], dir, (line +data[2], char + data[3]))      )
                            elif (dir == "U"):
                                if (mat[line-1][char] != '-'):
                                    graph[node].append(     (mat[line + data[0] ][char + data[1] ], dir, (line + data[2], char + data[3]))      )

                            elif (dir == "D"):
                                if (mat[line+1][char] != '-'):
                                    graph[node].append(     (mat[line + data[0] ][char + data[1] ], dir, (line + data[2], char + data[3]))      )        
                    except:
                        pass

    return graph

mat1 = createMatrix('maze_1.txt')
mat2 = createMatrix('maze_2.txt')
mat3 = createMatrix('maze_3.txt')

s1, e1 = getStartEnd(mat1)
s2, e2 = getStartEnd(mat2)
s3, e3 = getStartEnd(mat3)


graph1 = createGraph(mat1)
graph2 = createGraph(mat2)
graph3 = createGraph(mat3)
