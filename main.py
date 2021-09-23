def createMatrix(file):
    file = open(file, 'r')
    lines = file.readlines()

    mat = []

    for line in lines:
        mat.append([c for c in line])
    
    return mat
    

mat1 = createMatrix('maze_1.txt')
mat2 = createMatrix('maze_2.txt')
mat3 = createMatrix('maze_3.txt')



