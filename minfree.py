"""
最小可用ID：
找出最小可用ID
"""

def brute_force(lst):
    i = 0
    while True:
        if i not in lst:
            return i
        i =  i + 1