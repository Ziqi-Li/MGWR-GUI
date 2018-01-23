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

def summaryGWR(self):
    self.summary = ''
    self.summary += "%s\n" % ('Summary: Geographically Weighted Regression')
    self.summary += '-' * 75 + '\n'
    
    self.summary += "%-45s \n" % ('GWR Mode: GWR')
    self.summary += "%-21s: %s %s\n" % ('Program started at:', datetime.date(self.begin_t), datetime.strftime(self.begin_t,"%H:%M:%S"))
    self.summary += "%-21s: %s %s\n" % ('Program terminated at:', datetime.date(self.end_t), datetime.strftime(self.end_t,"%H:%M:%S"))
    self.summary += "%-21s: %s\n\n" % ('Program running time:', str(self.end_t - self.begin_t))
    self.summary += "%s %s\n" % ('Data filename:', self.openDataPath.text())
    self.summary += "%-45s %d\n" % ('Number of observations:', self.nObs)
    self.summary += "%-45s %d\n" % ('Number of Local Variables:', len(self.XNames))
    self.summary += "\n"
    
    
    self.summary += "%s\n" % ('Model settings:')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-45s %s\n" % ('Model type', self.modelTypeDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Geographic kernel:', self.kernelDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Method for optimal bandwidth search:', self.bwDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Criterion for optimal bandwidth:', self.optimCriDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Number of coefficients:', len(self.XNames))
    self.summary += "%-45s %s\n\n" % ('Termination criterion for GWR:', self.tol_gwr)
    
    self.summary += "%s\n" % ('Variable settings:')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-60s %s\n" % ('Geo ID:', self.idLabel.text())
    self.summary += "%-60s %s\n" % ('X-Coordinates:', self.xCoorLabel.text())
    self.summary += "%-60s %s\n" % ('Y-Coordinates:', self.yCoorLabel.text())
    self.summary += "%-60s %s\n" % ('Coordinates Type:', self.coorType)
    self.summary += "%-60s %s\n" % ('Dependent variable:', self.responseLabel.text())
    for xVar in self.XNames:
        self.summary += "%-60s %s\n" % ('Independent variable with varying coefficient:', xVar)
    
    
    self.summary += "\n%s\n" %('Global regression result')
    self.summary += '-' * 75 + '\n'
    self.summary += "%s\n" % ('< Diagnostic information >')
    self.summary += "%-45s %12.6f\n" %  ('Residual sum of squares:', self.GLMResult.deviance)
    self.summary += "%-45s %12.6f\n" %  ('ML based global sigma estimate:', 1.0000)
    self.summary += "%-45s %12.6f\n" %  ('Unbiased based global sigma estimate:', 1.0000)
    self.summary += "%-45s %12.6f\n" %  ('-2Log-likelihood:', -2*self.GLMResult.llf)
    self.summary += "%-45s %12.6f\n" % ('Classic AIC:', self.GLMResult.aic)
    self.summary += "%-45s %12.6f\n" % ('AICc:', self.GLMResult.aicc)
    self.summary += "%-45s %12.6f\n" %  ('BIC/MDL:', self.GLMResult.bic)
    self.summary += "%-45s %12.6f\n" %  ('CV:', 1.0000)
    self.summary += "%-45s %12.6f\n" % ('R-square', self.GLMResult.D2)
    self.summary += "%-45s %12.6f\n" % ('Adjusted R-square', self.GLMResult.adj_D2)
    
    self.summary += "%-20s %10s %20s %10s %10s\n" % ('Variable', 'Estimate', 'Standard Error' ,'t(Est/SE)', 'p-value')
    self.summary += "%-20s %10s %20s %10s %10s\n" % ('-'*20, '-'*10 ,'-'*20, '-'*10,'-'*10)
    for i in range(len(self.XNames)):
        self.summary += "%-20s %10.6f %20.6f %10.6f %10.6f\n" % (self.XNames[i], self.GLMResult.params[i], self.GLMResult.bse[i], self.GLMResult.tvalues[i], self.GLMResult.pvalues[i])

    self.summary += "\n"

    self.summary += "%s\n" %('GWR (Geographically weighted regression) result')
    self.summary += "\n%s\n" %('GWR bandwidth selection')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-20s %20s\n" % ('Bandwidth', self.bw)
    ###Search process?


    self.summary += "\n%s\n" % ('Diagnostic information')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-45s %12.6f\n\n" % ('Residual sum of squares:', self.results.resid_ss)
    self.summary += "%-60s %12.6f\n" % ('Effective number of parameters (model: trace(S)):', self.results.tr_S)
    self.summary += "%-60s %12.6f\n" % ('Effective number of parameters (variance: trace(S' + "'" + 'S))', self.results.tr_STS)
    self.summary += "%-60s %12.6f\n" % ('Degree of freedom (model: n - trace(S)):', self.results.df_model)
    self.summary += "%-60s %12.6f\n" % ('Degree of freedom (residual: n - 2trace(S) + trace(S' + "'" + 'S)):', self.results.df_resid)
    self.summary += "%-45s %12.6f\n" % ('ML based sigma estimate:', np.sqrt(self.results.sigma2_ML))
    self.summary += "%-45s %12.6f\n" % ('Unbiased sigma estimate:', np.sqrt(self.results.sigma2_v1v2))
    self.summary += "%-45s %12.6f\n" % ('-2Log-likelihood:', -2*self.results.llf)
    self.summary += "%-45s %12.6f\n" % ('Classic AIC:', self.results.aic)
    self.summary += "%-45s %12.6f\n" % ('AICc:', self.results.aicc)
    self.summary += "%-45s %12.6f\n" % ('BIC:', self.results.bic)
    self.summary += "%-45s %12.6f\n" % ('CV:', self.results.cv)
    self.summary += "%-45s %12s\n" % ('R square:', 'NA')
    #self.summary += "%-45s %12.6f\n" % ('Adjusted R square:', '1.000')
    self.summary += "%-45s %12s\n" % ('Adjusted R square:', 'NA')
    self.summary += "\n"

    self.summary += '-' * 75 + '\n'
    self.summary += "%s\n" % ('<<Geographically varying (Local) coefficients >>')
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
    self.summary += "\n%s\n" %('GWR ANOVA Table')
    self.summary += '-' * 75 + '\n'

    with open(self.sumFileSavePath.text(), "w") as text_file:
        print(self.summary, file=text_file)




