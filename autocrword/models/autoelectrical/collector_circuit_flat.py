class electrical:
    """
        定义第六章的相关内容
    """

    args_chapter6 = {'foundation_type': '预制桩承台基础', 'max_load': 100000}

    def generate_sql(self,tablename, **kwargs):
        """
        :param: dict 载入需要查询的字典key，以及对应的value。例如：
        args_chapter6 = {'foundation_type': '扩展基础', 'max_load': 110000}
        :returns: str, str foundation_sql, key_value
        SELECT * FROM foundation_model WHERE %s = '%s' and %s = '%s'
        key_value ['foundation_type', '扩展基础', 'maxload', 110000]

        """
        sql_str = ''
        key_value = ['tablename',tablename]
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

    def getname(self):
        return
