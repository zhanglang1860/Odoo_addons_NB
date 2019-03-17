def cal(a=1,b=1):
    result = a + b * 2
    return result


dic = {
    'b': 3,
    'a': 1
}

c = cal(b=1, a=2)
print(c)
d = cal(**dic)
print(d)
