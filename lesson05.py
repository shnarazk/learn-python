#!/usr/bin/env python3
import random

kuji: [str] = ["lucky", "bad lack"]
print(random.choice(kuji))

h = float(input("?cm ")) / 100
w = float(input("?kg "))
bmi = w / (h * h)
print("your BMI is ", bmi, ".")
