class electrical:
    """
        定义第六章的相关内容
    """

    args_chapter6 = {'单回线路JL/G1A-240/30长度': 25.3, '双回线路JL/G1A-240/30长度': 23.6,
                     '直埋电缆YJLV22-26/35-3×95': 1.55, '直埋电缆YJV22-26/35-1×300': 3,
                     '风机台数': 31, '线路回路数': 5}

    args_chapter6_tower = {'J2-24': 2, 'J4-24': 1, 'FS-18': 4, 'Z2-30': 1, 'ZK-42': 4, 'SJ2-24': 4, 'SJ4-24': 4,
                           'SZ2-24': 4, 'SZ2-36': 4}

    def input_parameters(self, **kwargs):

        if '单回线路JL/G1A-240/30长度' in kwargs and '双回线路JL/G1A-240/30长度' in kwargs and '直埋电缆YJLV22-26/35-3×95' in kwargs \
                and '直埋电缆YJV22-26/35-1×300' in kwargs and '风机台数'in kwargs and'线路回路数'in kwargs:
            return True
        else:
            return False

    def cal_tower(self, **kwargs):
        for k_tower, v_tower in kwargs.items():
            if k_tower == "J2-24":
                print("J2-24")
            print(k, v)

    def generate_sql(self, tablename, **kwargs):
        """
        :param: dict 载入需要查询的字典key，以及对应的value。例如：
        args_chapter6 = {'单回线路JL/G1A-240/30长度': 25.3, '双回线路JL/G1A-240/30长度': 23.6,
                     '直埋电缆YJLV22-26/35-3×95': 1.55, '直埋电缆YJV22-26/35-1×300': 3,
                     '风机台数': 31, '线路回路数': 5}
        args_chapter8 = {'foundation_type': '扩展基础', 'max_load': 110000}
        :returns: 一个str语句 foundation_sql, key_value
        SELECT * FROM foundation_model WHERE %s = '%s' and %s = '%s'
        key_value ['foundation_type', '扩展基础', 'maxload', 110000]

        """
        sql_str = ''
        key_value = ['tablename', tablename]
        for k, v in kwargs.items():
            if sql_str == '':
                sql_str = sql_str + '%s' + ' = ' + '\'%s\''
            else:
                sql_str = sql_str + ' and ' + '%s' + ' = ' + '\'%s\''
            key_value.append(k)
            key_value.append(v)
        sql = "SELECT * FROM %s WHERE " + sql_str
        return sql, key_value

    _name = 'autoreport.electrical'
    _description = 'electrical input'
    _rec_name = 'project_id'
