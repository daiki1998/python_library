"""
切り捨て
"""
x = int(x+0.000001)
x = int((x+t-1)/t+0.000001)
"""
切り上げ
"""
x = int(x-0.000001)+1