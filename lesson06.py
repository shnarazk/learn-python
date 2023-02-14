#!/usr/bin/env python3
from turtle import *

shape("turtle")
col = ["orange", "limegreen", "gold", "plum", "tomato"]
# forward(100)
pensize(5)
for i in range(5):
    color(col[i])
    circle(100)
    forward(197)
    left(72)
done() 

