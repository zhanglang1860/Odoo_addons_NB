import psycopg2
import numpy as np


def connect_sql_chapter5(*turbine_list):
    db = psycopg2.connect(host='localhost', user='openpg', password='openpgpwd', port=5432, database='huarun123')
    print(db)
    cur = db.cursor()
    sql_str = ''

    for i in range(len(turbine_list)):
        if i == len(turbine_list) - 1:
            sql_str = "(" + sql_str + '\'%s\')'
        else:
            sql_str = sql_str + '\'%s\','

    # 第五章

    selectsql_tur = "SELECT * FROM autoreport_generator WHERE name_tur in " + sql_str
    selectsql_power = "SELECT * FROM autoreport_outputcurve WHERE name_output in " + sql_str
    selectsql_efficiency = "SELECT * FROM autoreport_efficiency WHERE name_efficiency in " + sql_str

    cur.execute(selectsql_tur % turbine_list)
    data_tur = cur.fetchall()  # 所有
    cur.execute(selectsql_power % turbine_list)
    data_power = cur.fetchall()  # 所有
    cur.execute(selectsql_efficiency % turbine_list)
    data_efficiency = cur.fetchall()  # 所有
    db.close()
    data_tur_np = np.array(data_tur)
    data_power_np = np.array(data_power)
    data_efficiency_np = np.array(data_efficiency)
    return data_tur_np, data_power_np, data_efficiency_np



# turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']
# data_tur_np, data_power_np, data_efficiency_np=connect_sql(*turbine_list)
# print(data_tur_np)


def connect_sql_chapter8(sql_foundation, *checklist):
    db = psycopg2.connect(host='localhost', user='zhangyicheng', password='12345', port=5432, database='Turbine')
    cur = db.cursor()
    cur.execute(sql_foundation % checklist)
    data_foundation = cur.fetchall()  # 所有
    db.close()
    data_foundation_np = np.array(data_foundation)
    return data_foundation_np


# from foundation_args_chapter8 import foundation_args_chapter8
# sql_foundation, key_vaule = foundation_args_chapter8(foundation_type='扩展基础', baseboard_r=11)
# foundation_np = connect_sql_chapter8(sql_foundation,*key_vaule)
# print(foundation_np)
