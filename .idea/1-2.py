import pandas as pd

data=pd.read_excel('D:\\workdata\\testmoney.xlsx',index_col='时间')
data=data.iloc[48:,:]
#print(data)
cpi=data.CPI
print(cpi)
basecpi=cpi/100.2
print(basecpi)
basecpi=pd.DataFrame(basecpi)
writer=pd.ExcelWriter('D:\\workdata\\testmoney2.xlsx')
basecpi.to_excel(writer,'Sheet1')
writer.save()