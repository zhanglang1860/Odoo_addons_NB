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


def round_dict_numbers(dic, numbers):
    for key_o in list(dic.keys()):
        # if type(dic[key_o]).__name__ != 'int':
        if 'numbers' not in key_o:
            if type(dic[key_o]).__name__ != 'int':
                dic[key_o] = round_up(dic[key_o], 2)
                key = key_o + '_numbers'
                dic[key] = round_up(dic[key_o] * numbers, 2)
            else:
                key = key_o + '_numbers'
                dic[key] = dic[key_o] * numbers
    return dic


def round_dict(dic):
    for key in dic:
        if type(dic[key]).__name__ != 'int':
            dic[key] = round_up(dic[key], 2)

    return dic
# print(round_up(2.55, dec_digits=1))
#
# result = str(2.55).strip()
# index_dec = result.find('.')
# a = result[index_dec + 1:]
# print(result, index_dec, a)
