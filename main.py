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


                try:
                    if ( str.isalpha(mat[line][char-2])):
                        graph[node].append( (mat[line][char-2], 'L' ))

                except:
                    pass

                try:
                    if ( str.isalpha( mat[line][char+2])    ):
                        graph[node].append( (mat[line][char+2], 'R' ))
                except:
                    pass

                try:
                    if ( str.isalpha( mat[line-2][char])    ):
                        if (mat[line-1][char] != '-'):
                            graph[node].append( (mat[line-2][char], 'U' ))
                except:
                    pass


                try:
                    if ( str.isalpha( mat[line+2][char])    ):
                        if (mat[line+1][char] != '-'):
                            graph[node].append( (mat[line+2][char], 'D' ))
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
