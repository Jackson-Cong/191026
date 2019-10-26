# -*-coding:UTF-8 -*-


def pnt_cut_line(sn):
    'Desc: Print a cutting line for me'
    print('\n--------------- No (%d) Cutting Line ----------------' % (sn))
    return


def cal_triangle_area(a, b, c):
    'Desc: Caclculate triangle''s area'
    p = (a + b + c) / 2

    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area
