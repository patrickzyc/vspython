# coding: utf-8


class productSN:
    family = '01'
    name = '00'
    Hversion = '12'
    Eversion = '13'
    DOM = '14100b1a'
    SN = '0001'


def SN(hh):
    hh = productSN(hh)
    return hh.family+hh.name+hh.Hversion+hh.Eversion+hh.DOM+hh.SN
