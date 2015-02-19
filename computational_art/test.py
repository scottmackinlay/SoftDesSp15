def tester(stringy):
    if not stringy:
        return True
    if stringy[0]=='a' and stringy[-1]=='b':
        return tester(stringy[1:-1])
    else:
        return False


print tester('aaabbb')