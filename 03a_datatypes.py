#!/usr/bin/python3

def draw_horiz(n):
    print(" -" * n)

def draw_vert(n):
    print("| " * n)

gridsize = int(input("Enter the size of your grid: "))

for i in range(gridsize):
    draw_horiz(gridsize)
    draw_vert(gridsize + 1)
draw_horiz(gridsize)
