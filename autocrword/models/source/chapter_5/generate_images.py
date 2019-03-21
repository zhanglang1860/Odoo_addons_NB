# coding=utf=8
import os
import numpy as np
import matplotlib.pyplot as plt

# def generate_images(save_path, turbine_list):
# turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']
# data_tur_np, data_power_np, data_efficiency_np = connect_sql.connect_sql_chapter5(*turbine_list)

def generate_images(save_path, power_np, efficiency_np):
    png_box = ('powers', 'efficiency')

    # tur_np, power_np, efficiency_np = connect_sql(*turbine_list)

    speed = np.zeros(power_np.shape[1] - 6)  # 标注
    for i in range(0, power_np.shape[1] - 6):  # 标注
        if i == 0:
            speed[i] = 2.5
        else:
            speed[i] = i + 2
    power = power_np[:, 2: (power_np.shape[1] - 4)].astype('float32')  # 标注
    efficiency = efficiency_np[:, 2: (efficiency_np.shape[1] - 4)].astype('float32')  # 标注
    turbine_power_model = power_np[:, 5]
    turbine_efficiency_model = efficiency_np[:, 1]
    print(turbine_power_model,turbine_power_model.shape)
    # figure power
    print(speed,power)
    print(speed.shape, power.shape)
    plt.figure(figsize=(5.6, 3.15))
    for i in range(len(power)):
        plt.plot(speed, power[i], label=turbine_power_model[i])
    plt.xlim((2.5, 25))
    plt.ylim((0.0, 4000.0))
    plt.xlabel("Wind speed")
    plt.ylabel("Power")
    new_ticks = np.linspace(0, 4000, 9)
    print(new_ticks)
    plt.yticks(new_ticks)
    plt.legend(loc='lower right')
    plt.subplots_adjust(left=0.115, right=0.965, wspace=0.200, hspace=0.200, bottom=0.145, top=0.96)
    plt.savefig(os.path.join(save_path, '%s.png') % png_box[0])

    # figure efficiency
    plt.figure(figsize=(5.6, 3.15))
    for i in range(len(efficiency)):
        plt.plot(speed, efficiency[i], label=turbine_efficiency_model[i])
    plt.xlim((3, 20))
    plt.ylim((0.0, 0.5))
    plt.xlabel("Wind speed")
    plt.ylabel("efficiency")
    new_ticks = np.linspace(3, 20, 18)
    print(new_ticks)
    plt.xticks(new_ticks)

    new_ticks = np.linspace(0, 0.5, 11)
    print(new_ticks)
    plt.yticks(new_ticks)
    plt.legend(loc='upper right')
    plt.subplots_adjust(left=0.115, right=0.965, wspace=0.200, hspace=0.200, bottom=0.145, top=0.96)
    plt.savefig(os.path.join(save_path, '%s.png') % png_box[1])


# save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_5'
# print(data_power_np,data_efficiency_np)
# generate_images(save_path, data_power_np, data_efficiency_np)
