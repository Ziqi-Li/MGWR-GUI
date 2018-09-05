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
    summary = summaryAbout(self) + summaryModel(self.results,self) + summaryGLM(self.results,self) + summaryGWR(self.results,self)
    with open(self.sumFileSavePath.text(), "w") as text_file:
        print(summary, file=text_file)

def saveSummaryMGWR(self):
    summary = summaryAbout(self) + summaryModel(self.results,self) + summaryGLM(self.results,self) + summaryMGWR(self.results,self)
    with open(self.sumFileSavePath.text(), "w") as text_file:
        print(summary, file=text_file)

def saveProcessToCSVMGWR(self):
    bw = self.bw
    processDF = pd.concat([pd.DataFrame(bw.bw[1]), pd.DataFrame(bw.bw[2]),pd.DataFrame(bw.bw[3])], axis=1)
    processDF.columns = ['bw_'+ x for x in self.XNames] + [self.criterion +'_'+ x for x in self.XNames] + [self.SOC]
    processDF.to_csv(self.betaFileSavePath.text()[:-10]+'_process.csv',sep=',',index=True)

def saveBetasToCSVMGWR(self):
    resultsDF = pd.DataFrame(np.column_stack((self.id,self.xCoor,self.yCoor,self.y,self.results.predy,self.results.resid_response,self.results.params,self.results.bse,self.results.tvalues)))
    resultsDF.columns = ['GeoID','x_coor','y_coor','y','yhat','residual'] + ['beta_'+ x for x in self.XNames] + ['se_'+ x for x in self.XNames] + ['t_'+ x for x in self.XNames]
    
    if self.locollinear != "Off":
        old_columns = resultsDF.columns
        resultsDF = pd.concat([resultsDF,pd.DataFrame(np.column_stack([self.locollinearResults[-2],self.locollinearResults[-1]]))],axis=1)
        resultsDF.columns = list(old_columns) + ['local_CN'] + ['local_vdp_'+ x for x in self.XNames]
    
    resultsDF.to_csv(self.betaFileSavePath.text(),sep=',',index=False)

def saveBetasToCSVGWR(self):
    if isinstance(self.family, Gaussian):
        resultsDF = pd.DataFrame(np.column_stack((self.id,self.xCoor,self.yCoor,self.y,self.results.predy,self.results.resid_response,self.results.localR2,self.results.influ,self.results.cooksD,self.results.params,self.results.bse,self.results.tvalues)))
        resultsDF.columns = ['GeoID','x_coor','y_coor','y','yhat','residual','localR2','influ','CooksD'] + ['beta_'+ x for x in self.XNames] + ['se_'+ x for x in self.XNames] + ['t_'+ x for x in self.XNames]
    else:
        resultsDF = pd.DataFrame(np.column_stack((self.id,self.xCoor,self.yCoor,self.y,self.results.predy,self.results.resid_response,self.results.pDev,self.results.influ,self.results.cooksD,self.results.params,self.results.bse,self.results.tvalues)))
        resultsDF.columns = ['GeoID','x_coor','y_coor','y','yhat','residual','pDev','influ','CooksD'] + ['beta_'+ x for x in self.XNames] + ['se_'+ x for x in self.XNames] + ['t_'+ x for x in self.XNames]

    if self.locollinear != "Off":
        old_columns = resultsDF.columns
        resultsDF = pd.concat([resultsDF,pd.DataFrame(np.column_stack([self.locollinearResults[-2],self.locollinearResults[-1]]))],axis=1)
        resultsDF.columns = list(old_columns) + ['local_CN'] + ['local_vdp_'+ x for x in self.XNames]


    resultsDF.to_csv(self.betaFileSavePath.text(),sep=',',index=False)



