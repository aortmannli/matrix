"""from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


draw_lines( matrix, screen, color )
display(screen)
"""

from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 165, 225, 255 ]
matrix = new_matrix()


for a in range(500):
    add_edge(matrix,0,a,0,500,a,0)

head = new_matrix()
h_color = [ 80, 185, 30 ]

#adds edges of entire box and details inside
def draw_box(mat,x,y,t):
    add_edge(mat,x,y,0,x+t,y,0)
    add_edge(mat,x+t,y,0,x+t,y-t,0)
    add_edge(mat,x+t,y-t,0,x,y-t,0)
    add_edge(mat,x,y-t,0,x,y,0)
    for a in range(t):
        add_edge(mat,x,y-a,0,x+t,y-a,0)

#cheeks
add_edge(head,150,225,0,150,300,0)  
add_edge(head,350,225,0,350,300,0)
for a in range(75):
    add_edge(head,150,300-a,0,350,300-a,0)
    
#chin
#h
add_edge(head,150,225,0,160,225,0)
add_edge(head,350,225,0,340,225,0)
for a in range(10):
    add_edge(head,160,225-a,0,340,225-a,0)
    
add_edge(head,160,215,0,170,215,0)
add_edge(head,340,215,0,330,215,0)
for a in range(10):
    add_edge(head,170,215-a,0,330,215-a,0)
    
add_edge(head,170,205,0,330,205,0)

#v
add_edge(head,160,225,0,160,215,0)
add_edge(head,340,225,0,340,215,0)

add_edge(head,170,215,0,170,205,0)
add_edge(head,330,215,0,330,205,0)




#eyes
#h
add_edge(head,150,300,0,160,300,0)
add_edge(head,350,300,0,340,300,0)

add_edge(head,160,310,0,170,310,0)
add_edge(head,340,310,0,330,310,0)

add_edge(head,170,320,0,195,320,0)
add_edge(head,330,320,0,305,320,0)

add_edge(head,195,310,0,205,310,0)
add_edge(head,305,310,0,295,310,0)

for a in range(10):
   add_edge(head,160,300+a,0,205,300+a,0)
for a in range(10):
    add_edge(head,170,310+a,0,195,310+a,0)

for a in range(10):
   add_edge(head,295,300+a,0,340,300+a,0)
for a in range(10):
    add_edge(head,305,310+a,0,330,310+a,0)

#v
add_edge(head,160,300,0,160,310,0)
add_edge(head,340,300,0,340,310,0)

add_edge(head,170,310,0,170,320,0)
add_edge(head,330,310,0,330,320,0)

add_edge(head,195,320,0,195,310,0)
add_edge(head,305,320,0,305,310,0)

add_edge(head,205,310,0,205,300,0)
add_edge(head,295,310,0,295,300,0)

add_edge(head,205,300,0,295,300,0)

body = new_matrix()
b_color = h_color
#main
#legs

eye = new_matrix()
e_color = [255,255,255]

draw_box(eye,170,310,25)
draw_box(eye,305,310,25)

lines = new_matrix()
l_color = [0,0,0]

draw_box(lines,175,310,20)
draw_box(lines,310,310,20)

draw_box(lines,210,270,10)
draw_box(lines,285,270,10)

for a in range(10):
    add_edge(lines,220,260-a,0,285,260-a,0)

draw_lines(matrix,screen,color)
draw_lines( head, screen, h_color )
draw_lines( eye, screen, e_color )
draw_lines(lines,screen,l_color)
display(screen)
save_ppm_ascii(screen,'img.ppm')
