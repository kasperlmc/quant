import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR,DynamicVAR
from statsmodels.tsa.base.datetools import dates_from_str
from arch.unitroot import ADF
from statsmodels.tsa.stattools import coint

def de_season(x):
    import statsmodels.tsa.seasonal as sts
    result=sts.seasonal_decompose(x,model='additive',freq=3)
    season=result.seasonal
    deseason=x-season
    return deseason

'导入数据'
data=pd.read_excel('D:\\workdata\\money.xlsx',index_col='date')
#print(data)
data.index=pd.to_datetime(data.index)
#print(type(data.index))
#print(data)
'定义变量'
loan_str=data['LL/SL']
gdp=data['估算GDP']
cpi=data['CPI']
cpi_sta=data['定基后CPI']
cpi_lrr=data['环比CPI']
m2=data['货币和准货币(M2)']
m1=data['货币(M1)']
m_qua=m2-m1
loan_long=data['中长期贷款']
loan_short=data['短期贷款']
stock_value=data['股市市值']
bond_value=data['债券市值']
m_str=m1/m_qua
loan_total=loan_short+loan_long
finance_value=stock_value+bond_value
'去除价格因素，'
gdp_cpi=gdp/cpi_sta
m2_cpi=m2/cpi_sta
loan_total_cpi=loan_total/cpi_sta
finance_value_cpi=finance_value/cpi_sta
cpi_nor=cpi/cpi_sta
#print(gdp_cpi,m2_cpi,loan_total_cpi)
'对数据进行对数处理'
lg_gdg=np.log(gdp_cpi)
lg_m2=np.log(m2_cpi)
lg_loan=np.log(loan_total_cpi)
lg_finance=np.log(finance_value_cpi)
lg_cpi=np.log(cpi_nor)
#print(lg_loan)
'去除季节因素'
l=[lg_gdg,lg_m2,lg_loan,cpi_lrr,m_str,loan_str,lg_finance,lg_cpi]
i=0
while i<len(l):
    l[i]=de_season(l[i])
    i+=1
lg_gdg=l[0]
lg_m2=l[1]
lg_loan=l[2]
cpi_lrr=l[3]
m_str=l[4]
loan_str=l[5]
lg_finance=l[6]
lg_cpi=l[7]
lg_gdg.name='gdp'
lg_m2.name='m2'
lg_loan.name='total_loan'
m_str.name='money_str'
lg_finance.name='finance_value'
cpi_lrr.name='cpi'
loan_str.name='loan_str'
lg_cpi.name='cpi_nor'

#print(ADF(lg_cpi).summary())
'''
'协整模型'
data1=pd.concat([lg_m2,m_str,lg_loan,lg_finance,loan_str],axis=1)
print(coint(lg_gdg,data1,trend='c',maxlag=15,autolag='aic'))
#print(data1)
data1=sm.add_constant(data1)
#print(type(data1))
model1=sm.OLS(lg_gdg,data1)
result1=model1.fit()
print(result1.summary())
alpha=result1.params[0]
beta0=result1.params[1]
beta1=result1.params[2]
beta2=result1.params[3]
beta3=result1.params[4]
beta4=result1.params[5]
spread=lg_gdg-alpha-beta0*lg_m2-beta1*m_str-beta2*lg_loan-beta3*lg_finance-beta4*loan_str
adfspread=ADF(spread,trend='nc')
print(adfspread.summary())
#spread.plot()
#plt.show()
'''

l1=[lg_gdg,lg_m2,lg_loan,cpi_lrr,m_str,loan_str,lg_finance]
'平稳性检验'
#for variable in l1:
#    print(ADF(variable).summary())
lg_gdg=lg_gdg.diff().dropna()
lg_m2=lg_m2.diff().dropna()
lg_loan=lg_loan.diff().dropna()
cpi_lrr=cpi_lrr.shift(1).dropna()
m_str=m_str.diff().dropna()
loan_str=loan_str.diff().dropna()
lg_finance=lg_finance.diff().dropna()
l2=[lg_gdg,lg_m2,lg_loan,cpi_lrr,m_str,loan_str,lg_finance]
#for variable in l2:
#    print(ADF(variable).summary())




'第一个VAR模型'
data0=pd.concat([lg_gdg,cpi_lrr,lg_m2,lg_loan,loan_str,m_str,lg_finance],axis=1)
#print(data0)
model0=VAR(data0)
#print(model0.select_order(15))
result0=model0.fit(maxlags=15,ic='aic')
print(result0.summary())
print('VAR模型稳定：%s'%result0.is_stable())
#print(result0.test_causality('cpi',['m2','money_str','loan_str','finance_value','total_loan','gdp'],kind='f'))
irf=result0.irf(10)
plt.figure(21)
plt.subplots(211)
irf.plot(impulse='m2',response='gdp')
plt.subplots(212)
irf.plot(impulse='m2',response='cpi')
plt.show()

'''
alpha=result1.params[0]
beta0=result1.params[1]
beta1=result1.params[2]
beta2=result1.params[3]
spread=lg_gdg-alpha-beta0*loan_str-beta1*m_str-beta2*lg_finance
adfspread=ADF(spread,trend='c')
print(adfspread.summary())
spread.plot()
plt.show()
'''