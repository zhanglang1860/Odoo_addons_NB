from collector_circuit_flat import electrical

args_chapter6_tower = {'J2-24': 2, 'J4-24': 1, 'FS-18': 4, 'Z2-30': 1, 'ZK-42': 4, 'SJ2-24': 4, 'SJ4-24': 4,
                       'SZ2-24': 4, 'SZ2-36': 4}

args_chapter6 = {'单回线路JL/G1A-240/30长度': 25.3, '双回线路JL/G1A-240/30长度': 23.6,
                 '直埋电缆YJLV22-26/35-3×95': 1.55, '直埋电缆YJV22-26/35-1×300': 3,
                 '风机台数': 31, '线路回路数': 5}

chapter6 = electrical
# chapter6.cal(chapter6, **args_chapter6_tower)
a=chapter6.input_parameters(chapter6, **args_chapter6)
print(a)