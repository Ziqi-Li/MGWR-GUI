import numpy as np
from spglm.family import Gaussian, Binomial, Poisson
from spglm.glm import GLM
from .diagnostics import get_AICc

def summaryAbout(self):
    summary = '=' * 80 + '\n'
    summary += 'MGWR Version: 2.2.0\n'
    summary += 'Released on: 11/20/2019\n'
    summary += 'Source code is available at: https://github.com/pysal/mgwr\n'
    summary += 'Development Team: Ziqi Li, Taylor Oshan, Stewart Fotheringham, Wei Kang, \n'
    summary += 'Levi Wolf, Hanchen Yu, and Mehak Sachdeva\n'
    summary += 'Spatial Analysis Research Center (SPARC)\n'
    summary += 'Arizona State University, Tempe, USA\n'
    return summary

def summaryModel(self,diag):
    summary = '=' * 80 + '\n'
    summary += "%-60s %19s\n" % ('Model type:', self.family.__class__.__name__)
    summary += "%-65s %14d\n" % ('Number of observations:', self.n)
    #summary += "%-65s %14d\n" % ('Number of missing rows:', diag.nMiss)
    summary += "%-65s %14d\n" % ('Number of covariates:', self.k)
    summary += "%-65s %14s\n" % ('Dependent variable:', diag.yName)
    if (diag.offset is not None):
        summary += "%-65s %14s\n" % ('Offset variable:', diag.OffsetLabel.text())
    if diag.isMGWR and diag.MGWRVarSTD:
        summary += "%-65s %14s\n" % ('Variable standardization:', diag.MGWRVarSTD)
    elif diag.isGWR and diag.GWRVarSTD:
        summary += "%-65s %14s\n" % ('Variable standardization:', diag.GWRVarSTD)

    summary += "%-50s %29s\n\n" % ('Total runtime:', str(diag.end_t - diag.begin_t).split('.', 2)[0])
    return summary

def summaryGLM(self,diag):
    
    glm_rslt = diag.glm_rslt

    summary = "%s\n" %('Global Regression Results')
    summary += '-' * 80 + '\n'
    
    if isinstance(self.family, Gaussian):
        summary += "%-67s %12.3f\n" %  ('Residual sum of squares:', glm_rslt.deviance)
        summary += "%-67s %12.3f\n" %  ('Log-likelihood:', glm_rslt.llf)
        summary += "%-67s %12.3f\n" %  ('AIC:', glm_rslt.aic)
        summary += "%-67s %12.3f\n" %  ('AICc:', get_AICc(glm_rslt))
        #summary += "%-67s %12.3f\n" %  ('BIC:', glm_rslt.bic)
        summary += "%-67s %12.3f\n" %  ('R2:', glm_rslt.D2)
        summary += "%-67s %12.3f\n\n" % ('Adj. R2:', glm_rslt.adj_D2)
    else:
        summary += "%-67s %12.3f\n" %  ('Deviance:', glm_rslt.deviance)
        summary += "%-67s %12.3f\n" %  ('Log-likelihood:', glm_rslt.llf)
        summary += "%-67s %12.3f\n" %  ('AIC:', glm_rslt.aic)
        summary += "%-67s %12.3f\n" %  ('AICc:', get_AICc(glm_rslt))
        #summary += "%-67s %12.3f\n" %  ('BIC:', glm_rslt.bic)
        summary += "%-67s %12.3f\n" %  ('Percent deviance explained:', glm_rslt.D2)
        summary += "%-67s %12.3f\n\n" % ('Adj. percent deviance explained:', glm_rslt.adj_D2)
    
    summary += "%-36s %10s %10s %10s %10s\n" % ('Variable', 'Est.', 'SE' ,'t(Est/SE)', 'p-value')
    summary += "%-36s %10s %10s %10s %10s\n" % ('-'*36, '-'*10 ,'-'*10, '-'*10,'-'*10)
    for i in range(self.k):
        summary += "%-36s %10.3f %10.3f %10.3f %10.3f\n" % (diag.XNames[i], glm_rslt.params[i], glm_rslt.bse[i], glm_rslt.tvalues[i], glm_rslt.pvalues[i])
    summary += "\n"
    return summary

