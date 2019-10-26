#-*-coding:UTF-8 -*-

from my_pack.my_mod1 import cal_triangle_area, pnt_cut_line

# 输入一条分割线
pnt_cut_line(1)

area = cal_triangle_area(3,4,5)
if area < 0 :
    print('Error')
else:
    print('Area=%d'% area)
print(area)
