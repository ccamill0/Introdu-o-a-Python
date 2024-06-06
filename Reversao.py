def FirstReverse(strParam):
    i = -1
    b = strParam[i]
    while i > -len(strParam):
        b += strParam[i-1]
        i-=1
    strParam = b
    return strParam
