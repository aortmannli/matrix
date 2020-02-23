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
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
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
    iden = matrix
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if (r == c):
                iden[r][c] = 1
            else:
                iden[r][c] = 0
    return iden


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    prod = new_matrix(len(m1),len(m2[0]))
    if len(m1[0]) == len(m2):
        for a in range(len(m1)):
            for b in range(len(m2[0])):
                for c in range(len(m2)):
                    prod[a][b] += m1[a][c]*m2[c][b] 
    else:
        print("u are a buffoon")
    print_matrix(prod)
    return prod


g = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print_matrix(g)
print()
print()

f=ident(g)
print_matrix(f)
print()
print()



g = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix_mult(g,f)
print()
print()
j= [[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]]
matrix_mult(g,j)


a= [[1.00,4.00],[2.00,5.00],[3.00,6.00],[1.00,1.00]]
b= [[1.00,4.00,7.00,10.00],[2.00,5.00,8.00,11.00],[3.00,6.00,9.00,12.00],[1.00,1.00,1.00,1.00]]

matrix_mult(b,a)
