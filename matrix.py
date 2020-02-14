"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ""
    for row in matrix:
        for col in row:
            s+= str(col) + " "
        s+= "\n"
    print(s)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    prod = []
    temp = 0
    for h in range(len(m1)):
        for i in range(4):
            for w in range(len(m1[0])):
            temp += m1[h][w]*m2[i][w]
            prod.append(temp)
            temp = 0
    return prod

g = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print_matrix(g)
