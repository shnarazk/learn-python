#!/usr/bin/env python3.11
from sklearn import datasets

digits = sklearn.datasets.load_digits()

print(len(digits.images))
 
