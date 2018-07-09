"""
题目 two to one  <kyu7>

两个string，s1，s2 只包含字母 a-z。返回一个新的有序string。
包含了s1,s2中不同的字母。
例如：
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

"""


# def longest(s1, s2):
#     result = set()
#     for letter in s1:
#         result.add(letter)
#     for letter in s2:
#         result.add(letter)
#     result = list(result)
#     result.sort()
#     return ''.join(result)

# def longest(s1, s2):
#     total = [*(s1 + s2)]
#     result = set(total)
#     result = list(result)
#     result.sort()
#     return ''.join(result)

def longest(s1, s2):
    return "".join(sorted(set(s1 + s2)))


# Test
# print(longest('xyaabbbccccdefww', 'xxxxyyyyabklmopq'))

s = 'xyaabbbccccdefww'
li = [*s]
# li = list(s)
# print(li)
# print(set(li))

st = set(s)
print(st)

print(sorted(st))

print(li)

print(sorted(li))