def summaryGWR(self,diag):
    #XNames = ["X"+str(i) for i in range(self.k)]
    
    summary = "%s\n" %('Geographically Weighted Regression (GWR) Results')
    summary += '-' * 80 + '\n'
    if self.model.spherical:
        summary += "%-59s %20s\n" % ('Coordinates type:', 'Spherical')
    else:
        summary += "%-59s %20s\n" % ('Coordinates type:', 'Projected')
    
    if self.model.fixed:
        summary += "%-59s %20s\n" % ('Spatial kernel:', 'Fixed ' + self.model.kernel)
    else:
        summary += "%-59s %20s\n" % ('Spatial kernel:', 'Adaptive ' + self.model.kernel)

    summary += "%-59s %20s\n" % ('Criterion for optimal bandwidth:', diag.criterion)
    #summary += "%-65s %14s\n" % ('Multiple comparison correction:', diag.mcc)
    summary += "%-67s %12.3f\n" % ('Bandwidth used:', self.model.bw)
    if diag.bw_ci != "Off":
        summary += "%-59s %20s\n" % ('Bandwidth confidence interval (95%):', tuple2string(diag.bw_intervals))



    summary += "\n%s\n" % ('Diagnostic Information')
    summary += '-' * 80 + '\n'
    
    if isinstance(self.family, Gaussian):
        summary += "%-67s %12.3f\n" % ('Residual sum of squares:', self.resid_ss)
        summary += "%-67s %12.3f\n" % ('Effective number of parameters (trace(S)):', self.tr_S)
        summary += "%-67s %12.3f\n" % ('Degree of freedom (n - trace(S)):', self.df_model)
        summary += "%-67s %12.3f\n" % ('Sigma estimate:', np.sqrt(self.sigma2))
        summary += "%-67s %12.3f\n" % ('Log-likelihood:', self.llf)
        summary += "%-67s %12.3f\n" % ('Degree of Dependency (DoD):', self.DoD)
        summary += "%-67s %12.3f\n" % ('AIC:', self.aic)
        summary += "%-67s %12.3f\n" % ('AICc:', self.aicc)
        summary += "%-67s %12.3f\n" % ('BIC:', self.bic)
        summary += "%-67s %12.3f\n" % ('R2:', self.D2)
        summary += "%-67s %12.3f\n" % ('Adj. R2:', self.adj_D2)
    else:
        summary += "%-67s %12.3f\n" % ('Effective number of parameters (trace(S)):', self.tr_S)
        summary += "%-67s %12.3f\n" % ('Degree of freedom (n - trace(S)):', self.df_model)
        summary += "%-67s %12.3f\n" % ('Deviance:', self.global_deviance)
        summary += "%-67s %12.3f\n" % ('AIC:', self.aic)
        summary += "%-67s %12.3f\n" % ('AICc:', self.aicc)
        summary += "%-67s %12.3f\n" % ('BIC:', self.bic)
        summary += "%-67s %12.3f\n" % ('Percent deviance explained:', self.D2)
        summary += "%-67s %12.3f\n" % ('Adj. percent deviance explained:', self.adj_D2)


    summary += "%-67s %12.3f\n" % ('Adj. alpha (95%):', self.adj_alpha[1])
    summary += "%-67s %12.3f\n" % ('Adj. critical t value (95%):', self.critical_tval(self.adj_alpha[1]))

    if diag.mcTest != "Off":
        summary += "\n%s\n" %('Monte Carlo Test for Spatial Variability')
        summary += '-' * 80 + '\n'
        summary += "%-67s %12s\n" % ('Variable', 'p-value')
        for j in range(self.k):
            summary += "%-67s %12.3f\n" % (diag.XNames[j], diag.testMCResults[j])

    summary += "\n%s\n" % ('Summary Statistics For GWR Parameter Estimates')
    summary += '-' * 80 + '\n'
    summary += "%-25s %10s %10s %10s %10s %10s\n" % ('Variable', 'Mean' ,'STD', 'Min' ,'Median', 'Max')
    summary += "%-25s %10s %10s %10s %10s %10s\n" % ('-'*20, '-'*10 ,'-'*10, '-'*10 ,'-'*10, '-'*10)
    for i in range(self.k):
        summary += "%-25s %10.3f %10.3f %10.3f %10.3f %10.3f\n" % (diag.XNames[i], np.mean(self.params[:,i]) ,np.std(self.params[:,i]),np.min(self.params[:,i]) ,np.median(self.params[:,i]), np.max(self.params[:,i]))

    summary += '=' * 80 + '\n'

    return summary



