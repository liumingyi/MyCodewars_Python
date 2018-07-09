"""
题目：Count the smiley face <kyu6>

以一个列表作为参数的函数 contSmileys, 返回笑脸的数量。

笑脸判定标准：
- 每个笑脸必须包含一对眼睛，眼睛可以使用 ：or ；表示
- 一个笑脸可以有一个鼻子，也可以没有，鼻子可以用 - or ~ 表示
- 每个笑脸必须有一个微笑的嘴，可以使用 ) or D 表示
除了以上提到的符号，其他符号都是不允许的。
eg:
合法笑脸：:) :D ;-D :~)
非法笑脸：;( :> :} :]

方法示例：
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

"""

# Case.1
# def countSmileys(arr):
#     vali = {':', ';', ')', 'D', '-', '~'}
#     n = 0
#     for smiley in arr:
#         # 排除非法符号
#         if not set(smiley).issubset(vali):
#             continue
#         # 检查格式
#         if (':' in smiley or ';' in smiley) and (')' in smiley or 'D' in smiley):
#             n += 1
#     return n


from re import findall


# Case.2
# 使用正则表达式
def countSmileys(arr):
    return len(findall(r'[:;][-~]?[)D]', ''.join(arr)))


# Test
# should return 2;
print(countSmileys([':)', ';(', ';}', ':-D']))
# should return 3;
print(countSmileys([';D', ':-(', ':-)', ';~)']))
# should return 1;
print(countSmileys([';]', ':[', ';*', ':$', ';-D']))

s = ':)'

# valid = {':', ';', ')', 'D', '-', '~'}
valid = [':', ';', ')', 'D', '-', '~']

ls = list(s)

# bol = ls in valid
bol = set(ls).issubset(set(valid))

# print(bol)

items = [1, 2, 3, 4, 5]
it = [1, 2, 3, 4, 5]
