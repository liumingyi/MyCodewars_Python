"""
Simple Encryption #1 - Alternating Split

For building the encrypted string:
Take every 2nd char from the string,
then the other chars,
that are not every 2nd char,
and concat them as new String.
Do this n times!

Example:
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

创建一个加密字符串：
取出字符串的偶数位的字符，然后剩下了奇数位的字符，然后把他们连接起来形成一个新的字符串。
重复n次！

---
解释:
所有字符当然也就包括空格，下面用下划线（_）表示空格做个说明。

String:This_is_a_test!
角标   :121212121212121

取出角标为2的char：hsi__et
剩下的char: Ti_sats!
然后把他们连接起来就是："hsi__etTi_sats!" 即 "hsi  etTi sats!"
然后重复这个过程。      121212121212121

推断，此过程通过重复可以变回原始数据!
---


"""


def encrypt(text, n):
    for time in range(n):
        s1, s2 = '', ''
        for i in range(len(text)):
            if i % 2 == 1:
                s1 += text[i]
            else:
                s2 += text[i]
        text = s1 + s2
    return text


def decrypt(encrypted_text, n):
    for tiem in range(n):
        size = len(encrypted_text)
        ls0 = list(encrypted_text)
        ls1 = []
        ls2 = []
        ls2.extend(ls0[: size // 2])
        ls1.extend(ls0[size // 2:])
        result = []
        for i in range(len(ls2)):
            result.append(ls1[i])
            result.append(ls2[i])
        if size % 2 == 1:
            result.append(ls1[-1])
        encrypted_text = ''.join(result)
    return encrypted_text


# "hsi  etTi sats!"
print(encrypt('This is a test!', 1))
# "s eT ashi tist!"
print(encrypt('This is a test!', 2))
# "This is a test!"
print(decrypt('hsi  etTi sats!', 1))
# "hsi  etTi sats!"
print(decrypt('s eT ashi tist!', 1))
# "This is a test!"
print(decrypt('s eT ashi tist!', 2))

test = "1234567"
ls1 = list(test)
#
# ls2 = []
# ls2.extend(ls1)
#
# print(ls2)

# size = len(ls1)
#
# print(ls1[:size // 2])
#
# print(ls1[size // 2:])
#
# print(ls1[0:3])
