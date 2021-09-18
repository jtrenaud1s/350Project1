def createMatrix(file):
    file = open(file, 'r')
    lines = file.readlines()

    mat = []

    for line in lines:
        mat.append([c for c in line.split()])

    return mat
    

mat1 = createMatrix('maze_1.txt')


