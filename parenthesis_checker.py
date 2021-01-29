def test(t):
    res = []
    for i in t:
        if i in ["("]:
            res.append(i)
        else:
            if not res:
                return False
            j = res.pop()
            if j == '(':
                if i != ")":
                    return False
    if res:
        return False
    return True


a = input()
if test(a):
    print(a.count("("))
else:
    print(-1)