'''
def summaryGWR(self):
    self.summary = ''
    
    self.summary += '*' * 75 + '\n'
    self.summary += '*' + ' ' * 73 + '*' + '\n'
    self.summary += '*' + ' ' * 73 + '*' + '\n'
    self.summary += '*' + ' ' * 73 + '*' + '\n'
    self.summary += '*' * 75 + '\n'
    self.summary += "%s\n" % ('<< Summary: Geographically Weighted Regression >>')
    self.summary += '-' * 75 + '\n'
    
    self.summary += "%-45s \n" % ('GWR Mode: GWR')
    self.summary += "%-21s: %s %s\n" % ('Program started at:', datetime.date(self.begin_t), datetime.strftime(self.begin_t,"%H:%M:%S"))
    self.summary += "%-21s: %s %s\n" % ('Program terminated at:', datetime.date(self.end_t), datetime.strftime(self.end_t,"%H:%M:%S"))
    self.summary += "%-21s: %s\n\n" % ('Program running time:', str(self.end_t - self.begin_t))
    self.summary += "%s %s\n" % ('Data filename:', self.openDataPath.text())
    self.summary += "%-45s %d\n" % ('Number of observations:', self.nObs)
    self.summary += "%-45s %d\n" % ('Number of Local Variables:', len(self.XNames))
    self.summary += "\n"
    
    
    self.summary += "%s\n" % ('<< Model Settings >>')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-45s %s\n" % ('Model type', self.modelTypeDropdown.currentText() + ' GWR')
    self.summary += "%-45s %s\n" % ('Spatial kernel:', self.fixedBox.currentText() + ' ' + self.shapeBox.currentText())
    self.summary += "%-45s %s\n" % ('Method for optimal bandwidth search:', self.bwDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Criterion for optimal bandwidth:', self.optimCriDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Number of coefficients:', len(self.XNames))
    self.summary += "%-45s %s\n\n" % ('Termination criterion for GWR:', self.tol_gwr)
    
    self.summary += "%s\n" % ('<< Variable Settings >>')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-60s %s\n" % ('Geo ID:', self.idLabel.text())
    self.summary += "%-60s %s\n" % ('X-Coordinates:', self.xCoorLabel.text())
    self.summary += "%-60s %s\n" % ('Y-Coordinates:', self.yCoorLabel.text())
    self.summary += "%-60s %s\n" % ('Coordinates Type:', self.coorType)
    self.summary += "%-60s %s\n" % ('Dependent variable:', self.responseLabel.text())
    for xVar in self.XNames:
        self.summary += "%-60s %s\n" % ('Independent variable with varying coefficient:', xVar)
    
    
    self.summary += "\n%s\n" %('<< Global Regression Results >>')
    self.summary += '-' * 75 + '\n'
    self.summary += "%s\n" % ('Diagnostic Information')
    self.summary += "%-45s %12.6f\n" %  ('Residual sum of squares:', self.GLMResult.deviance)
    self.summary += "%-45s %12.6f\n" %  ('ML based global sigma estimate:', 1.0000)
    self.summary += "%-45s %12.6f\n" %  ('Unbiased based global sigma estimate:', 1.0000)
    self.summary += "%-45s %12.6f\n" %  ('-2Log-likelihood:', -2*self.GLMResult.llf)
    self.summary += "%-45s %12.6f\n" % ('Classic AIC:', self.GLMResult.aic)
    self.summary += "%-45s %12.6f\n" % ('AICc:', self.GLMResult.aicc)
    #self.summary += "%-45s %12.6f\n" %  ('BIC/MDL:', self.GLMResult.bic)
    
    if isinstance(self.family, Gaussian):
        self.summary += "%-45s %12.6f\n" %  ('CV:', 1.0000)
        self.summary += "%-45s %12.6f\n" % ('R2', self.GLMResult.D2)
        self.summary += "%-45s %12.6f\n\n" % ('Adj. R2', self.GLMResult.adj_D2)
        self.summary += "%-20s %10s %20s %10s %10s" % ('Variable', 'Estimate', 'Standard Error' ,'t(Est/SE)', 'p-value')
    else:
        self.summary += "%-45s %12.6f\n" % ('Null deviance:', self.GLMResult.null_deviance)
        self.summary += "%-45s %12.6f\n" % ('Residual deviance:', self.GLMResult.deviance)
        self.summary += "%-45s %12.6f\n\n" % ('Percent deviance explained:', self.GLMResult.D2)
        self.summary += "%-20s %10s %20s %10s %10s" % ('Variable', 'Estimate', 'Standard Error' ,'z(Est/SE)', 'p-value')

    
    self.summary += "\n"
    self.summary += "%-20s %10s %20s %10s %10s\n" % ('-'*20, '-'*10 ,'-'*20, '-'*10,'-'*10)
    for i in range(len(self.XNames)):
        self.summary += "%-20s %10.6f %20.6f %10.6f %10.6f\n" % (self.XNames[i], self.GLMResult.params[i], self.GLMResult.bse[i], self.GLMResult.tvalues[i], self.GLMResult.pvalues[i])


    self.summary += "\n%s\n" %('<< Geographically Weighted Regression (GWR) Results >>')
    self.summary += "\n%s\n" %('GWR bandwidth selection')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-20s %20s\n" % ('Optimal Bandwidth:', self.bw)
    ###Search process?


    self.summary += "\n%s\n" % ('Diagnostic Information')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-60s %12.6f\n" % ('Residual sum of squares:', self.results.resid_ss)
    self.summary += "%-60s %12.6f\n" % ('Effective number of parameters (trace(S)):', self.results.tr_S)
    self.summary += "%-60s %12.6f\n" % ('Residual Degree of freedom (n - trace(S)):', self.results.df_model)
    #self.summary += "%-60s %12.6f\n" % ('Degree of freedom (residual: n - 2trace(S) + trace(S' + "'" + 'S)):', self.results.df_resid)
    self.summary += "%-60s %12.6f\n" % ('Sigma estimate:', np.sqrt(self.results.sigma2))
    self.summary += "%-60s %12.6f\n" % ('-2Log-likelihood:', -2*self.results.llf)
    self.summary += "%-60s %12.6f\n" % ('Classic AIC:', self.results.aic)
    self.summary += "%-60s %12.6f\n" % ('AICc:', self.results.aicc)
    self.summary += "%-60s %12.6f\n" % ('BIC:', self.results.bic)

    if isinstance(self.family, Gaussian):
        self.summary += "%-60s %12.6f\n" % ('CV:', self.results.cv)
        self.summary += "%-60s %12.6f\n" % ('R2:', self.results.R2)
        self.summary += "%-60s %12.6f\n" % ('Adj. R2:', self.results.adjR2)

        #self.summary += "%-60s %12.6f\n" % ('Null deviance:', 0)
        #self.summary += "%-60s %12.6f\n" % ('Residual deviance:', 0)
        #self.summary += "%-60s %12.6f\n" % ('Percent deviance explained:', 0)

    self.summary += "%-60s %12.6f\n" % ('Adj. alpha at 95%:', self.results.adj_alpha[1])
    self.summary += "%-60s %12.6f\n" % ('Adj. t-value at 95%:', self.results.critical_tval(self.results.adj_alpha[1]))

    self.summary += "\n"

    self.summary += "%s\n" % ('Geographically Varying (Local) Coefficients')
    self.summary += '-' * 75 + '\n'
    
    self.summary += "%s\n\n" % ('Summary statistics for varying (Local) coefficients')
    self.summary += "%-20s %20s %20s\n" % ('Variable', 'Mean' ,'STD')
    self.summary += "%-20s %20s %20s\n" % ('-'*20, '-'*20 ,'-'*20)
    for i in range(len(self.XNames)):
        self.summary += "%-20s %20.6f %20.6f\n" % (self.XNames[i], np.mean(self.results.params[:,i]) ,np.std(self.results.params[:,i]))
    self.summary += "\n"
    self.summary += "%-20s %20s %20s %20s\n" % ('Variable', 'Min' ,'Max', 'Range')
    self.summary += "%-20s %20s %20s %20s\n" % ('-'*20, '-'*20 ,'-'*20, '-'*20)
    for i in range(len(self.XNames)):
        self.summary += "%-20s %20.6f %20.6f %20.6f\n" % (self.XNames[i], np.min(self.results.params[:,i]) ,np.max(self.results.params[:,i]), np.max(self.results.params[:,i])-np.min(self.results.params[:,i]))
    self.summary += "\n"
    self.summary += "%-20s %20s %20s %20s\n" % ('Variable', 'Lwr Quartile' ,'Median', 'Upr Quartile')
    self.summary += "%-20s %20s %20s %20s\n" % ('-'*20, '-'*20 ,'-'*20, '-'*20)
    for i in range(len(self.XNames)):
        quan = mquantiles(self.results.params[:,i])
        self.summary += "%-20s %20.6f %20.6f %20.6f\n" % (self.XNames[i], quan[0],np.median(self.results.params[:,i]), quan[2])
    self.summary += "\n"
    self.summary += "%-20s %20s %20s\n" % ('Variable', 'Interquartile R' ,'Robust STD')
    self.summary += "%-20s %20s %20s\n" % ('-'*20, '-'*20 ,'-'*20)
    for i in range(len(self.XNames)):
        quan = mquantiles(self.results.params[:,i])
        self.summary += "%-20s %20.6f %20.6f\n" % (self.XNames[i], quan[2]-quan[0], (quan[2]-quan[0])/1.349)
    self.summary += "\n"
    self.summary += "%s\n" % ('(Note: Robust STD is given by (interquartile range / 1.349) )')
    self.summary += "\n"


    ###ANOVA TABLE
    df_gwr = self.results.df_resid
    df_glo = self.nObs - len(self.XNames)
    rss_gwr = self.results.resid_ss
    rss_glo = self.GLMResult.deviance
    ms_gwr = rss_gwr/df_gwr
    ms_imp = (rss_glo-rss_gwr)/(df_glo-df_gwr)
    if isinstance(self.family, Gaussian):
        self.summary += "%s\n" %('<< GWR ANOVA Table >>')
        self.summary += '-' * 75 + '\n'
        self.summary += "%-16s %16s %16s %16s %16s\n" % ('Source', 'SS', 'DF', 'MS', 'F')
        self.summary += "%-16s %16s %16s %16s %16s\n" % ('-'*16, '-'*16, '-'*16, '-'*16, '-'*16)
        self.summary += "%-16s %16.3f %16.3f\n" % ('Global Residuals', rss_glo, df_glo)
        self.summary += "%-16s %16.3f %16.3f %16.3f\n" % ('GWR Improvement', rss_glo-rss_gwr, df_glo-df_gwr, ms_imp)
        self.summary += "%-16s %16.3f %16.3f %16.3f %16.3f\n" % ('GWR Residuals', rss_gwr, df_gwr, rss_gwr/df_gwr, ms_imp/ms_gwr)

    else:
        self.summary += "%s\n" %('<< GWR Analysis of Deviance Table >>')
        self.summary += '-' * 75 + '\n'
        self.summary += "%-16s %16s %16s %16s\n" % ('Source', 'Deviance', 'DF', 'Deviance/DF')
        self.summary += "%-16s %16s %16s %16s\n" % ('-'*16, '-'*16, '-'*16, '-'*16)
        self.summary += "%-20s %12.6f %12.6f %12.6f\n" % ('Global Model', rss_glo, df_glo,rss_glo/df_glo)
        self.summary += "%-20s %12.6f %12.6f %12.6f\n" % ('GWR Model', rss_gwr, df_gwr, rss_gwr/df_gwr)
        self.summary += "%-20s %12.6f %12.6f %12.6f\n" % ('Difference', rss_glo-rss_gwr, df_glo-df_gwr, ms_imp)


    with open(self.sumFileSavePath.text(), "w") as text_file:
        print(self.summary, file=text_file)




def summaryMGWR(self):
    self.summary = ''
    self.summary += '*' * 75 + '\n'
    self.summary += '*' + ' ' * 73 + '*' + '\n'
    self.summary += '*' + ' ' * 73 + '*' + '\n'
    self.summary += '*' + ' ' * 73 + '*' + '\n'
    self.summary += '*' * 75 + '\n'
    self.summary += "%s\n" % ('<< Summary: Multi-Scale Geographically Weighted Regression (MGWR) >>')
    self.summary += '-' * 75 + '\n'
    
    self.summary += "%-45s \n" % ('GWR Mode: Multi-scale GWR')
    self.summary += "%-21s: %s %s\n" % ('Program started at:', datetime.date(self.begin_t), datetime.strftime(self.begin_t,"%H:%M:%S"))
    self.summary += "%-21s: %s %s\n" % ('Program terminated at:', datetime.date(self.end_t), datetime.strftime(self.end_t,"%H:%M:%S"))
    self.summary += "%-21s: %s\n\n" % ('Program running time:', str(self.end_t - self.begin_t))
    self.summary += "%s %s\n" % ('Data filename:', self.openDataPath.text())
    self.summary += "%-45s %d\n" % ('Number of observations:', self.nObs)
    self.summary += "%-45s %d\n" % ('Number of Local Variables:', len(self.XNames))
    self.summary += "\n"
    
    
    self.summary += "%s\n" % ('<< Model settings >>')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-45s %s\n" % ('Spatial kernel:', self.fixedBox.currentText() + ' ' + self.shapeBox.currentText())
    self.summary += "%-45s %s\n" % ('Method for optimal bandwidth search:', self.bwDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Criterion for optimal bandwidth:', self.optimCriDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Number of coefficients:', len(self.XNames))
    self.summary += "%-45s %s\n" % ('Initialization choice:', self.initBeta)
    self.summary += "%-45s %s\n" % ('Score of Change (SOC) type:', self.SOC)
    self.summary += "%-45s %s\n" % ('Termination criterion for GWR:', self.tol_gwr)
    self.summary += "%-45s %s\n\n" % ('Termination criterion for MGWR:', self.tol_multi)
    
    self.summary += "%s\n" % ('<< Variable settings >>')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-60s %s\n" % ('Geo ID:', self.idLabel.text())
    self.summary += "%-60s %s\n" % ('X-Coordinates:', self.xCoorLabel.text())
    self.summary += "%-60s %s\n" % ('Y-Coordinates:', self.yCoorLabel.text())
    self.summary += "%-60s %s\n" % ('Coordinates Type:', self.coorType)
    self.summary += "%-60s %s\n" % ('Dependent variable:', self.responseLabel.text())
    for xVar in self.XNames:
        self.summary += "%-60s %s\n" % ('Independent variable with varying coefficient:', xVar)
    
    self.summary += "\n%s\n" %('<< Global regression result >>')
    self.summary += '-' * 75 + '\n'
    self.summary += "%s\n" % ('Diagnostic information')
    self.summary += "%-45s %12.6f\n" %  ('Residual sum of squares:', self.GLMResult.deviance)
    self.summary += "%-45s %12.6f\n" %  ('-2Log-likelihood:', -2*self.GLMResult.llf)
    self.summary += "%-45s %12.6f\n" %  ('Classic AIC:', self.GLMResult.aic)
    self.summary += "%-45s %12.6f\n" %  ('AICc:', self.GLMResult.aicc)
    self.summary += "%-45s %12.6f\n" %  ('BIC/MDL:', self.GLMResult.bic)
    self.summary += "%-45s %12.6f\n" %  ('R2', self.GLMResult.D2)
    self.summary += "%-45s %12.6f\n\n" % ('Adj. R2', self.GLMResult.adj_D2)
    
    self.summary += "%-20s %10s %20s %10s %10s\n" % ('Variable', 'Estimate', 'Standard Error' ,'t(Est/SE)', 'p-value')
    self.summary += "%-20s %10s %20s %10s %10s\n" % ('-'*20, '-'*10 ,'-'*20, '-'*10,'-'*10)
    for i in range(len(self.XNames)):
        self.summary += "%-20s %10.6f %20.6f %10.6f %10.6f\n" % (self.XNames[i], self.GLMResult.params[i], self.GLMResult.bse[i], self.GLMResult.tvalues[i], self.GLMResult.pvalues[i])
    
    self.summary += "\n"


    self.summary += "%s\n" %('<< Multi-scale Geographically Weighted Regression (MGWR) results >>')
    self.summary += "\n%s\n" %('MGWR bandwidth selection')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-20s %30s %20s\n" % ('Variable', 'Optimal Bandwidth', 'ENP')
    for j in range(len(self.XNames)):
        self.summary += "%-20s %30.3f %20.3f\n" % (self.XNames[j], self.bws[j], self.results.ENP_j[j])

    self.summary += "\n%s\n" % ('Diagnostic information')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-60s %12.6f\n" % ('Residual sum of squares:', self.results.resid_ss)
    self.summary += "%-60s %12.6f\n" % ('Effective number of parameters (trace(S)):', self.results.tr_S)
    self.summary += "%-60s %12.6f\n" % ('Residual Degree of freedom (n - trace(S)):', self.results.df_model)
    #self.summary += "%-60s %12.6f\n" % ('Degree of freedom (residual: n - 2trace(S) + trace(S' + "'" + 'S)):', self.results.df_resid)
    self.summary += "%-60s %12.6f\n" % ('Sigma estimate:', np.sqrt(self.results.sigma2))
    self.summary += "%-60s %12.6f\n" % ('-2Log-likelihood:', -2*self.results.llf)
    self.summary += "%-60s %12.6f\n" % ('Classic AIC:', self.results.aic)
    self.summary += "%-60s %12.6f\n" % ('AICc:', self.results.aicc)
    self.summary += "%-60s %12.6f\n" % ('BIC:', self.results.bic)
    
    
    self.summary += '-' * 75 + '\n'
    self.summary += "%s\n" % ('Multiscale geographically varying (Local) coefficients')
    self.summary += '-' * 75 + '\n'

    self.summary += "%s\n\n" % ('Summary statistics for varying (Local) coefficients')
    self.summary += "%-20s %20s %20s\n" % ('Variable', 'Mean' ,'STD')
    self.summary += "%-20s %20s %20s\n" % ('-'*20, '-'*20 ,'-'*20)
    for i in range(len(self.XNames)):
        self.summary += "%-20s %20.6f %20.6f\n" % (self.XNames[i], np.mean(self.results.params[:,i]) ,np.std(self.results.params[:,i]))
    self.summary += "\n"

    self.summary += "%-20s %20s %20s %20s\n" % ('Variable', 'Min' ,'Max', 'Range')
    self.summary += "%-20s %20s %20s %20s\n" % ('-'*20, '-'*20 ,'-'*20, '-'*20)
    for i in range(len(self.XNames)):
        self.summary += "%-20s %20.6f %20.6f %20.6f\n" % (self.XNames[i], np.min(self.results.params[:,i]) ,np.max(self.results.params[:,i]), np.max(self.results.params[:,i])-np.min(self.results.params[:,i]))
    self.summary += "\n"
    
    self.summary += "%-20s %20s %20s %20s\n" % ('Variable', 'Lwr Quartile' ,'Median', 'Upr Quartile')
    self.summary += "%-20s %20s %20s %20s\n" % ('-'*20, '-'*20 ,'-'*20, '-'*20)
    for i in range(len(self.XNames)):
        quan = mquantiles(self.results.params[:,i])
        self.summary += "%-20s %20.6f %20.6f %20.6f\n" % (self.XNames[i], quan[0],np.median(self.results.params[:,i]), quan[2])
    self.summary += "\n"
    
    self.summary += "%-20s %20s %20s\n" % ('Variable', 'Interquartile R' ,'Robust STD')
    self.summary += "%-20s %20s %20s\n" % ('-'*20, '-'*20 ,'-'*20)
    for i in range(len(self.XNames)):
        quan = mquantiles(self.results.params[:,i])
        self.summary += "%-20s %20.6f %20.6f\n" % (self.XNames[i], quan[2]-quan[0], (quan[2]-quan[0])/1.349)
    self.summary += "\n"
    self.summary += "%s\n" % ('(Note: Robust STD is given by (interquartile range / 1.349) )')
    self.summary += "\n"
        
        
    print (self.summary)
    with open(self.sumFileSavePath.text(), "w") as text_file:
        print(self.summary, file=text_file)
'''


















