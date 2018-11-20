import pandas as pd

data=pd.read_excel('D:\\workdata\\testmoney.xlsx')
#print(data)
cpi=data.CPI
lagcpi=cpi.shift(1)
#print(cpi,lagcpi)
calcpi=pd.DataFrame({'cpi':cpi,'lagcpi':lagcpi})
print(calcpi)
huanbi=cpi/lagcpi
calcpi=pd.merge(calcpi,pd.DataFrame(huanbi),left_index=True,right_index=True)
print(calcpi)
writer=pd.ExcelWriter('D:\\workdata\\testmoney1.xlsx')
calcpi.to_excel(writer,'Sheet1')
writer.save()