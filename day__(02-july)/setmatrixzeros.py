class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        visited = [row[:] for row in matrix] 
        for i in range (n):
            for j in range (m):
                if(matrix[i][j]==0):
                    for k in range(m):
                        visited[i][k]=0




        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==0):
                    for k in range(n):
                        visited[k][j]=0




        for i in range (n):
            for j in range(m):
                matrix[i][j]=visited[i][j]
    

# t.c=O(n*m)
# s.c=O(n*m)