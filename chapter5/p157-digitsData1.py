#!/usr/bin/env python
import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("データの個数", len(digits.images))
 
