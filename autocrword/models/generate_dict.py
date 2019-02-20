#  chapter 8
def get_dict(np, dict_keys):
    """
    结合传入np数组和dict_keys关键字参数，创建字典。注意一一对应。
    :param np:  传入数组
    :param dict_keys: 关键字字典
    :return: 返回字典

    """
    dict = {}
    for i in range(0, len(dict_keys)):
        key_dict = dict_keys[i]
        value_dict = np[:, i]
        dict[key_dict] = value_dict
    return dict


def write_context(dict, *context_keys):
    """
    根据context_keys的内容，找出dict内部的keys-value，并形成context，用以docx-temple
    :param dict: 输入的字典
    :param context_keys: context的特定值
    :return: 返回context字典
    """
    context = {}
    for i in context_keys:
        key = i
        value = dict.get(i, None)
        context[key] = value
    return context


def write_context_numbers(dict, *context_keys, numbers):
    """
    根据context_keys的内容，找出dict内部的keys-value，并形成context，用以docx-temple
    :param dict: 输入的字典
    :param context_keys: context的特定值
    :param numbers: 风机台数
    :return: 返回context字典
    """
    context = {}
    context['numbers'] = numbers
    for i in context_keys:
        key = i
        key_numbers = i + 'numbers'
        value = dict.get(i, None)
        if value != None:
            value = float('%.02f' % dict[key])
            value_numbers = float('%.02f' % (float(dict[key]) * numbers))
        else:
            value = None
            value_numbers = None
        context[key] = value
        context[key_numbers] = value_numbers
    return context


# ****************
#   测试调用
# from foundation_args_chapter8 import foundation_args_chapter8
# from connect_sql import connect_sql_chapter5, connect_sql_chapter8
# from connect_sql import connect_sql_chapter5, connect_sql_chapter8

# chapter 5
# turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']
# tur_np, power_np, efficiency_np = connect_sql_chapter5(*turbine_list)  # 一会儿注释connect_sql_chapter5
# print(tur_np)
# dict_keys_chapter5 = ['型号ID', '机组类型', '功率', '叶片数', '风轮直径', '扫风面积', '轮毂高度',
#                       '功率调节', '切入风速', '切出风速', '额定风速', '发电机型式', '额定功率', '电压', '频率',
#                       '塔架型式', '塔筒重量', '主制动系统', '第二制动', '3秒最大值']
# context_keys_chapter5 = ['机组类型', '机组类型', '叶片数', '风轮直径', '扫风面积', '轮毂高度', '功率调节', '切入风速',
#                          '切出风速', '额定风速', '发电机型式', '额定功率', '电压', '主制动系统', '第二制动']
# Dict_5 = get_dict(tur_np, dict_keys_chapter5)
# context = write_context(Dict_5, *context_keys_chapter5)
# print(context)
# chapter 8
# args_chapter8 = {'foundation_type': '扩展基础', 'max_load': 110000}
# sql_foundation, key_vaule = foundation_args_chapter8(**args_chapter8)
# foundation_np = connect_sql_chapter8(sql_foundation, *key_vaule)
#
# dict_keys = ['ID', '基础型式', '极限荷载', '设防烈度', '承载力', '土方比', '底板半径R', '棱台顶面半径R1', '台柱半径R2',
#              '底板外缘高度H1', '底板棱台高度H2', '台柱高度H3', '桩直径', '根数', '长度', '总桩长', '面积m2', '体积m3',
#              '垫层', '土方开挖', '石方开挖', '土石方回填', '复合地基换填', '复合地基桩']
# context_keys = ['土方开挖', '石方开挖', '土石方回填', '体积m3', '垫层', '钢筋', '基础防水', '沉降观测']
# numbers = 32
#
# Dict_8 = get_dict(foundation_np, dict_keys)
# context = write_context_numbers(Dict_8, *context_keys, numbers=numbers)
# context['钢筋'] = float('%.02f' % (Dict_8['体积m3'] / 10))
# context['钢筋numbers'] = float('%.02f' % (Dict_8['体积m3'] / 10 * numbers))
# context['基础防水'] = 1
# context['基础防水numbers'] = 1 * numbers
# context['沉降观测'] = 4
# context['沉降观测numbers'] = 4 * numbers
# print(context)
