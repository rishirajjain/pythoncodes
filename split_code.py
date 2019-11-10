import json,re,csv
with open('/home/karthik/Downloads/collect re.json') as json_file:
    data = json.load(json_file)

keys=data.keys()
values=data.values()
val="".join(values)
st=re.split('x = |y= |z=',val)
i=3
dat=''
lenn = len(st)
while i < lenn:
      dat=dat+" "+st[i]	
      i += 3
data=dat.split()		
print(data)


with open('data_z.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(data)

