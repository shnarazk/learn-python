#!/usr/bin/env python
import random

kuji: list[str] = ["lucky", "bad lack"]
print(random.choice(kuji))
## 身長(単位cm)
h: float = float(input("?cm ")) / 100
## 体重(単位kg)
w: float = float(input("?kg "))
bmi: float  = w / (h * h)
print("your BMI is", bmi, ".")
