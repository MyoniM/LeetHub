class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        gender = []
        for i in range(len(matrix[0])):
            trans = []
            for j in matrix:
                trans.append(j[i])
            gender.append(trans)
        return gender