def summaryMGWR(self,diag):
    
    summary = ''
    summary += "%s\n" %('Multiscale Geographically Weighted Regression (MGWR) Results')
    summary += '-' * 80 + '\n'
    
    if self.model.spherical:
        summary += "%-59s %20s\n" % ('Coordinates type:', 'Spherical')
    else:
        summary += "%-59s %20s\n" % ('Coordinates type:', 'Projected')

    if self.model.fixed:
        summary += "%-59s %20s\n" % ('Spatial kernel:', 'Fixed ' + self.model.kernel)
    else:
        summary += "%-59s %20s\n" % ('Spatial kernel:', 'Adaptive ' + self.model.kernel)

    summary += "%-59s %20s\n" % ('Criterion for optimal bandwidth:', self.model.selector.criterion)

    if self.model.selector.rss_score:
        summary += "%-59s %20s\n" % ('Score of change (SOC) type:', 'RSS')
    else:
        summary += "%-59s %20s\n" % ('Score of change (SOC) type:', 'Smoothing f')

    summary += "%-59s %20s\n" % ('Termination criterion for MGWR:', '{:.1e}'.format(self.model.selector.tol_multi))

    #summary += "%-65s %14s\n" % ('Multiple comparison correction:', diag.mcc)

    summary += "%-59s %20d\n\n" % ('Number of iterations used:', diag.selector.bw[1].shape[0])

    summary += "%s\n" %('MGWR bandwidths')
    summary += '-' * 80 + '\n'
    '''
    summary += "%-20s %14s %10s %16s %16s\n" % ('Variable', 'Bandwidth', 'ENP_j','Adj t-val(95%)','Adj alpha(95%)')
    for j in range(self.k):
        summary += "%-20s %14.3f %10.3f %16.3f %16.3f\n" % (diag.XNames[j], self.model.bws[j], self.ENP_j[j],self.critical_tval()[j],self.adj_alpha_j[j,1])
    '''
    summary += "%-20s %14s %10s %16s %16s\n" % ('Variable', 'Bandwidth', 'ENP_j','Adj t-val(95%)','DoD_j')
    for j in range(self.k):
        summary += "%-20s %14.3f %10.3f %16.3f %16.3f\n" % (diag.XNames[j], self.model.bws[j], self.ENP_j[j],self.critical_tval()[j],self.DoD_j[j])
    
    if diag.bw_ci != "Off":
        summary += "\n%s\n" %('Bandwidth Confidence Intervals (95%)')
        summary += '-' * 80 + '\n'
        for j in range(self.k):
            summary += "%-60s %20s\n" % (diag.XNames[j], tuple2string(diag.bw_intervals[j]))
    
    if diag.mcTest != "Off":
        summary += "\n%s\n" %('Monte Carlo Test for Spatial Variability')
        summary += '-' * 80 + '\n'
        summary += "%-67s %12s\n" % ('Variable', 'p-value')
        for j in range(self.k):
            summary += "%-67s %12.3f\n" % (diag.XNames[j], diag.testMCResults[j])
    

    summary += "\n%s\n" % ('Diagnostic Information')
    summary += '-' * 80 + '\n'
    
    summary += "%-67s %12.3f\n" % ('Residual sum of squares:', self.resid_ss)
    summary += "%-67s %12.3f\n" % ('Effective number of parameters (trace(S)):', self.tr_S)
    summary += "%-67s %12.3f\n" % ('Degree of freedom (n - trace(S)):', self.df_model)
    summary += "%-67s %12.3f\n" % ('Sigma estimate:', np.sqrt(self.sigma2))
    summary += "%-67s %12.3f\n" % ('Log-likelihood:', self.llf)
    summary += "%-67s %12.3f\n" % ('Degree of Dependency (DoD):', self.DoD)
    summary += "%-67s %12.3f\n" % ('AIC:', self.aic)
    summary += "%-67s %12.3f\n" % ('AICc:', self.aicc)
    summary += "%-67s %12.3f\n" % ('BIC:', self.bic)
    summary += "%-67s %12.3f\n" % ('R2:', self.D2)
    summary += "%-67s %12.3f\n" % ('Adj. R2:', self.adj_D2)

    summary += "\n%s\n" % ('Summary Statistics For MGWR Parameter Estimates')
    summary += '-' * 80 + '\n'
    summary += "%-25s %10s %10s %10s %10s %10s\n" % ('Variable', 'Mean' ,'STD', 'Min' ,'Median', 'Max')
    summary += "%-25s %10s %10s %10s %10s %10s\n" % ('-'*20, '-'*10 ,'-'*10, '-'*10 ,'-'*10, '-'*10)
    for i in range(self.k):
        summary += "%-25s %10.3f %10.3f %10.3f %10.3f %10.3f\n" % (diag.XNames[i], np.mean(self.params[:,i]) ,np.std(self.params[:,i]),np.min(self.params[:,i]) ,np.median(self.params[:,i]), np.max(self.params[:,i]))

    summary += '=' * 80 + '\n'
    return summary

def summaryACK(self):
    summary = 'Acknowledgement:\n'
    summary += 'We acknowledge the support of the National Science Foundation under Award 1758786 \nfrom the Geography and Spatial Sciences Program to A. S. Fotheringham which \nenabled this software to be written and made freely available.\n'
    summary += '=' * 80 + '\n'
    return summary

def tuple2string(tp):
    return "(" + str(tp[0]) + ", " + str(tp[1]) + ")"

