def round_up(value, dec_digits=2):
    result = str(value).strip()
    if result != '':
        zero_count = dec_digits
        index_dec = result.find('.')
        if index_dec > 0:
            zero_count = len(result[index_dec + 1:])
            if zero_count > dec_digits:
                if int(result[index_dec + dec_digits + 1]) > 4:
                    result = str(value + pow(10, dec_digits * -1))
                    # 存在进位的可能，小数点会移位
                    index_dec = result.find('.')
                result = result[:index_dec + dec_digits + 1]
                zero_count = 0
            else:
                zero_count = dec_digits - zero_count
        else:
            result += '.'
        for i in range(zero_count):
            result += '0'
    return float(result)


# print(round_up(2.55, dec_digits=1))
#
# result = str(2.55).strip()
# index_dec = result.find('.')
# a = result[index_dec + 1:]
# print(result, index_dec, a)
