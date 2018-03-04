#! /usr/bin/python

import re

def f1(a, b=0):
    return (a**2)+b

def f2(slowo):
    if slowo==[]:
        return "BUUM"
    else:
        return slowo[0]

def f3(klucz):
    if klucz == 1:
        return "jeden"
    elif klucz == 2:
        return "dwa"
    elif klucz == 3:
        return "trzy"
    elif klucz:
        return "other"

def f4(e, f=''):
    if f=='':
        return "%s ma kota" %e
    else:
        return  "%s ma kota i %s" %(e, f)

def f5(e, d=1):
    return range(e)[::d]
#    lista=[]
#    for i in range(17)[0:e:d]:
#        lista.append(i)
#        return lista


def f6(g, h):
    return g*h

def f7(slowo):
    if re.match("[a-z]+",slowo):
        return 'slowo'
    elif re.match("[0-9][0-9]+",slowo):
        return 'liczba'
    elif re.match("[0-9]",slowo):
        return 'cyfra'
    elif re.match("[-0-9]+",slowo):
        return 'liczba_ze_znakiem'
    elif re.match("[a-z A-Z ,.]+",slowo):
        return 'zdanie'
    elif re.match("[<a-z]+[a-z>]", slowo):
        return 'tag poczatkowy'
    elif re.match("[</a-z]+[a-z>]", slowo):
        return 'tag koncowy'
