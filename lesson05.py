#!/usr/bin/env python3
import random

kuji: list[str] = ["lucky", "bad lack"]
print(random.choice(kuji))

h: float = float(input("?cm ")) / 100
w: float = float(input("?kg "))
bmi: float  = w / (h * h)
print("your BMI is", bmi, ".")
