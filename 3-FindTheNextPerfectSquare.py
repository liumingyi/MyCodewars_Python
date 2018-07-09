"""
题目：Find the next perfect square <kyu7>

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square
after the one passed as a parameter.Recall that an integral perfect square is
an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square, than -1 should be returned.
You may assume the parameter is positive.

你或许见过一些很大的完全平方数，但是他们下一个是多少呢？
完成这个 findNextSquare 函数，找到传入参数的下个一个完全平方数。想象一下一个完全平方数是个整数n，
那么sqrt(n)也是一个整数。
如果参数不是一个完全平方数，则返回-1。你可以假的参数都是正数。

Examples:
findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect

"""


# from math import sqrt


# def findNextSquare(sq):
#     if not sqrt(sq).is_integer():
#         return -1
#     sq += 1
#     while not sqrt(sq).is_integer():
#         sq += 1
#     return sq

# 其实并不需要sqrt,看看下面的函数
def findNextSquare(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1


# Test
# --> returns 144
print(findNextSquare(121))
# --> returns 676
print(findNextSquare(625))
# --> returns -1 since 114 is not a perfect
print(findNextSquare(114))

# 检查是否是整数 内置函数：isinstance()
# print(isinstance(5.2, int))
# print(isinstance(5.0, int))
# print(isinstance(5, int))


# 这样很快捷，但是面对大数的时候会有精度问题
# print(sqrt(16).is_integer())

# print(sqrt(16))
# print(len(str(sqrt(16))))

# print(int(5.2))

# print(isinstance(5.0, int))

# 关于sqrt计算的精度问题：
# def is_square(apositiveint):
#     x = apositiveint // 2
#     seen = {x}
#     while x * x != apositiveint:
#         x = (x + (apositiveint // x)) // 2
#         if x in seen:
#             return False
#         seen.add(x)
#     return True
#
#
# for i in range(110, 130):
#     print(i, is_square(i))

# 另外还有一个库:gmpy
