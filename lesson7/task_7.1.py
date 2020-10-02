class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self, matrx=None):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrx]))

    def __add__(self):
        matrx = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrx[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrx]))


my_matrix = Matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[7, 8, 9],
                    [4, 5, 6],
                    [1, 2, 3]])

print(my_matrix.__add__())
