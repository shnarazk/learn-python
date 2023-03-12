#!/usr/bin/env python

import random

def omikuji():
    kuji = ['大吉', '中吉', '小吉', '凶']
    return random.choice(kuji)

kekka = omikuji()
print("結果は", kekka, "です")


# 等価変換
print("結果は", omikuji(), "です")


# 等価変換
print("結果は", random.choice(['大吉', '中吉', '小吉', '凶']), "です")


# f文字列 {}で埋め込み
print("結果は", kekka, "です")
print(f"結果は{kekka}です")
print(f"結果は{random.choice(['大吉', '中吉', '小吉', '凶'])}です")
