# 引数priceの消費税を表すキーワード引数tax(省略時は10とする）込み金額を計算して返す関数
def postTaxPrice2(price, tax = 10):
    return math.ceil(price * (1 + tax / 100))
