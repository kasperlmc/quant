import csv

c=open('D:\\workdata\\url.csv','w')
writer=csv.writer(c)
writer.writerow(['name','address','city','state'])
