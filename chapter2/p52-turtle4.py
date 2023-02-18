#!/usr/bin/env python
from turtle import *
import math

shape("turtle")
col: list[str] = ["orange", "limegreen", "gold", "plum", "tomato"]
pensize(5)
n: int = 6
r: int = 192
for i in range(n):
    color(col[i % 5])
    circle(r/2)
    forward(r)
    left(360 / n)
done() 
 