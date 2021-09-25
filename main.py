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

mat1 = createMatrix('maze_1.txt')
mat2 = createMatrix('maze_2.txt')
mat3 = createMatrix('maze_3.txt')

s1, e1 = getStartEnd(mat1)
s2, e2 = getStartEnd(mat2)
s3, e3 = getStartEnd(mat3)


