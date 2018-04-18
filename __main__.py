# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:47:51 2018

@author: yinghuang
"""
import os
import fire

from pipCtrl import CtrlPip


PWD = os.path.split(os.path.realpath(__file__))[0]
shPath = os.path.join(PWD, 'piplib')


def main(pipName, infoCsv, refgenome, idir, odir, nproc=1):
    print('starting ...')
    if not os.path.exists(infoCsv):
        raise Exception("Path '{}' not exist.".format(infoCsv))
    elif not os.path.exists(idir):
        raise Exception("Path '{}' not exist.".format(idir))
    elif not os.path.exists(odir):
        print("Make directory '{}'.".format(odir))
        os.mkdir(odir)

    res = CtrlPip(pipName, nproc, infoCsv, refgenome, idir, odir)
    print(str(res))


def lst_pips():
    pips = os.listdir(shPath)
    return tuple(pips)


if __name__ == '__main__':
    pips = lst_pips()
    msg = '"pipName" are as follow: [{}] \n mapping'.format(' ,'.join(pips))
    fire.Fire(component=main, name=msg)
