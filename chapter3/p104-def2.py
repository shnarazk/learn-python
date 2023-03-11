#!/usr/bin/env python
import math

def postTaxPrice(price):
    ans = price * 1.1
    return ans

print(postTaxPrice(100), "円")
print(postTaxPrice(129), "円")
print(postTaxPrice(980), "円")

################################
# 1. 小数点は不要なのでは

def postTaxPrice1(price):
    ans = price * 1.1
    return math.ceil(ans)

print(postTaxPrice1(100), "円")
print(postTaxPrice1(129), "円")
print(postTaxPrice1(980), "円")

################################
# 2. 消費税は将来変わるかも

def postTaxPrice2(price, tax = 10):
    ans = price * (1 + tax / 100)
    return math.ceil(ans)

print(postTaxPrice2(100), "円")
print(postTaxPrice2(109, 15), "円")
print(postTaxPrice2(100, 3), "円")

print(postTaxPrice2(160), "円")
print(postTaxPrice2(169, 15), "円")
print(postTaxPrice2(160, 3), "円")

################################
# 3. この関数は2行にまとめられるのでは

def postTaxPrice2(price, tax = 10):
    return math.ceil(price * (1 + tax / 100))
