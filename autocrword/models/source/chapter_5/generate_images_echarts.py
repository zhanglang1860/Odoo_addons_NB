# coding=utf=8
import os
import numpy as np
from pyecharts import Line
import connect_sql
import pandas as pd

turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']
data_tur_np, data_power_np, data_efficiency_np = connect_sql.connect_sql_chapter5(*turbine_list)

save_path = r'D:\Program Files (x86)\Odoo 12.0\server\addons\autocrword\models\chapter_5'


from eplot import eplot
df = pd.DataFrame([np.random.uniform(10,1,size=1000),
                   np.random.uniform(10,5,size=1000),
                   np.random.randint(1,high=10,size=1000),
                   np.random.choice(list('ABCD'),size=1000)],
                  index=['col1','col2','col3','col4']).T

print(df)
df.eplot.box('efficiency1.gif')

def generate_images(save_path, power_np, efficiency_np):
    png_box = ('powers', 'efficiency')

    speed = np.zeros(power_np.shape[1] - 6)  # 标注
    for i in range(0, power_np.shape[1] - 6):  # 标注
        if i == 0:
            speed[i] = 2.5
        else:
            speed[i] = i + 2
    power = power_np[:, 2: (power_np.shape[1] - 4)].astype('float32')  # 标注
    efficiency = efficiency_np[:, 2: (efficiency_np.shape[1] - 4)].astype('float32')  # 标注
    # Label
    turbine_power_model = power_np[:, 1]
    turbine_efficiency_model = efficiency_np[:, 1]
    # figure power
    line1 = Line("power")
    attr = [i for i in range(0, 24)]
    print(power)
    for i in range(0, len(turbine_power_model)):
        line1.add(turbine_power_model[i], attr, power[i], is_stack=False)

    path = os.path.join('.', 'powers.gif')
    print(path)
    line1.render('powers.gif')

    line2 = Line("efficiency")
    attr = [i for i in range(0, 24)]
    for i in range(0, len(turbine_efficiency_model)):
        line2.add(turbine_efficiency_model[i], attr, efficiency[i], is_stack=False)

    path = os.path.join(save_path, 'efficiency.gif')
    line2.render('efficiency.gif')


# generate_images(save_path, data_power_np, data_efficiency_np)
