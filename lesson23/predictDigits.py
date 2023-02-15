#!/usr/bin/env python

import sklearn.databases
import sklearn.svm
import PIL.image
import numby

def imagetoData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.Resampling)
    numImage = numpy.asarray(grayImage, dtype = float)
    numImage = 16 - numpy.floor(17 * numImage / 256)
    numImage = numImage.flatten()
    return numImage

def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    print("result: ", n)

predictDigits(imagetoData("2.png"))
