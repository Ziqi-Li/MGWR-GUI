# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.stats.mstats import mquantiles
from datetime import datetime
import numpy as np
import pandas as pd
from spglm.family import Gaussian, Binomial, Poisson
from mgwrlib.mgwr.summary import *


def outputGWR(self):
    saveSummaryGWR(self)
    saveBetasToCSVGWR(self)


def outputMGWR(self):
    saveSummaryMGWR(self)
    saveBetasToCSVMGWR(self)
    #saveProcessToCSVMGWR(self)


def saveSummaryGWR(self):
    summary = summaryAbout(self) + summaryModel(
        self.results, self) + summaryGLM(self.results, self) + summaryGWR(
            self.results, self) + summaryACK(self)
    with open(self.sumFileSavePath.text(), "w") as text_file:
        print(summary, file=text_file)


def saveSummaryMGWR(self):
    summary = summaryAbout(self) + summaryModel(
        self.results, self) + summaryGLM(self.results, self) + summaryMGWR(
            self.results, self) + summaryACK(self)
    with open(self.sumFileSavePath.text(), "w") as text_file:
        print(summary, file=text_file)


def saveProcessToCSVMGWR(self):
    bw = self.bw
    processDF = pd.concat([
        pd.DataFrame(bw.bw[1]),
        pd.DataFrame(bw.bw[2]),
        pd.DataFrame(bw.bw[3])
    ],
                          axis=1)
    processDF.columns = ['bw_' + x for x in self.XNames
                         ] + [self.criterion + '_' + x
                              for x in self.XNames] + [self.SOC]
    processDF.to_csv(
        self.betaFileSavePath.text()[:-10] + '_process.csv',
        sep=',',
        index=True)


def saveBetasToCSVMGWR(self):
    resultsDF = pd.DataFrame(
        np.column_stack(
            (self.id, self.xCoor, self.yCoor, self.y, self.glm_rslt.resid_response, self.results.predy,
             self.results.resid_response, self.results.localR2,self.results.params,
             self.results.bse, self.results.tvalues, self.results.pvalues, self.results.sumW)))
    resultsDF.columns = [self.idName] + [
        'x_coor', 'y_coor', 'y', 'ols_residual','mgwr_yhat', 'mgwr_residual','localR2'
    ] + ['beta_' + x for x in self.XNames] + [
        'se_' + x for x in self.XNames
    ] + ['t_' + x for x in self.XNames] + ['p_' + x for x in self.XNames] + ['sumW_' + x for x in self.XNames]

    if self.locollinear != "Off":
        old_columns = resultsDF.columns
        resultsDF = pd.concat([
            resultsDF,
            pd.DataFrame(
                np.column_stack([
                    self.locollinearResults[-2], self.locollinearResults[-1]
                ]))
        ],
                              axis=1)
        resultsDF.columns = list(old_columns) + ['local_CN'] + [
            'local_vdp_' + x for x in self.XNames
        ]

    resultsDF.to_csv(self.betaFileSavePath.text(), sep=',', index=False)


def saveBetasToCSVGWR(self):
    if isinstance(self.family, Gaussian):
        resultsDF = pd.DataFrame(
            np.column_stack(
                (self.id, self.xCoor, self.yCoor, self.y, self.glm_rslt.resid_response, self.results.predy,
                 self.results.resid_response, self.results.localR2,
                 self.results.influ, self.results.cooksD, self.results.params,
                 self.results.bse, self.results.tvalues,
                 self.results.pvalues, self.results.sumW)))
        resultsDF.columns = [self.idName] + [
            'x_coor', 'y_coor', 'y', 'ols_residual', 'gwr_yhat', 'gwr_residual', 'localR2', 'influ',
            'CooksD'
        ] + ['beta_' + x for x in self.XNames] + [
            'se_' + x for x in self.XNames
        ] + ['t_' + x for x in self.XNames] + ['p_' + x for x in self.XNames] + ['sumW']
    else:
        resultsDF = pd.DataFrame(
            np.column_stack(
                (self.id, self.xCoor, self.yCoor, self.y, self.results.predy,
                 self.results.resid_response, self.results.pDev,
                 self.results.influ, self.results.cooksD, self.results.params,
                 self.results.bse, self.results.tvalues,
                 self.results.pvalues)))
        resultsDF.columns = [self.idName] + [
            'x_coor', 'y_coor', 'y', 'gwr_yhat', 'gwr_residual', 'pDev', 'influ',
            'CooksD'
        ] + ['beta_' + x for x in self.XNames] + [
            'se_' + x for x in self.XNames
        ] + ['t_' + x for x in self.XNames] + ['p_' + x for x in self.XNames]

    if self.locollinear != "Off":
        old_columns = resultsDF.columns
        names = self.XNames
        if "Intercept" in self.XNames:
            names = self.XNames[1:]
        resultsDF = pd.concat([
            resultsDF,
            pd.DataFrame(
                np.column_stack([
                    self.locollinearResults[-2], self.locollinearResults[-3],
                    self.locollinearResults[-1]
                ]))
        ],
                              axis=1)
        resultsDF.columns = list(old_columns) + ['local_CN'] + [
            'local_vif_' + x for x in names
        ] + ['local_vdp_' + x for x in self.XNames]

    resultsDF.to_csv(self.betaFileSavePath.text(), sep=',', index=False)
