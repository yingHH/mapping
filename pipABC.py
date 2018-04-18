# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:27:21 2018

@author: yinghuang
"""
import os


PWD = os.path.split(os.path.realpath(__file__))[0]
shPath = os.path.join(PWD, 'piplib')


class RunPip:

    def __init__(self, shName, ifiles, odir, refgenome):
        """
        shName:str
        ifiles:tuple
        odir:/path/to/out/dir
        """
        self.shName = shName
        if isinstance(ifiles, tuple):
            self.ifiles = ifiles
        else:
            msg = "Input is a '{}', 'ifiles' must be tuple.".format(type(ifiles))
            raise Exception(msg)
        self.odir = odir
        self.refgenome = refgenome

    def pipABC(self):
        script = os.path.join(shPath, self.shName)

        fq1, fq2 = self.ifiles

        if os.path.isfile(fq1) and os.path.isfile(fq2):
            cmd = 'bash {} {} {} {} {}'.format(
                script, fq1, fq2, self.odir, self.refgenome)
            print('> Mapping as "PE" type, command line is :\n... "{}".'.format(cmd))
            signal = os.system(cmd)
            return signal
        elif os.path.isfile(fq1) and not os.path.isfile(fq2):
            cmd = 'bash {} {} {} {}'.format(
                script, fq1, self.odir, self.refgenome)
            print('> Mapping as "SE" type, command line is :\n... "{}".'.format(cmd))
            signal = os.system(cmd)
            return signal
        else:
            msg = '> Warning: can not read file ["{}", "{}"] .'.format(fq1, fq2)
            print(msg)

    def __repr__(self):
        self.signal = self.pipABC()
        return "Shell return signal is {}".format(str(self.signal))