def summaryMGWR(self):
    self.summary = ''
    self.summary += "%s\n" % ('Summary: Multiscale Geographically Weighted Regression')
    self.summary += '-' * 75 + '\n'
    
    self.summary += "%-45s \n" % ('GWR Mode: Multi-scale GWR')
    self.summary += "%-21s: %s %s\n" % ('Program started at:', datetime.date(self.begin_t), datetime.strftime(self.begin_t,"%H:%M:%S"))
    self.summary += "%-21s: %s %s\n" % ('Program terminated at:', datetime.date(self.end_t), datetime.strftime(self.end_t,"%H:%M:%S"))
    self.summary += "%-21s: %s\n\n" % ('Program running time:', str(self.end_t - self.begin_t))
    self.summary += "%s %s\n" % ('Data filename:', self.openDataPath.text())
    self.summary += "%-45s %d\n" % ('Number of observations:', self.nObs)
    self.summary += "%-45s %d\n" % ('Number of Local Variables:', len(self.XNames))
    self.summary += "\n"
    
    
    self.summary += "%s\n" % ('Model settings:')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-45s %s\n" % ('Geographic kernel:', self.kernelDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Method for optimal bandwidth search:', self.bwDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Criterion for optimal bandwidth:', self.optimCriDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Number of coefficients:', len(self.XNames))
    self.summary += "%-45s %s\n" % ('Initialization choice:', self.initDropDown.currentText())
    self.summary += "%-45s %s\n" % ('Score of Change (SOC) type:', self.SOCDropdown.currentText())
    self.summary += "%-45s %s\n" % ('Termination criterion for GWR:', self.tol_gwr)
    self.summary += "%-45s %s\n\n" % ('Termination criterion for MGWR:', self.tol_multi)
    
    self.summary += "%s\n" % ('Variable settings:')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-60s %s\n" % ('Geo ID:', self.idLabel.text())
    self.summary += "%-60s %s\n" % ('X-Coordinates:', self.xCoorLabel.text())
    self.summary += "%-60s %s\n" % ('Y-Coordinates:', self.yCoorLabel.text())
    self.summary += "%-60s %s\n" % ('Coordinates Type:', self.coorType)
    self.summary += "%-60s %s\n" % ('Dependent variable:', self.responseLabel.text())
    for xVar in self.XNames:
        self.summary += "%-60s %s\n" % ('Independent variable with varying coefficient:', xVar)


    self.summary += "\n%s\n" %('MGWR bandwidth selection')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-20s %20s %20s\n" % ('Variable', 'Bandwidth', self.criterion)
    for i in range(len(self.XNames)):
        self.summary += "%-20s %20.6f %20.6f\n" % (self.XNames[i], self.bws[i], self.bw.bw[2][-1,i])

    self.summary += "\n%s\n" % ('Diagnostic information')
    self.summary += '-' * 75 + '\n'
    self.summary += "%-45s %12.6f\n\n" % ('Residual sum of squares:', self.results.resid_ss)
    
    
    self.summary += '-' * 75 + '\n'
    self.summary += "%s\n" % ('<< Multiscale Geographically varying (Local) coefficients >>')
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


















