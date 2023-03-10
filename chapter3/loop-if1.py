#!/usr/bin/env python

scores = [["あ", 68], ["い", 72], ["う", 85], ["え", 50], ["お", 100]]

for score in scores:
    if score[1] >= 60:
        print(score[0])
        print("OK")
    else:
        print("bad luck")

for score in scores:
    print(score[0], end = ": ")
    if score[1] >= 60:
        print("OK")
    else:
        print("bad luck")
