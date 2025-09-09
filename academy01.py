"""
pythonの基本

pythonとは高水準で、動的型付けを行うマルチパラダイムプログラミング言語
"""

# exe quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

"""
python Version 3.12.3

pythonのバージョン確認: python --version

python インクリメントやデクリメント演算子は対応していない。

python 基本データ型
int # 整数
float # 浮動小数点数
str # 文字列

bool # 真偽値 &&, || (記号)ではなく and, or （英単語）を使用
print t and f # False 論理AND
print t or f  # True　論理OR
print not t    # False　論理NOT
print t != f # True　論理XOR

list # リスト
tuple # タプル
set # セット
dict # 辞書 

このように型を確認できる
print(type(123)) # <class 'int'>
"""