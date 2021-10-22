#!/usr/bin/env python3
import random
import math

# PER MODALITA' LAZY, GENERIAMO UN TRIANGOLO CASUALE DI n RIGHE

def random_triangle(n:int, minVal:int, maxVal:int, s:int):
    random.seed(s,version=2)
    triangle = []
    values = [i for i in range(0,100)]
    for i in range(0,n):
        triangle.append(random.sample(values,i+1))
    return triangle

# STAMPIAMO IL TRIANGOLO SUL TERMINALE

def print_triangle(triangle):
    triangle_array = []
    for l in triangle:
        triangle_array += l
    n = len(triangle)
    for i in range(len(triangle_array)):
        if len(str(triangle_array[i])) == 1:
            triangle_array[i] = str(triangle_array[i]) + " "
    z = 0
    m = (2 * n) - 2
    for i in range(0, n):
        for j in range(0, m):
            print(end="  ")
        m = m - 1
        for j in range(0, i + 1):
            print(str(triangle_array[z]), end='  ')
            z += 1
        print("  ")
        
def calculate_path(triangle,path_values):
    triangle_array = []
    for l in triangle:
        triangle_array += l
    n = len(triangle)
    path = [triangle_array[0]]
    s = triangle_array[0]
    i = 0
    last_pos = 0
    for move in path_values:
        if(move == "L"):
            path.append(triangle_array[i+1 + last_pos])
            s += triangle_array[i+1 + last_pos]
            last_pos += i + 1 
        else:
            path.append(triangle_array[i+2 + last_pos])
            s += triangle_array[i+2 + last_pos]
            last_pos += i + 2 
        i += 1
    return path,s

def best_path_cost(triangle):
    dist = len(triangle)
    triangle_array = []
    for l in triangle:
        triangle_array += l
    triangle_array = triangle_array[::-1]
    i  = 0
    count = 1
    while dist > 1:
        triangle_array[i + dist] = max(triangle_array[i] + triangle_array[i + dist], triangle_array[i + 1] + triangle_array[i + dist])
        count += 1
        i += 1
        if count == dist:
            count = 1
            dist -= 1
            i += 1
    return triangle_array[i]
    

