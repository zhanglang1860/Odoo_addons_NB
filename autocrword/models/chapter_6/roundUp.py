def roundUp(value, decDigits=0):
    result = str(value).strip()
    if result != '':
        zeroCount = decDigits
        indexDec = result.find('.')
        if indexDec > 0:
            zeroCount = len(result[indexDec + 1:])
            if zeroCount > decDigits:
                if int(result[indexDec + decDigits + 1]) > 4:
                    result = str(value + pow(10, decDigits * -1))
                    # 存在进位的可能，小数点会移位
                    indexDec = result.find('.')
                result = result[:indexDec + decDigits + 1]
                zeroCount = 0
            else:
                zeroCount = decDigits - zeroCount
        else:
            result += '.'
        for i in range(zeroCount):
            result += '0'
    return float(result)

print(roundUp(2.5,0))